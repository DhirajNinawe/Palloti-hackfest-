import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# load dataset
data = pd.read_csv('indian_liver_patient.csv')
# fix Gender column (IMPORTANT)
if 'Gender' in data.columns:
    data['Gender'] = data['Gender'].map({'Male': 1, 'Female': 0})

# fix target column (ILPD dataset)
if 'Dataset' in data.columns:
    data['Dataset'] = data['Dataset'].apply(lambda x: 1 if x == 1 else 0)
    X = data.drop('Dataset', axis=1)
    y = data['Dataset']
else:
    print("Check target column name!")
    exit()

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# save model
pickle.dump(model, open('saved_models/liver_model.pkl', 'wb'))

print("🔥 Liver model trained & saved successfully!")