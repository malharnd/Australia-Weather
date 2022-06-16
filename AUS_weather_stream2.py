
import pandas as pd
import numpy as np
import pickle 
import streamlit as st

pickle_in = open('/Users/md/Python/AUS_weather/RFC3.pkl','rb')
classifier = pickle.load(pickle_in)

def predict_weather(Location,MinTemp,MaxTemp,Rainfall,WindGustDir,WindGustSpeed,RainToday,Mean_pressure,Mean_windsp,Mean_Humidity,Mean_Temp):
    
    """Let's Authenticate the Weather
    This is using docstring for specifications.
    ---
    parameters:
    
      - name: Location 
        in: query 
        type: number 
        required: true
      - name: MinTemp
        in: query 
        type: number 
        required: true
      - name: MaxTemp 
        in: query 
        type: number 
        required: true
      - name: Rainfall 
        in: query 
        type: number 
        required: true
      - name: WindGustDir 
        in: query 
        type: number 
        required: true  
      - name: WindGustSpeed 
        in: query 
        type: number 
        required: true
      - name: RainToday 
        in: query 
        type: number 
        required: true
      - name: Mean_pressure 
        in: query 
        type: number 
        required: true
      - name: Mean_windsp 
        in: query 
        type: number 
        required: true
      - name: Mean_Humidity 
        in: query 
        type: number 
        required: true
      - name: Mean_Temp 
        in: query 
        type: number 
        required: true
        
    responses:
        200:
            description: The output values
    """
    Loc = {'Albury':1 , 'BadgerysCreek': 2, 'Cobar':3, 'CoffsHarbour':4, 'Moree':5,
       'NorahHead':6, 'NorfolkIsland':7, 'Richmond':8, 'Sydney':9,
       'SydneyAirport':10, 'WaggaWagga':11, 'Williamtown':12, 'Wollongong':13,
       'Canberra':14, 'Tuggeranong':15, 'Ballarat':16, 'Bendigo':17, 'Sale':18,
       'MelbourneAirport':19, 'Melbourne':20, 'Mildura':21, 'Nhil':22, 'Portland':23,
       'Watsonia':24, 'Dartmoor':25, 'Brisbane':26, 'Cairns':27, 'GoldCoast':28,
       'Townsville':29, 'Adelaide':30, 'MountGambier':31, 'Nuriootpa':32, 'Woomera':33,
       'Witchcliffe':34, 'PearceRAAF':35, 'PerthAirport':36, 'Perth':37, 'Walpole':38,
       'Hobart':39, 'Launceston':40, 'AliceSprings':41, 'Darwin':42, 'Katherine':43,
       'Uluru':44}
    Location = int(Loc[Location])
    Dir = {'NNW':0, 'NW':1, 'WNW':2, 'N':3, 'W':4, 'WSW':5, 'NNE':6, 'S':7, 'SSW':8, 'SW':9, 'SSE':10,
       'NE':11, 'SE':12, 'ESE':13, 'ENE':14, 'E':15}
    WindGustDir = int(Dir[WindGustDir])
    raintod = {'Yes':1,'No':2}
    RainToday =raintod[RainToday] 
    
       
       
    prediction = classifier.predict([[Location,MinTemp,MaxTemp,Rainfall,WindGustDir,WindGustSpeed,RainToday,Mean_pressure,Mean_windsp,Mean_Humidity,Mean_Temp]])
    if (prediction == 0):
        return "It may not Rain Tomorrow"
    else:
        return "It might Rain Tomorrow"
    return "The Predicted value is " + str(prediction)

def main():
    st.title("Weather Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> Weather Prediction </h2>
    </div>
    """
    arry1 =['','Albury', 'BadgerysCreek', 'Cobar', 'CoffsHarbour', 'Moree',
       'NorahHead', 'NorfolkIsland', 'Richmond', 'Sydney',
       'SydneyAirport', 'WaggaWagga', 'Williamtown', 'Wollongong',
       'Canberra', 'Tuggeranong', 'Ballarat', 'Bendigo', 'Sale',
       'MelbourneAirport', 'Melbourne', 'Mildura', 'Nhil', 'Portland',
       'Watsonia', 'Dartmoor', 'Brisbane', 'Cairns', 'GoldCoast',
       'Townsville', 'Adelaide', 'MountGambier', 'Nuriootpa', 'Woomera',
       'Witchcliffe', 'PearceRAAF', 'PerthAirport', 'Perth', 'Walpole',
       'Hobart', 'Launceston', 'AliceSprings', 'Darwin', 'Katherine',
       'Uluru']
    arry2 =[' ','W', 'WNW', 'WSW', 'NE', 'NNW', 'N', 'NNE', 'SW', 'ENE', 'SSE',
       'S', 'NW', 'SE', 'ESE', 'E', 'SSW']
    rain_arr = [' ', 'Yes','No']
    
    
    st.markdown(html_temp,unsafe_allow_html=True)
    Location = st.selectbox("Location",arry1)
    MinTemp = st.text_input("MinTemp","Type Here")
    MaxTemp = st.text_input("MaxTemp","Type Here")
    Rainfall = st.text_input("Rainfall","Type Here")
    WindGustDir = st.selectbox("Wind Direction",arry2)
    WindGustSpeed = st.slider("Wind Speed",min_value=0.0,max_value=150.0,step=0.1)
    RainToday = st.selectbox("RainToday",rain_arr)
    Mean_pressure = st.text_input("Mean_pressure ","Type Here")
    Mean_windsp = st.text_input("Mean_windsp","Type Here")
    Mean_Humidity = st.text_input("Mean_Humidity","Type Here")
    Mean_Temp = st.text_input("Mean_Temp","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_weather(Location,MinTemp,MaxTemp,Rainfall,WindGustDir,WindGustSpeed,RainToday,Mean_pressure,Mean_windsp,Mean_Humidity,Mean_Temp)
    st.success('{}'.format(result))
   

if(__name__) == '__main__':
    main()
