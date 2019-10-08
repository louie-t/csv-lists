import csv
import pprint
import shutil
pp = pprint.PrettyPrinter(indent=4,width=80)

import logging
logging.basicConfig(level=logging.DEBUG)

class ListsManager:
    my_list_data = list() 
    # The list contains a lists of list. Each sublist corresponds to the individual list. 
    # Sublists has the name, path, and number of categories respectively.
    my_lists = list()
    # This list contains a list of all of the list objects, of type "ListManager"
    
    def validate_string(self,value):
        logging.debug('Validating string')
        for i in value:
            if i.isalpha():
                return True
        return False

    def create_list(self):
        logging.debug('Creating list')
        while True:
            value = input("Enter the name for the list. It must be only letters.")
            if self.validate_string(value):
                list_name = value.title()
                temp = value.split(' ')
                file_name = '_'.join(temp)
                file_name = file_name + '.csv'
                list_path = '.\\lists\\' + file_name
                break
        
        
        num_categories = 0
        categories = list()
        
        while True:
            print("Enter the category number {}. Enter nothing to finish.".format(num_categories + 1))
            category = input()
            if category == "":
                break
            else:
                category = category.title()
                categories.append(category)
                num_categories += 1
                
        file = open(list_path, 'w')
        file.close()
        
        file = open(list_path, 'w', newline='')
        writer = csv.writer(file)
        
          
        new_list = list()
        new_list.append(categories)
        
        for i in range(len(new_list)):
            writer.writerow(new_list[i])
        file.close()
        
        self.my_lists.append(new_list)
        
        new_data = [list_name, list_path, num_categories]
        self.my_list_data.append(new_data)
        
    def remove_list(self):
        while True:
            value = input("Enter the list to remove. Type quit to cancel.")
            value = value.title()
            if value == "Quit":
                break
            for i in range(len(self.my_list_data)):
                if value == self.my_list_data[i][0]:
                    shutil.copy(self.my_list_data[i][1])
                    del self.my_list_data[i]
                    del self.my_lists[i]
        

