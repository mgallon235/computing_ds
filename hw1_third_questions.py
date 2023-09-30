#############

# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)

cases={'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}


# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country

cases={'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}

def total_registered_cases(a : dict, b: str):
    total_per_country=sum(a.get(b))
    return total_per_country

answer7=total_registered_cases(cases, "Spain")
print(answer7)


# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#

cases={'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}

def total_registered_cases(a : dict):
    new_dict={}
    for k in a.keys():
        total_per_country=sum(a.get(k))
        new_dict.update({k:total_per_country})
    return new_dict

answer8=total_registered_cases(cases)
print(answer8)


# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases

cases={'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}

def country_with_most_cases(dictionary : dict):
    new_dict={}
    for k in dictionary.keys():
        total_per_country=sum(dictionary.get(k))
        new_dict.update({k:total_per_country})
    max_key = max(new_dict, key=lambda k: new_dict[k])
    return max_key

answer9=country_with_most_cases(cases)
print(answer9)