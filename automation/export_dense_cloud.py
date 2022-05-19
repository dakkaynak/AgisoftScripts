import os
import Metashape


def export_dense_cloud(output_path):
    """
    Exports dense cloud from the Metashape project specified in the output path.
    :param output_path: Specifies the path of the project.psx file
    """
   
    doc = Metashape.app.document
    doc.open(f"{output_path}{os.path.sep}project.psx")
    chunk = doc.chunk

    doc.read_only = False
    doc.save()
    doc.read_only = False

    chunk.buildDenseCloud(point_colors=True, point_confidence=False, keep_depth=True, max_neighbors=100, subdivide_task=True, workitem_size_cameras=20, max_workgroup_size=100)
    doc.save()

    chunk.colorizeDenseCloud(source_data=Metashape.ImagesData)
    doc.save()

    chunk.exportPoints(path=f"{output_path}{os.path.sep}dense_cloud.las", source_data=Metashape.DenseCloudData, binary=True, save_normals=True, save_colors=True, save_classes=True, save_confidence=True, raster_transform=Metashape.RasterTransformNone, colors_rgb_8bit=True, comment='', save_comment=True, format=Metashape.PointsFormatNone, image_format=Metashape.ImageFormatJPEG, clip_to_boundary=True, block_width=1000, block_height=1000, split_in_blocks=False, save_images=False, compression=True, screen_space_error=16, subdivide_task=True)
    doc.save()
