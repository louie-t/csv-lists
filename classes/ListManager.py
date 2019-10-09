import csv
import pprint
pp = pprint.PrettyPrinter(indent=4,width=80)

import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable()

class ListManager:
    
    def convert_file_to_list(self, data):
        logging.debug("convert_file_to_list() call")
        file = open(data[1])
        reader = csv.reader(file)
        new_list = list(reader)
        file.close()
        return new_list

    def add_item(self, item, data):
        logging.debug("add_item() call")
        new_list = self.convert_file_to_list(data)
        new_list.append(item)
        
        file = open(data[1], 'w', newline='')
        writer = csv.writer(file)
        
        for i in range(len(new_list)):
            writer.writerow(new_list[i])
        file.close()
        
    def get_new_item(self, data):
        logging.debug("get_item() call")
        new_item = list()
        for i in range(0, data[2]):
            value = input('What is entry for "' +\
            data[3][i]  + '" on "' + data[0] + '"?\n')
            value = value.title()
            new_item.append(value)
       
        return new_item
    
    def get_item(self):
        item = input("What is the item's name?\n")
        item = item.title()
        return item
        
    def remove_item(self, item, data):
        logging.debug("remove_item() call")
        new_list = self.convert_file_to_list(data)
        found = 0
        for i in range(1,len(new_list)):
            if item in new_list[i]:
                del new_list[i]
                found = 1
                logging.debug("removed item.")
                break
    
        if found == 0:
            print("Item could not be found in list.")
            return
        else:
            file = open(data[1], 'w', newline='')
            writer = csv.writer(file)
            logging.debug("Rewrote the list.")
            for i in range(len(new_list)):
                writer.writerow(new_list[i])
            file.close()
    
    def print_list(self, data):
        logging.debug("print_list() call")
        new_list = self.convert_file_to_list(data)
        pp.pprint(new_list)
        
    def update_item(self, item, data):
        logging.debug("update_item() call")
        new_list = self.convert_file_to_list(data)
        
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
            for i in range(0, data[2]):
                value = input("What is the entry for " +\
                new_list[0][i]  + " on your " + data[0] + "?\n\n")
                value = value.title()
                new_item.append(value)
        
            new_list.insert(new_item_index, new_item)
            del new_list[new_item_index + 1]
            
            file = open(data[1], 'w', newline='')
            writer = csv.writer(file)
            
            for i in range(len(new_list)):
                writer.writerow(new_list[i])
            file.close()
            logging.debug("update_item() ended.")
            return
        
    def get_input(self, data):
        logging.debug("get_input() call")
        value = '0'
        while value not in "1234":
            print("\nWhat do you want to do?\n")
            print("1 Add an item.")
            print("2 Update an item.")
            print("3 Remove an item.")
            print("4 Return to main menu.\n")
            self.print_list(data)
            value = input()
        return value
    
    def menu(self, value, data):
        logging.debug("menu() call")
        assert value in "1234", "Menu has gotten an invalid input."
        if value == "1":
            self.add_item(self.get_new_item(data), data)
        elif value == "2":
            self.update_item(self.get_item(), data)
        elif value == "3":
            self.remove_item(self.get_item(), data)
        else:
            return True