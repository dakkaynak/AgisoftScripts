import os
import Metashape
import json
import tkinter as tk
from tkinter import filedialog


def export_dense_cloud(input_path, output_path):
    """
    Exports dense cloud from the Metashape project specified in the output path.
    :param output_path: Specifies the path of the project.psx file
    """
    parameters = json.load(open(f"{input_path}{os.path.sep}parameters.json", "r"))

    if parameters["export_dense_cloud_to_file"]:

        doc = Metashape.app.document
        doc.open(f"{output_path}{os.path.sep}project.psx")
        chunk = doc.chunk

        doc.read_only = False
        doc.save()
        doc.read_only = False

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
            export_dense_cloud(input_path, output_path)

    elif not os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        export_dense_cloud(input_path, output_path)
