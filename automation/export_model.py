import os
import Metashape
import json
import tkinter as tk
from tkinter import filedialog


def export_model(input_path, output_path):
    """
    Exports a model and texture from the project specified in the output path
    :param output_path: Specifies the path of the project.psx file
    """
    parameters = json.load(open(f"{input_path}{os.path.sep}parameters.json", "r"))

    if parameters["export_model_to_file"]:

        doc = Metashape.app.document
        doc.open(f"{output_path}{os.path.sep}project.psx")
        chunk = doc.chunk

        doc.read_only = False
        doc.save()
        doc.read_only = False


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
            export_model(input_path, output_path)

    elif not os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        export_model(input_path, output_path)
