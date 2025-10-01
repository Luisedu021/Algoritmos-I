string = '98.87,100.91,22.12'
string_list = [f"'{value}'" for value in string.split(',')]
separator = ','
string_with_apostrophe = separator.join(string_list)
print(string_with_apostrophe)