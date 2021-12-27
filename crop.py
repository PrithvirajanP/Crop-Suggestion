import pandas as pd                                                       
from sklearn import preprocessing                                       
from sklearn.neighbors import KNeighborsClassifier                        
import numpy as np        
import pickle

excel = pd.read_excel('crop.xlsx', header = 0) 

le = preprocessing.LabelEncoder()                                         
crop = le.fit_transform(list(excel["CROP"]))                             

                                                    
NITROGEN = list(excel["NITROGEN"])                                        
PHOSPHORUS = list(excel["PHOSPHORUS"])                                    
POTASSIUM = list(excel["POTASSIUM"])                                    
TEMPERATURE = list(excel["TEMPERATURE"])                                 
HUMIDITY = list(excel["HUMIDITY"])                                        
PH = list(excel["PH"])                                                   
RAINFALL = list(excel["RAINFALL"])                                        
	
features = list(zip(NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL))                     
features = np.array([NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL])                   

features = features.transpose()                                                                                                                                                                       

model = KNeighborsClassifier(n_neighbors=3)                                                                    
sv = model.fit(features, crop)    

pickle.dump(sv, open('crops.pkl', 'wb'))