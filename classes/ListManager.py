import csv
import sys
import pprint
pp = pprint.PrettyPrinter(indent=4,width=80)

import logging
logging.disable()
logging.basicConfig(level=logging.DEBUG)

class ListManager:
    
    def __init__(self, name, path, length):
        logging.debug("ListManager constructor call.")
        self.name = name
        self.path = path
        self.length = length
        
    def convert_file_to_list(self,path):
        logging.debug("convert_file_to_list() call")
        file = open(path)
        reader = csv.reader(file)
        new_list = list(reader)
        file.close()
        return new_list

    def add_item(self, path):
        logging.debug("add_item() call")
        new_list = self.convert_file_to_list(path)
        new_item = list()
        for i in range(0, self.length):
            value = input("What is entry for " +\
            new_list[0][i]  + " on your " + self.name + "?\n")
            value = value.title()
            new_item.append(value)
        
        new_list.append(new_item)
        file = open(path, 'w', newline='')
        writer = csv.writer(file)
        
        for i in range(len(new_list)):
            writer.writerow(new_list[i])
        file.close()
        
    def remove_item(self, path):
        logging.debug("remove_item() call")
        item = input("What is the item you want to remove?\n")
        item = item.title()
        new_list = self.convert_file_to_list(path)
        found = 0
        for i in range(1,len(new_list)):
            if item in new_list[i]:
                del new_list[i]
                found = 1
                break
    
        if found == 0:
            print("Item could not be found in list.")
        else:
            file = open(path, 'w', newline='')
            writer = csv.writer(file)
            
            for i in range(len(new_list)):
                writer.writerow(new_list[i])
            file.close()
    
    def print_list(self,path):
        logging.debug("print_list() call")
        new_list = self.convert_file_to_list(path)
        pp.pprint(new_list)
        
    def update_ltem(self, path):
        logging.debug("update_item() call")
        new_list = self.convert_file_to_list(path)
        
        item = input("What is the item you want to update?\n")
        item = item.title()
        found = 0
        for i in range(1,len(new_list)):
            if item in new_list[i]:
                new_item_index = i
                found = 1
                break
        
        if found == 0:
            print("Item could not be found in list.")
            logging.debug("update_item() ended.")
            return
            
        else:
            new_item = []
            for i in range(0, self.length):
                value = input("What is entry for " +\
                new_list[0][i]  + " on your " + self.name + "?\n")
                value = value.title()
                new_item.append(value)
        
            new_list.insert(new_item_index, new_item)
            del new_list[new_item_index + 1]
            
            file = open(path, 'w', newline='')
            writer = csv.writer(file)
            
            for i in range(len(new_list)):
                writer.writerow(new_list[i])
            file.close()
            logging.debug("update_item() ended.")
            return
        
    def get_input(self):
        logging.debug("get_input() call")
        value = "0"
        while value not in "12345":
            print("\nWhat do you want to do?")
            print("1 Add an item.")
            print("2 Update an item.")
            print("3 Remove an item.")
            print("4 Print the current list.")
            print("5 Quit.\n")
            value = input()
            self.print_list(self.path)
        return value
    
    def menu(self, value):
        logging.debug("menu() call")
        assert value in "12345", "Menu has gotten an invalid input."
        if value == "1":
            self.add_item(self.path)
        elif value == "2":
            self.update_item(self.path)
        elif value == "3":
            self.remove_item(self.path)
        elif value == "4":
             pass
        else:
            sys.exit()
        if value != "4":
            self.print_list(self.path)