import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from load_parameters import load_parameters

def preprocessing(input_path):
    repository_path = f"'D:\Piet\Repsitories\derya-piet-test'"
    input_path_add_quot = f"'{input_path}'"
    os.system(f"cd C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MATLAB R2021b")
    os.system(f'matlab.exe -nosplash -nodesktop -r "cd({repository_path}), preprocessing({input_path_add_quot}), exit"')
#               matlab.exe -nosplash -nodesktop -r "cd('D:\Piet\Repsitories\derya-piet-test'), preprocessing('D:\testsetDNG_SDK\raw'), exit"


if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    # Opens dialog window to specify input and output folder
    print("Please select input folder containing images.")
    input_path = filedialog.askdirectory()
    root.title('Select input folder')
    output_path = os.path.join(input_path, os.pardir, 'photogrammetry')
    # parameters = load_parameters(os.path.join(input_path, os.pardir, 'parameters'))

    # Checks whether set of images has already been processed
    if not os.path.exists(f"{output_path}"):
        os.mkdir(f"{output_path}")

    else:
        pass

    if os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        msg_box = tk.messagebox.askokcancel(title="Warning",
                                            message="The dataset you specified has already been processed."
                                                    " If you proceed, previous files will be deleted.")
        if msg_box == 0:
            print("Please select a different set of images.")

        elif msg_box == 1:
            preprocessing(input_path)

    elif not os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        preprocessing(input_path)