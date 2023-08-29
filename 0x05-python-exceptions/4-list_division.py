#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                result_list.append(0)
            else:
                try:
                    element_1 = my_list_1[i]
                    element_2 = my_list_2[i]

                    if not isinstance(element_1, (int, float)) or \
                            not isinstance(element_2, (int, float)):
                        print("wrong type")
                        result_list.append(0)
                    else:
                        if element_2 == 0:
                            raise ZeroDivisionError
                        result = element_1 / element_2
                        result_list.append(result)
                except ZeroDivisionError:
                    print("division by 0")
                    result_list.append(0)
    except IndexError:
        pass
    finally:
        return result_list
