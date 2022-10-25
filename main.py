# TODO Update Values in Dictionaries and Lists

# TODO Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [[5, 2, 3], [10, 8, 9]]

x[1][0] = 15

print(x)

# TODO Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

students[0]['last_name'] = 'Bryant'

print(students)

# TODO In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'Andres'

print(sports_directory)
# TODO Change the value 20 in z to 30
z = [{'x': 10, 'y': 20}]

z[0]['y'] = 30

print(z)

# TODO Iterate Through a List of Dictionaries Create a function iterateDictionary(some_list) that, given a list of
#  dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.
#  For example, given the following list:

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonelcopy

def iterateDictionary(studentsParameter):
    for student in studentsParameter:
        str = ""
        for k, v in student.items():
            str += f"{k} - {v}, "
        print(str[:-2])


iterateDictionary(students)


# TODO Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name,
#  the function prints the value stored in that key for each dictionary.
def iterateDictionary2(key_name, some_list):
    for student in some_list:
        print(student[key_name])


#  For example, iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB

iterateDictionary2('first_name', students)


# And iterateDictionary2('last_name', students) should output:

iterateDictionary2('last_name', students)
# Jordan
# Rosales
# Guillen
# Tonel


# TODO Iterate Through a Dictionary with List Values
#
#  Create a function printInfo(some_dict) that given a dictionary
#  whose values are all lists, prints the name of each key along with the size of its list, and then prints the
#  associated values within each key's list. For example:

def printInfo(some_dict):
    for k,v in some_dict.items():
        print(len(v), k.upper())
        for i in v:
            print(i)
        print()


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# output:
# 7 LOCATIONS
# San
# Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
#
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
