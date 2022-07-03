import os
import Metashape
import json
import tkinter as tk
from tkinter import filedialog

def build_dense_cloud(input_path, output_path):
    """
    Exports dense cloud from the Metashape project specified in the output path.
    :param output_path: Specifies the path of the project.psx file
    """
    parameters = json.load(open(f"{input_path}{os.path.sep}parameters.json", "r"))

    if parameters["build_dense_cloud"]:

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

        chunk.buildDenseCloud(point_colors=True,
                              point_confidence=parameters["dense_cloud"]["point_confidence"],
                              keep_depth=parameters["dense_cloud"]["keep_depth"],
                              max_neighbors=parameters["dense_cloud"]["max_neighbors"],
                              subdivide_task=parameters["dense_cloud"]["subdivide_task"],
                              workitem_size_cameras=parameters["dense_cloud"]["workitem_size_cameras"],
                              max_workgroup_size=parameters["dense_cloud"]["max_workgroup_size"]
                              )
        doc.save()

        chunk.colorizeDenseCloud(source_data=Metashape.ImagesData)
        doc.save()


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
            build_dense_cloud(input_path, output_path)

    elif not os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        build_dense_cloud(input_path, output_path)
