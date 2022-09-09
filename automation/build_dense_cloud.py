import os
import Metashape
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from load_parameters import load_parameters


def build_dense_cloud(input_path, output_path, parameters):
    """
    Exports dense cloud from the Metashape project specified in the output path.
    :param output_path: Specifies the path of the project.psx file
    """

    if parameters.iloc[0]["build_dense_cloud"]:

        doc = Metashape.Document()
        doc.open(os.path.join(input_path, os.pardir, 'photogrammetry', 'project.psx'))
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

        chunk.buildDenseCloud(point_colors=True,
                              point_confidence=parameters.iloc[0]["dense_cloud/point_confidence"],
                              keep_depth=parameters.iloc[0]["dense_cloud/keep_depth"],
                              max_neighbors=parameters.iloc[0]["dense_cloud/max_neighbors"],
                              subdivide_task=parameters.iloc[0]["dense_cloud/subdivide_task"],
                              workitem_size_cameras=parameters.iloc[0]["dense_cloud/workitem_size_cameras"],
                              max_workgroup_size=parameters.iloc[0]["dense_cloud/max_workgroup_size"]
                              )
        doc.save()

        chunk.colorizeDenseCloud(source_data=Metashape.ImagesData)
        doc.save()

    #doc.save()

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
            build_dense_cloud(input_path, output_path, parameters)

    elif not os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        build_dense_cloud(input_path, output_path, parameters)
