import json

nursery_rhyme = [
    "Mary had a little lamb",
    "Its fleece was white as snow,",
    "And everywhere that Mary went,",
    "The lamb was sure to go."
]

with open('Mary.txt', 'w') as file:  # * /
    for line in nursery_rhyme:  # *
        file.write(line + "\n")


# * Had to create a file named names.txt
dictionary = {
    1: "William",
    2: "Patrick",
    3: "Jon",
    4: "Tom",
    5: "Peter",
    6: "Colin",
    7: "Sylvester",
    8: "Paul",
    9: "Chris",
    10: "David",
    11: "Matt",
    12: "Peter",
    13: "Jodie",
}

with open('names.txt', 'w') as file:
    print(json.dump(dictionary, file, indent=4))  # *
