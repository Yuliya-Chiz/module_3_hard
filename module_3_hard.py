def calculate_structure_sum(data_structure):
    global sum
    if isinstance(data_structure,int):
        sum +=data_structure
        return sum
    elif isinstance(data_structure,str):
        sum += len(data_structure)
        return sum
    else:
        for i in data_structure:
            if isinstance(i,dict):
                for key in i.keys():
                    calculate_structure_sum(key)
                for value in i.values():
                    calculate_structure_sum(value)
            else:
                calculate_structure_sum(i)

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum = 0
result = calculate_structure_sum(data_structure)
print(sum)
