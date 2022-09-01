def search_replace(my_list, search, replace):
    list_copy = my_list[:]
    for i in range(len(list_copy)):
        if search in list_copy and list_copy[i] is search:
            list_copy[i] = replace
        # else:
        #     print("Element not found")

    return list_copy
