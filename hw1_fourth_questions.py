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

import pandas as pd

path= "/Users/ruimaciel/Desktop/Barcelona/Computing for Data Science/computing_ds/covid.csv"
list=(500,1000,5000)
for i in list:
    covids = pd.read_csv(path)
    covids=covids.loc[covids['Confirmed'] > i, ['Country','Deaths', "Confirmed"]]
    print(f"Countries and respective deaths and confirmed cases of covid with more than {i} confirmed cases")
    covids
    mean_deaths=covids["Confirmed"].mean()
    mean_confirmed=covids["Deaths"].mean()
    print(f"The total average of Deaths and Confirmed cases among countries with more than {i} active cases daily are, respectively, {mean_deaths} and {mean_confirmed}.")