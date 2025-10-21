import pickle
import pandas as pd

# import model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

class_label = model.classes_.tolist()
def predict_insurance_premium(input_data):
    data = pd.DataFrame([input_data])
    prediction = model.predict(data)[0]

    # get the probabilities for each class
    probabilities = model.predict_proba(data)[0]
    confidence = max(probabilities)

    # create mapping of class labels to probabilities
    class_probabilities = dict(zip(class_label, map(lambda x: round(x, 2), probabilities)))
    
    return {
        'prediction': prediction,
        'confidence': confidence,
        'class_probabilities': class_probabilities
    }