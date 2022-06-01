import os
import Metashape
import json
import ast


def export_normal_maps(input_path, output_path):
    """
    Exports normal maps from the project specified in the output path
    :param output_path: Specifies the path of the project.psx file
    """
    parameters = json.load(open(f"{input_path}{os.path.sep}parameters.json", "r"))

    if parameters["export_normal_maps"]:
        doc = Metashape.app.document
        doc.open(f"{output_path}{os.path.sep}project.psx")
        chunk = doc.chunk

        doc.read_only = False
        doc.save()
        doc.read_only = False

        if not chunk.model:
            chunk.buildModel(surface_type=getattr(Metashape, parameters["model_surface_type"]),
                             interpolation=getattr(Metashape, parameters["model_interpolation"]),
                             face_count=getattr(Metashape, parameters["model_face_count"]),
                             face_count_custom=parameters["model_face_count_custom"],
                             source_data=getattr(Metashape, parameters["model_source_data"]),
                             vertex_colors=parameters["model_vertex_colors"],
                             keep_depth=parameters["keep_depth"])
            doc.save()
        if chunk.transform.scale is None:
            scale = 1
            print("Scale set to 1")
        else:
            scale = chunk.transform.scale

        if os.path.exists(f"{output_path}{os.path.sep}normal_maps"):
            pass
        else:
            os.mkdir(f"{output_path}{os.path.sep}normal_maps")

        for camera in chunk.cameras:
            if camera.transform:
                depth = chunk.model.renderNormalMap(camera.transform, camera.sensor.calibration)
                depth = depth * scale
                depth = depth.convert(" ", "F16")
                compr = Metashape.ImageCompression()
                compr.tiff_compression = Metashape.ImageCompression().TiffCompressionDeflate
                depth.save(f"{output_path}{os.path.sep}normal_maps{os.path.sep}{camera.label}.tif")
                print(f"Normal map for {camera.label} exported successfully!")

        doc.save()
