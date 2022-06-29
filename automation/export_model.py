import os
import Metashape
import json


def export_model(input_path, output_path):
    """
    Exports a model and texture from the project specified in the output path
    :param output_path: Specifies the path of the project.psx file
    """
    parameters = json.load(open(f"{input_path}{os.path.sep}parameters.json", "r"))

    if parameters["export_model"]:

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

        chunk.buildModel(surface_type=getattr(Metashape, parameters["model"]["surface_type"]),
                         interpolation=getattr(Metashape, parameters["model"]["interpolation"]),
                         face_count=getattr(Metashape, parameters["model"]["face_count"]),
                         face_count_custom=parameters["model"]["face_count_custom"],
                         source_data=getattr(Metashape, parameters["model"]["source_data"]),
                         vertex_colors=parameters["model"]["vertex_colors"],
                         keep_depth=parameters["model"]["keep_depth"])
        doc.save()

        chunk.buildUV(mapping_mode=getattr(Metashape, parameters["UV"]["mapping_mode"]),
                      page_count=parameters["UV"]["page_count"],
                      texture_size=parameters["UV"]["texture_size"])

        chunk.buildTexture(blending_mode=getattr(Metashape, parameters["texture"]["blending_mode"]),
                           texture_size=parameters["texture"]["size"],
                           fill_holes=parameters["texture"]["fill_holes"],
                           ghosting_filter=parameters["texture"]["ghosting_filter"],
                           transfer_texture=parameters["texture"]["transfer_texture"])

        chunk.exportModel(path=f"{output_path}{os.path.sep}model.obj",
                          binary=parameters["export_model"]["binary"],
                          precision=parameters["export_model"]["precision"],
                          texture_format=getattr(Metashape, parameters["export_model"]["texture_format"]),
                          save_texture=parameters["export_model"]["save_texture"],
                          save_uv=parameters["export_model"]["save_uv"],
                          save_normals=parameters["export_model"]["save_normals"],
                          save_colors=parameters["export_model"]["save_colors"],
                          save_confidence=parameters["export_model"]["save_confidence"],
                          save_cameras=parameters["export_model"]["save_cameras"],
                          save_markers=parameters["export_model"]["save_markers"],
                          save_udim=parameters["export_model"]["save_udim"],
                          save_alpha=parameters["export_model"]["save_alpha"],
                          embed_texture=parameters["export_model"]["embed_texture"],
                          strip_extensions=parameters["export_model"]["strip_extensions"],
                          raster_transform=getattr(Metashape, parameters["export_model"]["raster_transform"]),
                          colors_rgb_8bit=parameters["export_model"]["colors_rgb_8bit"],
                          comment=parameters["export_model"]["colors_rgb_8bit"],
                          save_comment=parameters["export_model"]["exp_comment"],
                          format=getattr(Metashape, parameters["export_model"]["format"]),
                          clip_to_boundary=parameters["export_model"]["clip_to_boundary"])
        doc.save()
