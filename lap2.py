

# Q1

def multiplication_table(n):
    table = []
    
    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            row.append(i * j)
        table.append(row)
    
    return table

number = int(input("Enter the number to generate custom multiplication table: "))
print(multiplication_table(number))


# Q2
def convert_dictionary(name_list):
    name_dict = {}

    for name in name_list:
        first_letter = name[0]

        if first_letter not in name_dict:
            
            name_dict[first_letter] = []
        name_dict[first_letter].append(name)

    for letter in name_dict:
        name_dict[letter]

    return name_dict

input_list = ["khaled", "hager", "ahmed"]
print(convert_dictionary(input_list))