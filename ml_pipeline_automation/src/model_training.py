import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model(X, y, config):
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
        test_size=config['train_test_split']['test_size'], 
        random_state=config['train_test_split']['random_state'])
    clf = RandomForestClassifier(**config['model']['params'])
    clf.fit(X_train, y_train)
    joblib.dump(clf, 'models/model.pkl')
    return clf
