#API com Flask
from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd

app = Flask(__name__)
api = Api(app)

#Pegar uma url e filtrar os dados
#Parte I
url = 'https://raw.githubusercontent.com/rudeboybert/fivethirtyeight/master/data-raw/births/US_births_2000-2014_SSA.csv'
df = pd.read_csv(url)
#Parte II
df= df[df.year == 2000 ]
df.drop(columns=['year','day_of_week'], inplace = True)
df.rename(columns = {'month':'Mês', 'date_of_month':'Dia do mês', 'births':'Nascimentos'}, inplace = True)

class Dados(Resource):
    def get(self):
        return df.to_json()
    
api.add_resource(Dados, '/dados')

if __name__ == '__main__':
    app.run(debug=True)
