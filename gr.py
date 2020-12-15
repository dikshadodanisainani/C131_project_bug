import pandas as pd
df = pd.read_csv('stars.csv')
df.head()
df.columns
df.drop(['Unnamed: 0'],axis=1,inplace=True)
#df['radius']=df['radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

radius = df['radius'].to_list()
mass = df['mass'].to_list()
gravity =[]

#converting solar mass and radius into km & kg
def convert_to_si(radius,mass):
    for i in range(0,len(radius)-1):
        radius[i] = radius[i]*6.957e+8
        mass[i] = mass[i]*1.989e+30
        
convert_to_si(radius,mass)
send me files 
where?


#this is also nbot working