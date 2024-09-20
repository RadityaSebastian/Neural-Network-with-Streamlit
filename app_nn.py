from types import NoneType
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

st.write("## Weather Prediction with Neural Network")
lst = []
model = load_model('nn_model.keras')
precipitation_numb = st.number_input(
    "Insert precipitation number", value=None, placeholder="Type a number..."
)
lst.insert(1,precipitation_numb)

max_temp = st.number_input(
    "Insert maximum temperature number", value=None, placeholder="Type a number..."
)
lst.insert(2,max_temp)

min_temp = st.number_input(
    "Insert minimum temperature number", value=None, placeholder="Type a number..."
)
lst.insert(3,min_temp)

wind = st.number_input(
    "Insert wind number", value=None, placeholder="Type a number..."
)
lst.insert(4,wind)

if lst[0] != None and lst[1]!=None and lst[2]!=None and lst[3]!=None:
  arrayed_lst = np.array(lst)
  prediction_raw_result = model.predict(arrayed_lst.reshape(1,-1))
  #checking result
  #st.write(prediction_raw_result)
  double_pos = 0
  pred_result = [0,0,0,0,0]
  memory = []
  for i in range(len(prediction_raw_result[0])):
    if 1>=prediction_raw_result[0][i]>0.1:
      pred_result[i]= 1
      double_pos +=1
      memory.append(i)
    else:
      pred_result[i]=0
  test_iteration=0
  if len(memory)==2:
    if prediction_raw_result[0][memory[0]] > prediction_raw_result[0][memory[1]]:
      pred_result[memory[1]] = 0
    else:
      pred_result[memory[0]] = 0
        
  elif len(memory)==3:
    for i in range(len(memory)):
      for j in range(len(memory)):
        for k in range(len(memory)):
          if j == 3:
            j = 0
          if prediction_raw_result[0][memory[k]] > prediction_raw_result[0][memory[j]]>prediction_raw_result[0][memory[3-i]]:
            pred_result[memory[j]] = 0
            pred_result[memory[i]] = 0
          elif prediction_raw_result[0][memory[k]] < prediction_raw_result[0][memory[j]]<prediction_raw_result[0][memory[3-i]]:
            pred_result[memory[k]]=0
            pred_result[memory[j]] =0
          else:
            pred_result[memory[k]] = 0 
            pred_result[memory[i]] = 0

  #st.write(pred_result)
  cols_name = ["drizzle","fog","rain","snow","sun"]
  for i in range(len(pred_result)):
    if pred_result[i]== 1:
      st.write("tommorow weather prediction is:",cols_name[i])
else:
  st.write("You haven't insert a number")
st.markdown('<div style="text-align: right;position: fixed;bottom:0;right:0;">Data Credits: https://www.kaggle.com/datasets/abdelrahman16/weather-seattle </div>', unsafe_allow_html=True)
