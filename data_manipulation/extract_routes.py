""" This module reads several files (xls format),
extracts only the useful information and
writes it to a .csv file.

In particular, two scenarios are being examined. Given a file of GPS points:
    - extract all data relevant to specific routes (i.e. Attiki Odos +/-1 stop)
    - extract all routes a truck has been done.

    To run this module as an independent script, type:
    > python extract_routes.py ~/my_folder output.csv
"""


import pdb
import xlrd
import os
import sys

class Extraction:
    """ Extracts data from several files to a new one.
    """

    def __init__(self, src_folder, dest_file):
        self.file_contents = []
        # read the file
        self.read_folder(src_folder)
        # process data
        self.process_file()
        # and write data to a new file
        self.write_output(dest_file)

    def read_folder(self, folder=""):
        """ This method reads a folder which contains files as input.

        :param str folder: is the folder where the function looks
        for files recursively
        """
        # search recursively the system
        for root, dirs, files in os.walk(folder):
            for f in files:
                if f.endswith(".xls"):
                    # read the xls file
                    xls_file = os.path.join(root, f)
                    self._read_xls(xls_file)

    def _read_xls(self, xls_file):
        """ This method reads a single xls file."""
        # open the workbook
        workbook = xlrd.open_workbook(xls_file)
        # split all sheets by name
        worksheets = workbook.sheet_names()
        # acquire the first one
        worksheet = workbook.sheet_by_name(worksheets[0])
        # and append it to the list of files
        self.file_contents.append(worksheet)

    def process_file(self):
        """ This method processes a file and extracts only the data
        the user is interested for.
        """
        pass

    def write_output(self, write_filename=""):
        """ This method writes the contents to a new file.

        :param str write_filename: the filename of the file to
        be written.
        """
        pass
