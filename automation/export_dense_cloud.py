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

        chunk.buildDenseCloud(point_colors=True,
                              point_confidence=parameters["dense_cloud"]["point_confidence"],
                              keep_depth=parameters["dense_cloud"]["keep_depth"],
                              max_neighbors=parameters["dense_cloud"]["max_neighbors"],
                              subdivide_task=parameters["dense_cloud"]["subdivide_task"],
                              workitem_size_cameras=parameters["dense_cloud"]["workitem_size_cameras"],
                              max_workgroup_size=parameters["dense_cloud"]["max_workgroup_size"]
                              )
        doc.save()

        chunk.colorizeDenseCloud(source_data=Metashape.ImagesData)
        doc.save()

        chunk.exportPoints(path=f"{output_path}{os.path.sep}dense_cloud.las",
                           source_data=getattr(Metashape, parameters["export_dense_cloud"]["source_data"]),
                           binary=parameters["export_dense_cloud"]["binary"],
                           save_normals=parameters["export_dense_cloud"]["save_normals"],
                           save_colors=parameters["export_dense_cloud"]["save_colors"],
                           save_classes=parameters["export_dense_cloud"]["save_classes"],
                           save_confidence=parameters["export_dense_cloud"]["save_confidence"],
                           raster_transform=getattr(Metashape, parameters["export_dense_cloud"]["raster_transform"]),
                           colors_rgb_8bit=parameters["export_dense_cloud"]["colors_rgb_8bit"],
                           comment=parameters["export_dense_cloud"]["comment"],
                           save_comment=parameters["export_dense_cloud"]["save_comment"],
                           format=getattr(Metashape, parameters["export_dense_cloud"]["format"]),
                           image_format=getattr(Metashape, parameters["export_dense_cloud"]["image_format"]),
                           clip_to_boundary=parameters["export_dense_cloud"]["clip_to_boundary"],
                           block_width=parameters["export_dense_cloud"]["block_width"],
                           block_height=parameters["export_dense_cloud"]["block_height"],
                           split_in_blocks=parameters["export_dense_cloud"]["split_in_blocks"],
                           save_images=parameters["export_dense_cloud"]["save_images"],
                           compression=parameters["export_dense_cloud"]["compression"],
                           screen_space_error=parameters["export_dense_cloud"]["screen_space_error"],
                           subdivide_task=parameters["export_dense_cloud"]["subdivide_task"])
        doc.save()
