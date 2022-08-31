import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path
from PIL import Image

IMAGE_SUFFIX = [".jpg", ".jpeg", ".tif", ".tiff", ".dng", ".DNG", ".png"]


def generate_white_masks(input_path):
    """
    Checks whether there is a mask for every image and generates white masks to avoid error messages in Agisoft.
    :param output_path: Specifies the path of the project.psx file
    """
    masks_path = f"{input_path}{os.path.sep}masks{os.path.sep}"
    dataset_path = f"{input_path}{os.path.sep}"

    dataset_images = filenames_in_folder(input_path)
    existing_masks = filenames_in_folder(masks_path)

    missing_masks = list(set(dataset_images).difference(set(existing_masks)))

    input_path = Path(input_path)

    for path in input_path.iterdir():
        if path.suffix in IMAGE_SUFFIX:
            with Image.open(path) as im:
                shape = im.size
                break

    width, height = shape[0], shape[1]
    white_mask = Image.new('RGB', (width, height), (255, 255, 255))

    for mask_name in missing_masks:
        white_mask.save(f"{masks_path}{mask_name}.jpg")


def filenames_in_folder(input_path):
    """

    :param input_path: path str
    :return: list of files names within the input path folder
    """

    input_path = Path(input_path)
    file_names = []
    for path in input_path.iterdir():
        if path.suffix in IMAGE_SUFFIX:
            file_names.append(path.stem)

    return file_names


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
            generate_white_masks(input_path, output_path)

    elif not os.path.exists(f"{output_path}{os.path.sep}project.psx"):
        generate_white_masks(input_path, output_path)
