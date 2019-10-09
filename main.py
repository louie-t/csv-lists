from classes.ListsManager import ListsManager
from classes.ListManager import ListManager

import saved_lists
import saved_data

import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable()

def lists_manager_tester():
    
    
    my_lists = saved_lists.lists
    logging.debug('My lists are {}'.format(my_lists))
    my_data = saved_data.data
    logging.debug('My data is {}'.format(my_data))
    
    my_lists_manager = ListsManager()
    
    while True:
        list_to_view = my_lists_manager.menu(my_lists_manager.get_input())
        while list_to_view != None:
            data = my_lists_manager.my_data[list_to_view]
            temp_list = ListManager()
            result = temp_list.menu(temp_list.get_input(data), data)
            if result == True:
                break
    
lists_manager_tester()


