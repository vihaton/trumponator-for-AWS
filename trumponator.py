import fasttext

model = None

def read_model():
	model = fasttext.supervised('train.txt', 'model', lr='0.5', epoch=100)
	
def predict(tweet):
	if model is None:
		read_model()
		
	tweet = [tweet] #the tweet has to be in a list
	return model.predict(tweet)
	#return model.predict_proba(tweet, 6) #returns the probabilities for all 6 classes, the first is the most probable (and therefore the prediction)
	

