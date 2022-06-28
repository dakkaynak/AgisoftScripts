import os
import Metashape
import tkinter as tk
from tkinter import filedialog
from os import listdir
from os.path import isfile, join


def import_masks(input_path, output_path):
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

    if os.path.exists(f"{input_path}{os.path.sep}masks"):
        pass
    else:
            os.mkdir(f"{input_path}{os.path.sep}masks")

    #camera_list =
            #if os.path.exists(f"{input_path}{os.path.sep}masks{os.path.sep}{camera.label}.jpg"):



    chunk.generateMasks(path=f"{input_path}{os.path.sep}masks{os.path.sep}"+"{filename}.jpg",
                        masking_mode=Metashape.MaskingMode.MaskingModeFile,
                        cameras=chunk.cameras)

    doc.save()

if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    # Opens dialog window to specify input and output folder
    print("Please select input folder containing images.")
    input_path = filedialog.askdirectory()
    root.title('Select input folder')
    output_path = f"{input_path}{os.path.sep}output"

    # Checks whether set of images has already been processed
    if os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        msg_box = tk.messagebox.askokcancel(title="Warning",
                                            message="The dataset you specified has already been processed."
                                                    " If you proceed, previous files will be deleted.")
        if msg_box == 0:
            print("Please select a different set of images.")

        elif msg_box == 1:
            import_masks(input_path, output_path)

    elif not os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        import_masks(input_path, output_path)

        