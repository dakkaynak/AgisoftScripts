import os
import Metashape


def export_depth_maps(output_path):
    """
    Exports depth maps from the project specified in the output path
    :param output_path: Specifies the path of the project.psx file
    """
   
    doc = Metashape.app.document
    doc.open(f"{output_path}{os.path.sep}project.psx")
    chunk = doc.chunk

    doc.read_only = False
    doc.save()
    doc.read_only = False

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
            depth = chunk.model.renderDepth(camera.transform, camera.sensor.calibration)
            depth = depth * scale
            depth = depth.convert(" ", "F16")
            compr = Metashape.ImageCompression()
            compr.tiff_compression = Metashape.ImageCompression().TiffCompressionDeflate
            depth.save(f"{output_path}{os.path.sep}depth_maps{os.path.sep}{camera.label}.tif")
            print(f"Depth map for {camera.label} exported successfully!")
    
    doc.save()
