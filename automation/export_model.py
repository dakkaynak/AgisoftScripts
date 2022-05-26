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

        chunk.buildModel(surface_type=Metashape.Arbitrary,
                         interpolation=Metashape.EnabledInterpolation,
                         face_count=Metashape.CustomFaceCount,
                         face_count_custom=60000000,
                         source_data=Metashape.DepthMapsData,
                         vertex_colors=False, keep_depth=True)

        chunk.buildUV(mapping_mode=Metashape.GenericMapping,
                      page_count=1,
                      texture_size=8192)

        chunk.buildTexture(blending_mode=Metashape.MosaicBlending,
                           texture_size=8192,
                           fill_holes=True,
                           ghosting_filter=True,
                           transfer_texture=True)

        chunk.exportModel(path=f"{output_path}{os.path.sep}model.obj",
                          binary=True,
                          precision=6,
                          texture_format=Metashape.ImageFormatJPEG,
                          save_texture=True,
                          save_uv=True,
                          save_normals=True,
                          save_colors=True,
                          save_confidence=False,
                          save_cameras=True,
                          save_markers=True,
                          save_udim=False,
                          save_alpha=False,
                          embed_texture=False,
                          strip_extensions=False,
                          raster_transform=Metashape.RasterTransformNone,
                          colors_rgb_8bit=True, comment='',
                          save_comment=True,
                          format=Metashape.ModelFormatNone,
                          clip_to_boundary=True)
        doc.save()
