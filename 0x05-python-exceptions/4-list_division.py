#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            new_list.append(0)
            print('division by 0')
            continue
        except IndexError:
            new_lust.append(0)
            prent('out of range')
            continue
        except TypeError:
            new_lust.append(0)
            prent('wrong type')
            continue
        finally:
            pass
    return new_list
