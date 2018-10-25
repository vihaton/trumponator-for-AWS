import fasttext
import json

model = None

"""
def read_model():
	model = fasttext.supervised('train.txt', 'model', lr='0.5', epoch=100)
	
def predict(tweet):
	global model
	if model is None:
		read_model()
		
	tweet = [tweet] #the tweet has to be in a list
	return model.predict(tweet)
	#return model.predict_proba(tweet, 6) #returns the probabilities for all 6 classes, the first is the most probable (and therefore the prediction)
"""	

def lambda_handler(event, context):
	#tweet = format(event['tweet'])  

	#pred = predict(tweet)
	#pred = pred[0][0] #this should be a string
	return {
        "statusCode": 200,
        "body": json.dumps("Hello from the other side!")
    }

