import os
import Metashape
import json


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