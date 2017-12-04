""" This module reads several files (xls format),
extracts only the useful information and
writes it to a .csv file.

In particular, two scenarios are being examined. Given a file of GPS points:
    - extract all data relevant to specific routes (i.e. Attiki Odos +/-1 stop)
    - extract all routes a truck has been done.
"""


import pdb
import xlrd
import sys

class Extraction:
    """ Extracts data from several files to a new one.
    """

    def __init__(self, ):
        self.file_contents = ""
        pass

    def read_folder(self, folder=""):
        """ This method reads a folder which contains files as input.

        :param str folder: is the folder where the function looks
        for files recursively
        """
        pass

    def process_file(self, filename=""):
        """ This method processes a file and extracts only the data
        the user is interested for.

        :param str filename: is the name of the file.
        """
        pass

    def write_output(self, write_filename=""):
        """ This method writes the contents to a new file.

        :param str write_filename: the filename of the file to
        be written.
        """
        pass""
