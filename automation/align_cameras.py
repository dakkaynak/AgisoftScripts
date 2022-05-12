from logging import warning
from pickle import FALSE, TRUE
import tkinter
import Metashape
import os, sys, time
import tkinter as tk
from tkinter import filedialog
#from parameters import *


def find_files(folder, types):
    return [entry.path for entry in os.scandir(folder) if (entry.is_file() and os.path.splitext(entry.name)[1].lower() in types)]


root = tkinter.Tk()

# closes window that opens in background
root.withdraw()
# opens dialog window to specify input and output folder
print("Please select input folder containing images.")
input_path = filedialog.askdirectory()
root.title('Select input folder')


# creates an output folder within input folder
output_path = input_path + os.path.sep + "output"

# root = tk.Tk()
# # closes window that opens in background
# root.withdraw()
# print("Please select output folder.")
# output_path = filedialog.askopenfilenames()
# root.title('Select output folder')

#print(parameters.keypoint_limit, parameters.tiepoint_limit, parameters.generic_preselection, parameters.reference_preselection_bool)


# checks whether path already exists and warns if it does
if os.path.exists(output_path):
    msg_box = tkinter.messagebox.askokcancel(title="Warning", message="The dataset you specified has already been processed. If you proceed, previous files will be deleted.")
    if  msg_box == 0:
        print("closing")
        sys.exit()
    else:
        pass

else:
    pass
# specifies file extensions that are allowed as input
images = find_files(input_path, [".jpg", ".jpeg", ".tif", ".tiff"])

# creates a new document in Metashape
doc = Metashape.Document()

# prevents opening without writing permissions and saves project
doc.read_only = False
doc.save(output_path + '/project.psx')
doc.read_only = False
      
# adds chunk to project
chunk = doc.addChunk()

# imports cameras into chunk and saves project
chunk.addPhotos(images)
doc.save()

# prints the amount of loaded images in console
print(str(len(chunk.cameras)) + " images loaded")

# help_reference_preselection = 'reference_preselection =' + reference_preselection_bool

# finds key features in importet cameras
chunk.matchPhotos(keypoint_limit = 40000, tiepoint_limit = 10000, generic_preselection = True, reference_preselection = True)
doc.save()

# aligns cameras 
chunk.alignCameras()
doc.save()

chunk.buildDepthMaps(filter_mode = Metashape.MildFiltering)
doc.save()
