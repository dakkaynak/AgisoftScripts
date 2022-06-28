import os
import Metashape
import json
import tkinter as tk
from tkinter import filedialog
import ast


def export_normal_maps(input_path, output_path):
    """
    Exports normal maps from the project specified in the output path
    :param output_path: Specifies the path of the project.psx file
    """
    parameters = json.load(open(f"{input_path}{os.path.sep}parameters.json", "r"))

    if parameters["export_normal_maps"]:
        doc = Metashape.app.document
        doc.open(f"{output_path}{os.path.sep}project.psx")
        chunk = doc.chunk

        doc.read_only = False
        doc.save()
        doc.read_only = False

        if not chunk.model:

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

        if chunk.transform.scale is None:
            scale = 1
            print("Scale set to 1")
        else:
            scale = chunk.transform.scale

        if os.path.exists(f"{output_path}{os.path.sep}normal_maps"):
            pass
        else:
            os.mkdir(f"{output_path}{os.path.sep}normal_maps")

        for camera in chunk.cameras:
            if camera.transform:
                depth = chunk.model.renderNormalMap(camera.transform, camera.sensor.calibration)
                depth = depth * scale
                depth = depth.convert(" ", "F16")
                compr = Metashape.ImageCompression()
                compr.tiff_compression = Metashape.ImageCompression().TiffCompressionDeflate
                depth.save(f"{output_path}{os.path.sep}normal_maps{os.path.sep}{camera.label}.tif")
                print(f"Normal map for {camera.label} exported successfully!")

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
            export_normal_maps(input_path, output_path)

    elif not os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        export_normal_maps(input_path, output_path)
