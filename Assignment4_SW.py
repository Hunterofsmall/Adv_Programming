import pandas as pd
import pdb 

fatality = []
for age in range(0,101):
    if age <= 17:
        fatality.append(20 / 1000000)
    elif age <= 49:
        fatality.append(500 / 1000000)
    elif age <= 64:
        fatality.append(6000 / 1000000)
    else:  
        fatality.append(90000 / 1000000)

data_dict = {'Age': list(range(0,101)), 'fatality rate': fatality}
dt1 = pd.DataFrame(data_dict)
dt2 = pd.read_csv('WorldDemographics.csv')
dt2 = dt2.drop(['Unnamed: 0', 'continent_code','country_code','Level'], axis=1)
Joined = pd.merge(dt1, dt2, on= 'Age')
# Joined['PopulationID'].nunique()
Joined['Expected death in Country/Age'] = Joined['fatality rate'] * Joined['#Alive']
Expected_death = Joined.groupby('PopulationID')['Expected death in Country/Age'].sum()
#pdb.set_trace()
Total_population = Joined.groupby('PopulationID')['#Alive'].sum()
dt3 = pd.merge(Expected_death, Total_population, on='PopulationID')
dt3 = dt3.rename(columns={'Expected death in Country/Age': 'Expected death'})
dt3['Percentage death(%)'] = dt3['Expected death']/dt3['#Alive'] *100
dt3 = dt3.rename(columns={'#Alive': 'Total population'})
dt3.index.name = 'Country'
dt3 = dt3[['Total population', 'Expected death', 'Percentage death(%)']]
print(dt3)
#pdb.set_trace()
dt3.to_csv('Assignment 4_Shenghan Wu.csv')