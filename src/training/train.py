# Import libraries and packages
from sklearn import svm, datasets
import pickle

# Load our training data
data = datasets.load_iris()
X = data.data
y = data.target

# Training the model. Here we go with a SVM
model = svm.SVC().fit(X, y)

# Persist model so that it can be used by different consumers
models_folder = './src/training/'
model_file_name = 'model.pickle'
pickle.dump(model, open(models_folder+model_file_name, 'wb'))