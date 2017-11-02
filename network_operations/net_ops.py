""" This module implements basic network operations for an arcgis
network.

Created on June 2017
author: Babis Babalis
"""

import sys
import arcpy
from arcpy import env


class Network_Operations:
    """ This class implements basic network operations.
    """
    def __init__(self, env_path):
        #TODO not sure why this is happening here. try to figure out
        env.workspace = env_path

    def get_point_coordinates():
        """ This method acquires the coordinates of a point in the map.
        """
        pass

    def compute_distance_between(point_a, point_b):
        """ This method computes the distance between two points.
        """
        pass

    def insert_node():
        """ This method inserts a new node in the network.
        """
        pass

    def delete_node():
        """ This method deletes a node from the network.
        """
        pass

    def is_network_robust():
        """ This method checks the continuity of the network.
        :return : True if the network is continuous, False otherwise.
        """
        pass