import saved_lists
import saved_data

from classes.ListCollection import ListCollection
from classes.ListManager import ListManager

import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(level=logging.DEBUG)

def main():
    my_lists = saved_lists.lists
    logging.debug('My lists are {}'.format(my_lists))
    my_data = saved_data.data
    logging.debug('My data is {}'.format(my_data))
    
    my_list_collection = ListCollection()
    
    while True:
        list_to_view = my_list_collection.menu(my_list_collection.get_input())
        while list_to_view != None:
            data = my_list_collection.my_data[list_to_view]
            temp_list = ListManager()
            result = temp_list.menu(temp_list.get_input(data), data)
            if result == True:
                break
    
main()


