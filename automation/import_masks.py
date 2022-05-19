import os
import Metashape


def import_masks(output_path):
    """
    Imports masks to mask areas not relevant to the model. Folder "masks" needs to be located within image directory.
    :param output_path: Specifies the path of the project.psx file
    """

    doc = Metashape.app.document
    doc.open(f"{output_path}{os.path.sep}project.psx")
    chunk = doc.chunk

    doc.read_only = False
    doc.save()
    doc.read_only = False

    if os.path.exists(f"{output_path}{os.path.sep}masks"):
        pass
    else:
        os.mkdir(f"{output_path}{os.path.sep}masks")

    for camera in chunk.cameras:
        chunk.generateMasks(path=f"{output_path}{os.path.sep}masks{os.path.sep}{camera.label}.png", masking_mode=Metashape.MaskingModeAlpha, mask_operation=Metashape.MaskOperationReplacement, tolerance=10, mask_defocus=False, fix_coverage=True, blur_threshold=3, depth_threshold=3.40282e+38)

    doc.save()