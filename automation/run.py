
import Metashape
import os
from align_cameras import align_cameras_depth_maps
from export_dense_cloud import export_dense_cloud
from export_depth_maps import export_depth_maps
from export_model import export_model
from export_normal_maps import export_normal_maps
from export_report import export_report



def find_files(folder, types):
    return [entry.path for entry in os.scandir(folder) if (entry.is_file() and os.path.splitext(entry.name)[1].lower() in types)]


def processing(input_path, output_path):

    align_cameras_depth_maps(input_path, output_path)
    export_dense_cloud(input_path, output_path)
    export_model(input_path, output_path)
    export_depth_maps(input_path, output_path)
    export_normal_maps(input_path, output_path)
    export_report(input_path, output_path)




print("Please select input folder containing images.")
input_path = f"D:\Piet\Material\D3\contrastStretchedJpg"
output_path = f"{input_path}{os.path.sep}output"

processing(input_path, output_path)

