from classes.ListManager import ListManager
      
def main():
    list_name = "To Do List"
    list_path = ".\\lists\\to_do_list.csv"
    list_len = 3
    
    list1 = ListManager(list_name, list_path, list_len)
    
    while True:
        list1.menu(list1.get_input())
    
main()


