import pprint
import sys
import shutil
pp = pprint.PrettyPrinter(indent=4,width=80)

import saved_lists
import saved_data
from classes.ListManager import ListManager

import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable()

class ListsManager:
    lists_path = 'saved_lists.py'
    data_path = 'saved_data.py'
    
    my_lists = saved_lists.lists
    my_data = saved_data.data

    def __init__(self):
        logging.debug('Lists manager constructor call.')
        
        self.my_lists = saved_lists.lists
        self.my_data = saved_data.data
            
    # This list contains a list of all of the list objects, of type "ListManager"
    
    def validate_string(self,value):
        logging.debug('Validating string')
        for i in value:
            if i.isalpha():
                return True
            if i.isnum():
                return True
        return False

    def get_list_data(self):
        logging.debug('Get list data call.')
        while True:
            value = input("\nEnter the name for the list.\n")
            if self.validate_string(value):
                list_name = value.title()
                value = value.lower()
                temp = value.split(' ')
                file_name = '_'.join(temp)
                file_name = file_name + '.csv'
                list_path = '.\\lists\\' + file_name
                break
            
        num_categories = 0
        categories = list()
        
        while True:
            print("\nEnter the category number {}. Enter nothing to finish.\n".format(num_categories + 1))
            category = input()
            if category == "":
                break
            else:
                category = category.title()
                categories.append(category)
                num_categories += 1
        
        data_list = [list_name, list_path, num_categories, categories]
        return data_list
        
    def create_list(self, data_list):
        logging.debug('Creating list')
        
        file = open(data_list[1], 'w')
        file.close()
        
        self.my_data.append(data_list)
        file = open(self.data_path, 'w')
        file.write('data = ' + pprint.pformat(self.my_data) + '\n')
        file.close()

        self.my_lists.append(data_list[0])
        file = open(self.lists_path, 'w')
        file.write('lists = ' + pprint.pformat(self.my_lists) + '\n')
        file.close()
        
        my_list = ListManager()
        my_list.add_item(data_list[3], data_list)
        
    def get_list_name(self):
        list_name = input("\nWhat is the list name? Type quit to quit.\n")
        if self.validate_string(list_name):
            list_name = list_name.title()
            return list_name
                
    def remove_list(self, list_name):
        while True:
            if list_name == "Quit":
                break
            for i in range(len(self.my_lists)):
                if list_name == self.my_data[i][0]:
                    print("List to be removed is {}\n".format(list_name))
                    trash_path = '.\\trash'
                    shutil.move(self.my_data[i][1], trash_path)
                    
                    del self.my_lists[i]
                    file = open(self.lists_path, 'w')
                    file.write('lists = ' + pprint.pformat(self.my_lists) + '\n')
                    file.close()
                    
                    del self.my_data[i]
                    file = open(self.data_path, 'w')
                    file.write('data = ' + pprint.pformat(self.my_data) + '\n')
                    file.close()
                    return

                
    def view_lists(self):
        logging.debug("view_lists() call")
        for i in range(len(self.my_lists)):
            print(str(i) + ' ' + self.my_lists[i] + '\n')
            
        value = int(input('Type the number to select the list. Type -1 to go to main menu.\n'))
        if value in range(len(self.my_lists) ):
            return value
        else:
            return None
    
    def get_input(self):
        logging.debug("get_input() call")
        value = '0'
        while value not in "1234":
            print("\nWhat do you want to do?\n")
            print("1 Create a new list.")
            print("2 Remove a list.")
            print("3 View the lists.")
            print("4 Quit.\n")
            value = input()
        return value
    
    def menu(self, value):
        logging.debug("menu() call")
        assert value in "1234", "Menu has gotten an invalid input."
        if value == "1":
            self.create_list(self.get_list_data())
        elif value == "2":
            self.remove_list(self.get_list_name())
        elif value == "3":
            list_to_view = self.view_lists()
            return list_to_view
        else:
            sys.exit()