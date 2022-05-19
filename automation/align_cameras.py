import os
import Metashape


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
    images = find_files(input_path, [".jpg", ".jpeg", ".tif", ".tiff"])

    doc = Metashape.Document()

    doc.read_only = False
    doc.save(f"{output_path}{os.path.sep}project.psx")
    doc.read_only = False

    chunk = doc.addChunk()

    chunk.addPhotos(images)
    doc.save()

    print(str(len(chunk.cameras)) + " images loaded")

    chunk.matchPhotos(keypoint_limit=40000, tiepoint_limit=10000, generic_preselection=True, reference_preselection=True)
    doc.save()

    chunk.alignCameras(min_image=2, adaptive_fitting=False, reset_alignment=False, subdivide_task=True)
    doc.save()

    chunk.buildDepthMaps(downscale=4, filter_mode=Metashape.MildFiltering, reuse_depth=False, max_neighbors=16, subdivide_task=True, workitem_size_cameras=20, max_workgroup_size=100)
    doc.save()
