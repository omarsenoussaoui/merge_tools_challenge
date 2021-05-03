def merge_tools(str,key):
    for i in range(0, len(string), key):
        list_of_strings = string[i:i + key];
        final_string = ''
        for char in list_of_strings:
            if char not in final_string:
                final_string = final_string + char;
        print(final_string)



if __name__ == '__main__':
    string = 'AABCAAADA'
    key = 3
    merge_tools(string, key)