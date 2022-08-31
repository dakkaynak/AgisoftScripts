import os
import Metashape
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from load_parameters import load_parameters


def build_model(input_path, output_path, parameters):
    """
    builds a model and texture from the project specified in the output path
    :param output_path: Specifies the path of the project.psx file
    """

    if parameters.iloc[0]["build_model"]:

        doc = Metashape.Document()
        doc.open(f"{output_path}{os.path.sep}project.psx")
        chunk = doc.chunk

        doc.read_only = False
        doc.save()
        doc.read_only = False

        f = Metashape.PointCloud.Filter()

        if parameters.iloc[0]["filtering/reprojection_error"]:
            f.init(chunk, criterion=Metashape.PointCloud.Filter.ReprojectionError)
            f.removePoints(parameters.iloc[0]["filtering/threshold_reprojection_error"])

        if parameters.iloc[0]["filtering/reconstruction_uncertainty"]:
            f.init(chunk, criterion=Metashape.PointCloud.Filter.ReconstructionUncertainty)
            f.removePoints(parameters.iloc[0]["filtering/threshold_reconstruction_uncertainty"])

        if parameters.iloc[0]["filtering/image_count"]:
            f.init(chunk, criterion=Metashape.PointCloud.Filter.ImageCount)
            f.removePoints(parameters.iloc[0]["filtering/threshold_image_count"])

        if parameters.iloc[0]["filtering/reprojection_accuracy"]:
            f.init(chunk, criterion=Metashape.PointCloud.Filter.ProjectionAccuracy)
            f.removePoints(parameters.iloc[0]["filtering/threshold_projection_accuracy"])

        chunk.buildModel(surface_type=getattr(Metashape, parameters.iloc[0]["model/surface_type"]),
                         interpolation=getattr(Metashape, parameters.iloc[0]["model/interpolation"]),
                         face_count=getattr(Metashape, parameters.iloc[0]["model/face_count"]),
                         face_count_custom=parameters.iloc[0]["model/face_count_custom"],
                         source_data=getattr(Metashape, parameters.iloc[0]["model/source_data"]),
                         vertex_colors=parameters.iloc[0]["model/vertex_colors"],
                         keep_depth=parameters.iloc[0]["model/keep_depth"])
        doc.save()

        chunk.buildUV(mapping_mode=getattr(Metashape, parameters.iloc[0]["UV/mapping_mode"]),
                      page_count=parameters.iloc[0]["UV/page_count"],
                      texture_size=parameters.iloc[0]["UV/texture_size"])

        chunk.buildTexture(blending_mode=getattr(Metashape, parameters.iloc[0]["texture/blending_mode"]),
                           texture_size=parameters.iloc[0]["texture/size"],
                           fill_holes=parameters.iloc[0]["texture/fill_holes"],
                           ghosting_filter=parameters.iloc[0]["texture/ghosting_filter"],
                           transfer_texture=parameters.iloc[0]["texture/transfer_texture"])
        doc.save()


if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    # Opens dialog window to specify input and output folder
    print("Please select input folder containing images.")
    input_path = filedialog.askdirectory()
    root.title('Select input folder')
    output_path = f"{input_path}{os.path.sep}output"

    parameters = load_parameters(input_path)

    # Checks whether set of images has already been processed
    if os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        msg_box = tk.messagebox.askokcancel(title="Warning",
                                            message="The dataset you specified has already been processed."
                                                    " If you proceed, previous files will be deleted.")
        if msg_box == 0:
            print("Please select a different set of images.")

        elif msg_box == 1:
            build_model(input_path, output_path, parameters)

    elif not os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        build_model(input_path, output_path, parameters)
