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

import pandas  as pd

def country_summary():
    df =  pd.read_csv('./covid.csv')
    ranges = [500,1000,5000]
    for r in ranges:
        new_df = df['Country'][df['Active']>r]
        tot_avg_death =  round(df['Deaths'][df['Active']>r].mean())
        tot_avg_confirmed =  round(df['Confirmed'][df['Active']>r].mean())

        print(r)
        print(new_df)
        print('avg confirmed',tot_avg_confirmed)
        print('avg death',tot_avg_death)

country_summary()