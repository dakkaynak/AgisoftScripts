import os
import Metashape
import json
from import_masks import import_masks


def find_files(folder, types):
    """
    Generates a list of files of a specific file type in a folder
    :param folder: Folder from which
    :param types: Desired filetypes
    :return: Returns list of specified filetypes in specified folder
    """
    return [entry.path for entry in os.scandir(folder) if (entry.is_file() and os.path.splitext(entry.name)[1].lower() in types)]


def align_cameras_depth_maps(input_path, output_path):
    """
    Creates a new Chunk in a new Metashape document and aligns imported cameras.
    :param input_path: Folder from which images will be imported
    :param output_path: folder where project files and exported files will be stored
    """

    parameters = json.load(open(f"{input_path}{os.path.sep}parameters.json", "r"))

    images = find_files(input_path, [".jpg", ".jpeg", ".tif", ".tiff"])

    doc = Metashape.Document()

    doc.read_only = False
    doc.save(f"{output_path}{os.path.sep}project.psx")
    doc.read_only = False

    chunk = doc.addChunk()

    chunk.addPhotos(images)
    doc.save()

    print(str(len(chunk.cameras)) + " images loaded")

    import_masks(input_path, output_path)

    chunk.matchPhotos(keypoint_limit=parameters["matching"]["keypoint_limit"],
                      tiepoint_limit=parameters["matching"]["tiepoint_limit"],
                      generic_preselection=parameters["matching"]["generic_preselection"],
                      reference_preselection=parameters["matching"]["reference_preselection"])
    doc.save()

    chunk.alignCameras(min_image=parameters["alignment"]["min_image"],
                       adaptive_fitting=parameters["alignment"]["adaptive_fitting"],
                       reset_alignment=parameters["alignment"]["reset_alignment"],
                       subdivide_task=parameters["alignment"]["subdivide_task"])
    doc.save()

    chunk.buildDepthMaps(downscale=parameters["alignment"]["downscale"],
                         filter_mode=getattr(Metashape, parameters["alignment"]["filter_mode"]),
                         reuse_depth=parameters["alignment"]["reuse_depth"],
                         max_neighbors=parameters["alignment"]["max_neighbors"],
                         subdivide_task=parameters["alignment"]["subdivide_task"],
                         workitem_size_cameras=parameters["alignment"]["workitem_size_cameras"],
                         max_workgroup_size=parameters["alignment"]["max_workgroup_size"])
    doc.save()
