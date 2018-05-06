#!/usr/bin/env python
# -*-coding: utf-8-*-

""" This module converts a table of link-centric table to an adjacency
    list equivalent.

    To run this module as an independent script, just type:
    > python conversion.py 'input_file' 'output_file'
    i.e
    > python conversion.py ~/my_files/a_file.xls output.csv
"""

import sys
import xlrd
import pdb


class Conversion:
    """ Converts a table to an adjacency list.
    #TODO (Graph url and theory here).
    """

    def __init__(self, src_file=None, dest_file=None):
        """ @param src_file is the file where the raw data is found.
        @param dest_file is the destination file, where the final results
        will be written.
        """
        self.src_file = src_file
        self.dest_file = dest_file
        ## initialize a dictionary which contains all nodes found.
        ## The form of data saved in the dictionary is as follows:
        ##  <   node1; <node3:dist3;node4:dist4>
        ##      node2; <node5:dist5;node6:dist6>    >
        self.nodes_list = {}
        # list of end nodes (with no connections to others)
        self.end_nodes = []
        # read the file and acquire just the appropriate sheet of data
        self.table = self.read_file(self.src_file)
        # and start the table to list conversion
        self.convert_data(self.table, self.nodes_list)
        # find all end nodes
        self.find_end_nodes(self.nodes_list, self.end_nodes, self.table)
        # finally, write the adjacency list to a file
        self.write_to_file(self.dest_file, self.nodes_list)
        self.write_end_nodes_to_file(self.dest_file, self.end_nodes)
        # check for network connectivity
        self.missing = self.is_network_connected(self.nodes_list, self.end_nodes)
        pdb.set_trace()

    def read_file(self, src_file):
        """ This method reads an .xls file and extracts a data sheet.
        @param src_file is the .xls file.
        @return is the data sheet to be returned.
        """
        # open the workbook
        self.workbook = xlrd.open_workbook(src_file)
        # split all sheets by name
        self.worksheets = self.workbook.sheet_names()
        # and acquire the first one
        self.worksheet = self.workbook.sheet_by_name(self.worksheets[0])
        # finally, return the whole worksheet
        return self.worksheet

    def convert_data(self, a_table, a_list):
        """ This method converts a table of info about a graph to an
        adjacency list.
        @param a_table is the table to be converted
        @param a_list is the list which finally contains the adjacency
        list.
        """
        # for each row of the table
        for row_number in range(1, a_table.nrows):
            # acquire all useful data (which is the node from which the
            # link starts, the node to which the link goes as well as
            # the distance between them)
            self.from_node_id, self.to_node_id, self.distance = \
                self.export_data_from_table(a_table.row_values(row_number))
            # and check whether the node already is inside the list of
            # nodes or not.
            #
            # If node is not inside, then create a new node and add it
            # with all its corresponding data (a.k.a. a neighbor node
            # and the the distance between them)
            if self.from_node_id not in a_list:
                a_list[self.from_node_id] = \
                    {self.to_node_id:self.distance}
            # else, just add the neighbor to the list of neighbors of
            # the particular node
            else:
                a_list[self.from_node_id][self.to_node_id] = \
                    self.distance

    def export_data_from_table(self, row):
        """ This method exports useful data from a row of a file
        (an .xls sheet).
        @param row is the row of an .xls sheet
        @return from_node_id is the from_node id
        @return to_node_id is the to_node id
        @return distance is the distance between the two nodes.
        """
        return str(int(row[2])), str(int(row[3])), int(row[10])

    def write_to_file(self, dest, a_list, delimiter=";"):
        """ This method writes a dictionary to a file.
        The form of the file is as following:
        <src_node1; dest_node1:distance1; dest_node2:distance2\n
         src_node2; dest_node3:distance3>
        @param dest is the path where the file is found.
        @param a_list is the adjacency list.
        @param delimiter is separator between different values.
        """
        # open the file
        with open(dest, "a") as f:
            # for each node, assign its key and the list of neighbor
            # nodes
            for key, value in a_list.items():
                # check if the node has neighbors.
                if value:
                    ## if it has neighbors, then they are placed in an
                    ## internal dictionary as <neighbor_id:distance>
                    ## pairs.
                    ## So, iterate the internal dictionary in order to
                    ## obtain al the pairs.
                    ##
                    # Initialize a variable which holds all neighbors
                    # and merges them to a single line.
                    self.all_neighbors = ""
                    for k, v in value.iteritems():
                        # and collect them to a single line separated
                        # by an appropriate delimiter.
                        self.pair = delimiter + str(k) + ":" + str(v)
                        self.all_neighbors += self.pair
                    self.row = key + self.all_neighbors + "\n"
                    f.write(self.row)
                else:
                    self.row = key + value + "\n"
                    f.write(self.row)

    def write_end_nodes_to_file(self, dest, a_list, delimiter=";"):
        """ This method writes a list to a file.
        @param dest is the destination where the data is going to be written.
        @param a_list is the list of nodes.
        @param delimiter is separator between different values.
        """
        # open the file
        with open(dest, "a") as f:
            # for each node in the list
            for node in a_list:
                # write the node followed by the delimiter and a blank line
                self.row = str(node) + delimiter + "\n"
                f.write(self.row)

    def find_end_nodes(self, nodes_list, end_nodes_list, a_table):
        """ This method finds all end nodes (which don't have any
        active connections towards others and it returns it.
        @param nodes_list is the list with the already existed nodes
        inside.
        @param end_nodes_list is the list of end nodes.
        @param a_table is the table with the raw nodes inside.
        """
        # check for to_nodes that do not exist in from_nodes
        for row_number in range(1, a_table.nrows):
            # acquire current row and export the to_node
            self.to_node_id = self.export_to_node\
                (a_table.row_values(row_number))
            # check if to_node exists into the nodes_list
            if self.to_node_id not in nodes_list:
                # if there isn't, then check if this node already is inside
                # the list
                if self.to_node_id not in end_nodes_list:
                    #add it to end_nodes_list
                    end_nodes_list.append(self.to_node_id)

    def export_to_node(self, row):
        """ This method inputs a row of a table and returns the to_node field.
        @param row is the row of the table.
        @return the to_node_id
        """
        return str(int(row[3]))

    def get_adjacency_list(self):
        """ This method returns a list full of node ids and their neighbors
        and a list with the end nodes.
        @return a dictionary full of node ids with <node: <neighbor:cost>
        pairs
        @return a list full of end node ids.
        """
        # be sure that both data structures have been initialized and are
        # full of nodes
        assert self.nodes_list and self.end_nodes, "lists of nodes are empty"
        return self.nodes_list, self.end_nodes

    def is_network_connected(self, list_a, list_b):
        """ This method checks if every single node has at least one neighbor.
        If there is at least one neighbor, then it returns true, else false.
        @param list_a is the list of nodes that have at least one neighbor.
        @param list_b is the list of single nodes.
        @return true for a strongly connected network (graph), false otherwise.
        """
        self.missing_nodes = []
        self.found = -1
        for end_node in list_b:
            for value in list_a.values():
                for node in value.keys():
                    if str(end_node) == str(node):
                        self.found = 1
            if self.found == -1:
                self.missing_nodes.append(end_node)
            self.found = -1
        return self.missing_nodes

    def debug_print(self, data):
        """ This is a small debugging function. It prints its argument,
        whatever it is.
        @param data is the data to be printed.
        """
        print data



def main():
    """ main class here.
    @src is the path of the table it needs to be converted.
    @dest is the path of the file where the list is going to be written.
    """
    src = str(sys.argv[1])
    dest = str(sys.argv[2])
    Conversion(src, dest)

if __name__ == '__main__':
    main()
