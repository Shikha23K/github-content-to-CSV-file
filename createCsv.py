import pandas as pd
import requests
#link is fetched from the githubusercontent of csv file and then creating own csv file by coding
url='https://raw.githubusercontent.com/mrcorizo/Qngn-Fpvrapr/main/PyDS/cars93.csv'
res=requests.get(url, allow_redirects=True)
with open('cars93.csv','wb') as file:
    file.write(res.content)
    cars_df=pd.read_csv('cars93.csv')
