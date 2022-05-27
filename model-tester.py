"""
Test your model here before starting the process. 
"""
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json

TRAINING_DATA_PATH =  'datasets/exports/spam-training-data.pkl'
model_path = "models/spam-sms/spam-model.h5"
tokenizer_path = "models/spam-sms/spam-classifer-tokenizer.json"
data = {}

with open(TRAINING_DATA_PATH, 'rb') as f:
    data = pickle.load(f)

model = load_model(model_path)
tokenizer = data['tokenizer']
labels_legend_inverted = {'0':'ham', "1":'spam'}

def predict(text_str, max_sequence = 280, tokenizer=None):
  if not tokenizer:
    return None
  sequences = tokenizer.texts_to_sequences([text_str])
  x_input = pad_sequences(sequences, maxlen=max_sequence)
  y_output = model.predict(x_input)
  top_y_index = np.argmax(y_output)
  preds = y_output[top_y_index]
  labeled_preds = [{f"{labels_legend_inverted[str(i)]}": x} for i, x in enumerate(preds)]
  return labeled_preds

while True:
    i = input('Insert a prediction: ')
    if i == 'e' or i=='q':
        break
    print(predict(i,tokenizer=tokenizer))