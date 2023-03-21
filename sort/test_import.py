from Linked_List import Linked_list
if __name__ == "__main__":
    a = Linked_list()
    a.push_back(1)
    a.push_front(0)
    a.push_back(2)
    a.push_back(3)
    a.print_List()
    a.insert(2, 87)
    a.print_List()