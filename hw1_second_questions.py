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
            if key == 'jobs' and val[0] == param:   # condition iterations in jobs and look for any analyst
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
#
