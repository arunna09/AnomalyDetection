import pandas as pd
import sklearn

csv = pd.read_csv('data/Torschlag_Trafo_07122015_to_11122015.csv', sep=',')
train, test = sklearn.model_selection.train_test_split(csv, train_size = 0.8)
