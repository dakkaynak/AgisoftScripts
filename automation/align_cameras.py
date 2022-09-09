import os
import Metashape
from load_parameters import load_parameters
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def find_files(folder, types):
    """
    Generates a list of files of a specific file type in a folder
    :param folder: Folder from which
    :param types: Desired filetypes
    :return: Returns list of specified filetypes in specified folder
    """
    return [entry.path for entry in os.scandir(folder) if (entry.is_file() and os.path.splitext(entry.name)[1].lower() in types)]


def align_cameras(input_path, parameters):
    """
    Creates a new Chunk in a new Metashape document and aligns imported cameras.
    :param input_path: Folder from which images will be imported
    :param output_path: folder where project files and exported files will be stored
    """

    print(parameters["matching/keypoint_limit"])

    images = find_files(input_path, [".jpg", ".jpeg", ".tif", ".tiff", ".dng", ".DNG"])

    doc = Metashape.Document()

    doc.read_only = False
    doc.save(os.path.join(input_path, os.pardir, 'photogrammetry', 'project.psx'))
    doc.read_only = False

    chunk = doc.addChunk()

    chunk.addPhotos(images)
    doc.save()

    print(str(len(chunk.cameras)) + " images loaded")

    chunk.matchPhotos(keypoint_limit=parameters.iloc[0]['matching/keypoint_limit'],
                      tiepoint_limit=parameters.iloc[0]["matching/tiepoint_limit"],
                      generic_preselection=parameters.iloc[0]["matching/generic_preselection"],
                      reference_preselection=parameters.iloc[0]["matching/reference_preselection"])
    doc.save()

    chunk.alignCameras(min_image=parameters.iloc[0]["alignment/min_image"],
                       adaptive_fitting=parameters.iloc[0]["alignment/adaptive_fitting"],
                       reset_alignment=parameters.iloc[0]["alignment/reset_alignment"],
                       subdivide_task=parameters.iloc[0]["alignment/subdivide_task"])
    doc.save()

    chunk.buildDepthMaps(downscale=parameters.iloc[0]["alignment/downscale"],
                         filter_mode=getattr(Metashape, parameters.iloc[0]["alignment/filter_mode"]),
                         reuse_depth=parameters.iloc[0]["alignment/reuse_depth"],
                         max_neighbors=parameters.iloc[0]["alignment/max_neighbors"],
                         subdivide_task=parameters.iloc[0]["alignment/subdivide_task"],
                         workitem_size_cameras=parameters.iloc[0]["alignment/workitem_size_cameras"],
                         max_workgroup_size=parameters.iloc[0]["alignment/max_workgroup_size"])
    doc.save()


if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    # Opens dialog window to specify input and output folder
    print("Please select input folder containing images.")
    input_path = filedialog.askdirectory()
    root.title('Select input folder')
    output_path = os.path.join(input_path, os.pardir, 'photogrammetry')
    parameters = load_parameters(os.path.join(input_path, os.pardir, 'parameters'))

    # Checks whether set of images has already been processed
    if os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        msg_box = tk.messagebox.askokcancel(title="Warning",
                                            message="The dataset you specified has already been processed."
                                                    " If you proceed, previous files will be deleted.")
        if msg_box == 0:
            print("Please select a different set of images.")

        elif msg_box == 1:
            align_cameras(input_path, output_path, parameters)

    elif not os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        align_cameras(input_path, output_path, parameters)
