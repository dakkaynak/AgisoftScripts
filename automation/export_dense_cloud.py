import os
import Metashape
import json


def export_dense_cloud(input_path, output_path):
    """
    Exports dense cloud from the Metashape project specified in the output path.
    :param output_path: Specifies the path of the project.psx file
    """
    parameters = json.load(open(f"{input_path}{os.path.sep}parameters.json", "r"))

    if parameters["export_dense_cloud"]:

        doc = Metashape.app.document
        doc.open(f"{output_path}{os.path.sep}project.psx")
        chunk = doc.chunk

        doc.read_only = False
        doc.save()
        doc.read_only = False

        chunk.buildDenseCloud(point_colors=True,
                              point_confidence=parameters["dense_point_confidence"],
                              keep_depth=parameters["dense_keep_depth"],
                              max_neighbors=parameters["dense_max_neighbors"],
                              subdivide_task=parameters["dense_subdivide_task"],
                              workitem_size_cameras=parameters["dense_workitem_size_cameras"],
                              max_workgroup_size=parameters["dense_max_workgroup_size"]
                              )
        doc.save()

        chunk.colorizeDenseCloud(source_data=Metashape.ImagesData)
        doc.save()

        chunk.exportPoints(path=f"{output_path}{os.path.sep}dense_cloud.las",
                           source_data=Metashape.DenseCloudData,
                           binary=parameters["exp_dense_binary"],
                           save_normals=parameters["exp_dense_save_normals"],
                           save_colors=parameters["exp_dense_save_colors"],
                           save_classes=parameters["exp_dense_save_classes"],
                           save_confidence=parameters["exp_dense_save_confidence"],
                           raster_transform=Metashape.RasterTransformNone,
                           colors_rgb_8bit=parameters["exp_dense_colors_rgb_8bit"],
                           comment=parameters["exp_dense_comment"],
                           save_comment=parameters["exp_dense_save_comment"],
                           format=Metashape.PointsFormatNone,
                           image_format=Metashape.ImageFormatJPEG,
                           clip_to_boundary=parameters["exp_dense_clip_to_boundary"],
                           block_width=parameters["exp_dense_block_width"],
                           block_height=parameters["exp_dense_block_height"],
                           split_in_blocks=parameters["exp_dense_split_in_blocks"],
                           save_images=parameters["exp_dense_save_images"],
                           compression=parameters["exp_dense_compression"],
                           screen_space_error=parameters["exp_dense_screen_space_error"],
                           subdivide_task=parameters["exp_dense_subdivide_task"])
        doc.save()
