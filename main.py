
import os
from prediction_Validation_Insertion import pred_validation
from trainingModel import trainModel
from training_Validation_Insertion import train_validation
import flask_monitoringdashboard as dashboard
from predictFromModel import prediction
import json
import sys
import time
from colored import fg, bg, attr


def predictRouteClient():
    try:
        key = input('Enter y to used inbuilt wafer dataset or any key to used own dataset: ')
        ag1=fg('green_3b')+ 'Please enter releative or absolute path for prediction datasets folder:' + attr('reset')
        while (True):
            if key=='y':
                path = 'Prediction_Batch_files'
                break
            else:
                path = input(ag1)
                break
        if path !='':
            path = path

            pred_val = pred_validation(path) #object initialization

            pred_val.prediction_validation() #calling the prediction_validation function

            pred = prediction(path) #object initialization

            # predicting for dataset present in database
            path,json_predictions = pred.predictionFromModel()
            print(("Prediction File created at !!!"  +str(path) +'and few of the predictions are '+str(json.loads(json_predictions) )))
        else:
            print('Provide the Dataset path')
    except Exception as e:
        print("Error Occurred! %s" %e)



def trainRouteClient():
    key = input('Enter y to used inbuilt wafer dataset or any key to used own dataset: ')
    ag2=fg('green_3b')+ 'Please enter releative or absolute path for training datasets folder:' + attr('reset')
    while (True):
        if key=='y':
            path = 'Training_Batch_Files'
            break
        else:
            path = input(ag2)
            break

    try:
        if path !='':

            train_valObj = train_validation(path) #object initialization

            train_valObj.train_validation()#calling the training_validation function


            trainModelObj = trainModel() #object initialization
            trainModelObj.trainingModel() #training the model for the files in the table
            print("Training successfull!!")
        else:
            print('Provide the Dataset path')


    except Exception as e:

        print("Error Occurred! %s" % e)
    
if __name__ == "__main__":
    n = len(sys.argv)

    if n==2 and sys.argv[1]=='--train':
        trainRouteClient()
    elif n==2 and sys.argv[1]=='--predict':
        predictRouteClient()
    else:
        text='''

        Note: This program only take one argument either --train or --predict
        This is the main function to enter the program:)
        you can train or predict the  directly on your Wafer dataset from main.py
        using two argument :)
        1) --train
        2) --predict  

        --train   This argument is used for training  by providing folder path of the dataset
        --predict This argument is used for predicting on model by providing the dataset folder path

        e.g. 
        for training   (main.py --train)
        for prediction (main.py --predict)

        '''
        print (fg('green_3b')+text + attr('reset'))
    


