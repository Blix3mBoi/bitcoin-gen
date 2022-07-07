#List to string
def list_to_string(list):
    string = ''
    for i in range(len(list)):
        string = string + list[i]
    return string
def string_to_list(string):
    return list(string)
