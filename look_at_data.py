import pandas as pd

parent_path = "D:/Dissertation"

data1 = pd.read_csv(parent_path + "/fire/LFB_2009_2012.csv")
data2 = pd.read_csv(parent_path + "/fire/LFB_2013_2016.csv")
data3 = pd.read_csv(parent_path + "/fire/LFB_2017.csv")

data = data1.append(data2)
data = data.append(data3)

data = data.loc[data['Easting_m'].notnull()]

data = data.loc[data['IncidentGroup'] == 'Fire']

data = data.loc[data['StopCodeDescription'] == 'Primary Fire']

data = data.loc[(data['AddressQualifier'] == 'Correct incident location') | (data['AddressQualifier'] == 'Within same building')]

data = data.loc[data['PropertyCategory'] != 'Road Vehicle']

print(len(data))

data.to_csv(parent_path + "/fire/filtered_fire.csv")