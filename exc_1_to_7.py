# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.
#
def triple(a):
    result = a*3
    return result

triple(4)

# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#
def subtract(a,b):
    result = b - a
    return result

subtract(3,7)



# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}
# You should program the function and not use
# the function "dict" directly

a=[('foo',1),('bar',3)]

def dictionary_maker(a):
    new_dict = {}
    k = []
    v = []
    for t in a: # iterate  over each tuple
        for i in t: # iterate over the values inside the tuple
            if isinstance(i,str): # if the value  is a string then we append it in key list
                k.append(i)
            else:                 # else we  append it in the value list
                v.append(i)

    ## Append to dict
    for (key,val) in zip(k, v): # We then make a for loop over the 2 lists using zip
        new_dict[key] = val     # we then save the key elements inside the key section of the dictionary and the value elements inside the dictionary vals
    return new_dict

x = dictionary_maker(a)

print(x)



############################################
#
# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".
#
# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.


cv = [{'user': 'john', 'jobs': ['analyst', 'engineer']},
      {'user': 'jane', 'jobs': ['finance', 'software']},
      {'user': 'mikel', 'jobs': ['analyst', 'manager']}]


a = 'analyst'
def has_experience_as(cv,param):
    names = []
    for i in cv:   # iterate over each dictionary inside list
        for key,val in i.items(): # iterate over the keys and values of the dictionaries
            if key == 'jobs' and val[0] == param:   # we  fix our iterations in jobs and  look for any analysts
                names.append(i['user'])    # if  we find  a analyst then we save the key value (name of person) in a list
    return names

nombres = has_experience_as(cv,a)

print(nombres)


#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.

def job_counts(cv):
    dict_2 = {}
    lista = []
    for i in cv:
            for key,val in i.items():
                if key == 'jobs':
                    for n in val:
                        lista.append(n)
    for i in lista:
        dict_2[i] = lista.count(i)

    return(dict_2)

x = job_counts(cv)

print(x)

#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.

def most_popular_job(cv):
    new_list = []
    # Transform cv into dictionary of  job counts
    diction = job_counts(cv)
    for k,v in diction.items():
        new_list.append((k,v))

    return new_list

u = most_popular_job(cv)

print(u)




##############

# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)


# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country


# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#


# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases



###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #
