
import Metashape
import os
import tkinter as tk

from tkinter import filedialog
from align_cameras import align_cameras_depth_maps
from export_dense_cloud import export_dense_cloud
from export_depth_maps import export_depth_maps
from export_model import export_model
from export_normal_maps import export_normal_maps
from export_report import export_report

from import_masks import import_masks

root = tk.Tk()
root.withdraw()


def find_files(folder, types):
    return [entry.path for entry in os.scandir(folder) if (entry.is_file() and os.path.splitext(entry.name)[1].lower() in types)]


def processing(input_path, output_path):

    align_cameras_depth_maps(input_path, output_path)
    export_dense_cloud(input_path, output_path)
    export_model(input_path, output_path)
    export_depth_maps(input_path, output_path)
    export_normal_maps(input_path, output_path)
    export_report(input_path, output_path)


# Opens dialog window to specify input and output folder
print("Please select input folder containing images.")
input_path = filedialog.askdirectory()
root.title('Select input folder')
output_path = f"{input_path}{os.path.sep}output"


# Checks whether set of images has already been processed
if os.path.exists(f"{output_path}{os.path.sep}project.psx"):
    msg_box = tk.messagebox.askokcancel(title="Warning", message="The dataset you specified has already been processed."
                                                                 " If you proceed, previous files will be deleted.")
    if msg_box == 0:
        print("Please select a different set of images.")
    
    elif msg_box == 1:
        processing(input_path, output_path)

elif not os.path.exists(f"{output_path}{os.path.sep}project.psx"):
    processing(input_path, output_path)
