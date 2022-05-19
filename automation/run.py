
import Metashape
import os
import tkinter as tk

from tkinter import filedialog
from align_cameras import align_cameras_depth_maps
from export_dense_cloud import export_dense_cloud
from export_depth_maps import export_depth_maps
from export_model import export_model
from import_masks import import_masks


def find_files(folder, types):
    return [entry.path for entry in os.scandir(folder) if (entry.is_file() and os.path.splitext(entry.name)[1].lower() in types)]


root = tk.Tk()
root.withdraw()

# doc = Metashape.Document()
# chunk = doc.addChunk()

# Opens dialog window to specify input and output folder
print("Please select input folder containing images.")
input_path = filedialog.askdirectory()
root.title('Select input folder')

output_path = f"{input_path}{os.path.sep}output"


# Checks whether set of images has already been processed
if os.path.exists(f"{output_path}{os.path.sep}project.psx"):
    msg_box = tk.messagebox.askokcancel(title="Warning", message="The dataset you specified has already been processed. If you proceed, previous files will be deleted.")
    if msg_box == 0:
        print("Please select a different set of images.")
    
    else:
        import_masks(output_path)
        align_cameras_depth_maps(input_path, output_path)
        export_dense_cloud(output_path)
        export_model(output_path)
        export_depth_maps(output_path)


else:
    import_masks(output_path)
    align_cameras_depth_maps(input_path, output_path)
    export_dense_cloud(output_path)
    export_model(output_path)
    export_depth_maps(output_path)



