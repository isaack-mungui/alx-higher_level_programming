def replace_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if i < 0:
            pass
        elif i > len(my_list):
            pass

        if i == idx:
            my_list[idx] = element
            return my_list
