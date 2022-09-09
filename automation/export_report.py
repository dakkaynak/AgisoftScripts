import os
import Metashape
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from load_parameters import load_parameters


def export_report(input_path, output_path, parameters):
    """
    Exports a report of the processed dataset.
    :param output_path: Specifies the path of the project.psx file
    """

    if parameters.iloc[0]["export_report"]:
        doc = Metashape.Document()
        doc.open(os.path.join(input_path, os.pardir, 'photogrammetry', 'project.psx'))
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
            export_report(input_path, output_path, parameters)

    elif not os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        export_report(input_path, output_path, parameters)
