import os
import Metashape
import json
import tkinter as tk
from tkinter import filedialog


def export_report(input_path, output_path):
    """
    Exports a report of the processed dataset.
    :param output_path: Specifies the path of the project.psx file
    """

    parameters = json.load(open(f"{input_path}{os.path.sep}parameters.json", "r"))

    if parameters["export_report"]:

        doc = Metashape.app.document
        doc.open(f"{output_path}{os.path.sep}project.psx")
        chunk = doc.chunk

        doc.read_only = False
        doc.save()
        doc.read_only = False

        chunk.exportReport(f"{output_path}{os.path.sep}report.pdf")
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
            export_report(input_path, output_path)

    elif not os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        export_report(input_path, output_path)
