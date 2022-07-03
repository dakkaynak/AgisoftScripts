import os
import Metashape
import json
import tkinter as tk
from tkinter import filedialog


def build_model(input_path, output_path):
    """
    builds a model and texture from the project specified in the output path
    :param output_path: Specifies the path of the project.psx file
    """
    parameters = json.load(open(f"{input_path}{os.path.sep}parameters.json", "r"))

    if parameters["build_model"]:

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
            build_model(input_path, output_path)

    elif not os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        build_model(input_path, output_path)
