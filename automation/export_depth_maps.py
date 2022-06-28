import os
import Metashape
import json
import glob



def export_depth_maps(input_path, output_path):
    """
    Exports depth maps from the project specified in the output path
    :param output_path: Specifies the path of the project.psx file
    """
    parameters = json.load(open(f"{input_path}{os.path.sep}parameters.json", "r"))

    if parameters["export_depth_maps"]:
        doc = Metashape.app.document
        doc.open(f"{output_path}{os.path.sep}project.psx")
        chunk = doc.chunk

        doc.read_only = False
        doc.save()
        doc.read_only = False

        if not chunk.model:

            f = Metashape.PointCloud.Filter()

            if parameters["filtering"]["reprojection_error"]:
                f.init(chunk, criterion=Metashape.PointCloud.Filter.ReprojectionError)
                f.removePoints(parameters["filtering"]["threshold_reprojection_error"])

            if parameters["filtering"]["reconstruction_uncertainty"]:
                f.init(chunk, criterion=Metashape.PointCloud.Filter.ReconstructionUncertainty)
                f.removePoints(parameters["filtering"]["threshold_reconstruction_uncertainty"])

            if parameters["filtering"]["image_count"]:
                f.init(chunk, criterion=Metashape.PointCloud.Filter.ImageCount)
                f.removePoints(parameters["filtering"]["threshold_image_count"])

            if parameters["filtering"]["reprojection_accuracy"]:
                f.init(chunk, criterion=Metashape.PointCloud.Filter.ProjectionAccuracy)
                f.removePoints(parameters["filtering"]["threshold_projection_accuracy"])

            chunk.buildModel(surface_type=getattr(Metashape, parameters["model"]["surface_type"]),
                             interpolation=getattr(Metashape, parameters["model"]["interpolation"]),
                             face_count=getattr(Metashape, parameters["model"]["face_count"]),
                             face_count_custom=parameters["model"]["face_count_custom"],
                             source_data=getattr(Metashape, parameters["model"]["source_data"]),
                             vertex_colors=parameters["model"]["vertex_colors"],
                             keep_depth=parameters["model"]["keep_depth"])
            doc.save()

        if chunk.transform.scale is None:
            scale = 1
            print("Scale set to 1")
        else:
            scale = chunk.transform.scale

        if os.path.exists(f"{output_path}{os.path.sep}depth_maps"):
            pass
        else:
            os.mkdir(f"{output_path}{os.path.sep}depth_maps")

        for camera in chunk.cameras:
            if camera.transform:
                depth = chunk.model.renderDepth(camera.transform, camera.calibration)
                depth = depth * scale
                depth = depth.convert(" ", "F16")
                compr = Metashape.ImageCompression()
                compr.tiff_compression = Metashape.ImageCompression().TiffCompressionDeflate
                depth.save(f"{output_path}{os.path.sep}depth_maps{os.path.sep}{camera.label}.tif")
                print(f"Depth map for {camera.label} exported successfully!")

        doc.save()
