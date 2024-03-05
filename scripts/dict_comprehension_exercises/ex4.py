string = "Feel Good"

string_dict = {letter:string.count(letter) for letter in string}

print(string_dict)

string_dict_2 = {}
for char in string:
    if char not in string_dict_2:
        string_dict_2[char] = 1
    else:
        string_dict_2[char] += 1

print(string_dict_2)