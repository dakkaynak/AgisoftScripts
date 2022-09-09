import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')


def load_parameters(input_path):

    parameters_excel = pandas.read_excel(f"{input_path}{os.path.sep}parameters.xlsx",
                                         sheet_name='parameters',
                                         true_values=["true"],
                                         false_values=["false"])

    print(parameters_excel)

    return parameters_excel


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
            load_parameters(os.path.join(input_path, os.pardir, 'parameters'))

    elif not os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        load_parameters(os.path.join(input_path, os.pardir, 'parameters'))
