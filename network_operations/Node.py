""" This is a structure representing a Node.  """

class Node:
    """ Doc here  """
    def __init__(self, id=None, name=None, link_ids=[], trans=[], info):
        self.id = id
        self.name = name
        self.link_ids = link_ids
        self.trans = trans
        self.additional_fields = self.create_fields_from_info(info)

    def is_node_valid(self):
        """ Checks the integrity of the node. """
        if not self.id or not self.name:
            return False
        else return True
        return False

    def create_fields_from_info(self, info):
        """ This method creates additional fields from info given to the node
        dynamically
        @param: info: the info
        """
        list_of_fields = []
        if not info:
            return list_of_fields
        # iterate the info list
        for item in info:
            # add the fields to a new list
            list_of_fields.add(item)
        # and return it.
        return list_of_fields



