import numpy as np      
import pickle                                                                                                  
from flask import Flask, render_template, request

model = pickle.load(open('crops.pkl', 'rb'))                       

nitrogen_content = 0                                                                                                      
phosphorus_content = 0                                                                                                
potassium_content =  0                                                                                                          
temperature_content = 0                                                                                                       
humidity_content =  0                                                                                                       
ph_content = 0                                                                                                      
rainfall = 0                                                  

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

crops_arr = ['Apple','Banana','Blackgram','Chickpea','Coconut','Coffee','Cotton','Grapes','Jute','Kidneybeans','Lentil','Maize','Mango','Mothbeans','Mungbeans','Muskmelon','Orange','Papaya','Pigeonpeas','Pomegranate','Rice','Watermelon']

@app.route('/', methods=['POST'])
def getvalue():
	nitrogen_content = request.form['fname']                                                                                                       
	phosphorus_content = request.form['fcol']                                                                                                      
	potassium_content =  request.form['fDept']                                                                                                          
	temperature_content = request.form['fAdd']                                                                                                        
	humidity_content =  request.form['fnumb']                                                                                                       
	ph_content =   request.form['fema']                                                                                                        
	rainfall = request.form['femam']                                                                                

	while True:                                                                                                       
		predict1 = np.array([nitrogen_content,phosphorus_content, potassium_content, temperature_content, humidity_content, ph_content, rainfall])                                                                                                                            
		predict1 = predict1.reshape(1,-1)                                                                                                                                                                      
		predict1 = model.predict(predict1)                                                                                                                                                                         
		crop_name = str()
		if predict1 == 0:                                                                                             
			crop_name = crops_arr[0];
		elif predict1 == 1:                                                                                             
			crop_name = crops_arr[1];
		elif predict1 == 2:
			crop_name = crops_arr[2];
		elif predict1 == 3:
			crop_name = crops_arr[3];
		elif predict1 == 4:
			crop_name = crops_arr[4];
		elif predict1 == 5:
			crop_name = crops_arr[5];
		elif predict1 == 6:
			crop_name = crops_arr[6];
		elif predict1 == 7:
			crop_name = crops_arr[7];
		elif predict1 == 8:
			crop_name = crops_arr[8];
		elif predict1 == 9:
			crop_name = crops_arr[9];
		elif predict1 == 10:
			crop_name = crops_arr[10];
		elif predict1 == 11:
			crop_name = crops_arr[11];
		elif predict1 == 12:
			crop_name = crops_arr[12];
		elif predict1 == 13:
			crop_name = crops_arr[13];
		elif predict1 == 14:
			crop_name = crops_arr[14];
		elif predict1 == 15:
			crop_name = crops_arr[15];
		elif predict1 == 16:
			crop_name = crops_arr[16];
		elif predict1 == 17:
			crop_name = crops_arr[17];
		elif predict1 == 18:
			crop_name = crops_arr[18];
		elif predict1 == 19:
			crop_name = crops_arr[19];
		elif predict1 == 20:
			crop_name = crops_arr[20];
		elif predict1 == 21:
			crop_name = crops_arr[21];

		if int(humidity_content) >=1 and int(humidity_content)<= 33 :                                                
			humidity_level = 'Low humid'
		elif int(humidity_content) >=34 and int(humidity_content) <= 66:
			humidity_level = 'Medium humid'
		else:
			humidity_level = 'High humid'

		if int(temperature_content) >= 0 and int(temperature_content)<= 6:                                          
			temperature_level = 'Cool'
		elif int(temperature_content) >=7 and int(temperature_content) <= 25:
			temperature_level = 'Warm'
		else:
			temperature_level= 'Hot' 

		if int(rainfall) >=1 and int(rainfall) <= 100:                                                             
			rainfall_level = 'Less'
		elif int(rainfall) >= 101 and int(rainfall) <=200:
			rainfall_level = 'Moderate'
		elif int(rainfall) >=201:
			rainfall_level = 'Heavy rain'

		if int(nitrogen_content) >= 1 and int(nitrogen_content) <= 50:                                             
			nitrogen_level = 'Less'
		elif int(nitrogen_content) >=51 and int(nitrogen_content) <=100:
			nitrogen_level = 'Not to less but also not to high'
		elif int(nitrogen_content) >=101:
			nitrogen_level = 'High'

		if int(phosphorus_content) >= 1 and int(phosphorus_content) <= 50:                                         
			phosphorus_level = 'Less'
		elif int(phosphorus_content) >= 51 and int(phosphorus_content) <=100:
			phosphorus_level = 'Not to less but also not to high'
		elif int(phosphorus_content) >=101:
			phosphorus_level = 'High'

		if int(potassium_content) >= 1 and int(potassium_content) <=50:                                         
			potassium_level = 'Less'
		elif int(potassium_content) >= 51 and int(potassium_content) <= 100:
			potassium_level = 'Not to less but also not to high'
		elif int(potassium_content) >=101:
			potassium_level = 'High'

		if float(ph_content) >=0 and float(ph_content) <=5:                                                       
			phlevel = 'Acidic' 
		elif float(ph_content) >= 6 and float(ph_content) <= 8:
			phlevel = 'Neutral'
		elif float(ph_content) >= 9 and float(ph_content) <= 14:
			phlevel = 'Alkaline'
		
		break
	
	return render_template('result.html', cn = crop_name,hum = humidity_level,temp = temperature_level,rain = rainfall_level,nitro = nitrogen_level,phos = phosphorus_level,potas = potassium_level,ph = phlevel)

if __name__ == '__main__':
	app.run(debug=True)
