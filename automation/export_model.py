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

        if parameters["filtering_reprojection_error"]:
            chunk = Metashape.app.document.chunk
            f = Metashape.PointCloud.Filter()
            f.init(chunk, criterion=Metashape.PointCloud.Filter.ReprojectionError)
            f.selectPoints(parameters["filter_threshold_reprojection_error"])

        if parameters["filtering_reconstruction_uncertainty"]:
            chunk = Metashape.app.document.chunk
            f = Metashape.PointCloud.Filter()
            f.init(chunk, criterion=Metashape.PointCloud.Filter.ReconstructionUncertainty)
            f.selectPoints(parameters["filter_threshold_reconstruction_uncertainty"])

        if parameters["filtering_image_count"]:
            chunk = Metashape.app.document.chunk
            f = Metashape.PointCloud.Filter()
            f.init(chunk, criterion=Metashape.PointCloud.Filter.ImageCount)
            f.selectPoints(parameters["filter_threshold_image_count"])

        if parameters["filtering_reprojection_error"]:
            chunk = Metashape.app.document.chunk
            f = Metashape.PointCloud.Filter()
            f.init(chunk, criterion=Metashape.PointCloud.Filter.ProjectionAccuracy)
            f.selectPoints(parameters["filter_threshold_projection_accuracy"])

        chunk.buildModel(surface_type=Metashape.Arbitrary,
                         interpolation=Metashape.EnabledInterpolation,
                         face_count=Metashape.CustomFaceCount,
                         face_count_custom=parameters["model_face_count_custom"],
                         source_data=Metashape.DepthMapsData,
                         vertex_colors=parameters["model_vertex_colors"],
                         keep_depth=parameters["keep_depth"])

        chunk.buildUV(mapping_mode=Metashape.GenericMapping,
                      page_count=parameters["UV_page_count"],
                      texture_size=parameters["UV_texture_size"])

        chunk.buildTexture(blending_mode=Metashape.MosaicBlending,
                           texture_size=parameters["texture_size"],
                           fill_holes=parameters["texture_fill_holes"],
                           ghosting_filter=parameters["texture_ghosting_filter"],
                           transfer_texture=parameters["texture_transfer_texture"])

        chunk.exportModel(path=f"{output_path}{os.path.sep}model.obj",
                          binary=parameters["exp_model_binary"],
                          precision=parameters["exp_model_precision"],
                          texture_format=Metashape.ImageFormatJPEG,
                          save_texture=parameters["exp_model_save_texture"],
                          save_uv=parameters["exp_model_save_uv"],
                          save_normals=parameters["exp_model_save_normals"],
                          save_colors=parameters["exp_model_save_colors"],
                          save_confidence=parameters["exp_model_save_confidence"],
                          save_cameras=parameters["exp_model_save_cameras"],
                          save_markers=parameters["exp_model_save_markers"],
                          save_udim=parameters["exp_model_save_udim"],
                          save_alpha=parameters["exp_model_save_alpha"],
                          embed_texture=parameters["exp_model_embed_texture"],
                          strip_extensions=parameters["exp_model_strip_extensions"],
                          raster_transform=Metashape.RasterTransformNone,
                          colors_rgb_8bit=parameters["exp_model_colors_rgb_8bit"],
                          comment=parameters["exp_model_colors_rgb_8bit"],
                          save_comment=parameters["exp_comment"],
                          format=Metashape.ModelFormatNone,
                          clip_to_boundary=parameters["exp_model_clip_to_boundary"])
        doc.save()
