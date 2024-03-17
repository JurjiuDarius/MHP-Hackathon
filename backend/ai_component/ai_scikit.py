from numpy import loadtxt
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

classifiers = [
    KNeighborsClassifier(4),
    SVC(kernel="linear", C=0.025, random_state=42),
    SVC(gamma=2, C=1, random_state=42),
    GaussianProcessClassifier(1.0 * RBF(1.0), random_state=42),
    DecisionTreeClassifier(max_depth=5, random_state=42),
    RandomForestClassifier(
        max_depth=5, n_estimators=10, max_features=1, random_state=42
    ),
    MLPClassifier(alpha=1, max_iter=10000, random_state=42),
    AdaBoostClassifier(algorithm="SAMME", random_state=42),
    GaussianNB(),
    QuadraticDiscriminantAnalysis(),
    XGBClassifier(),
]

label_encoder = LabelEncoder()
workspace_data = loadtxt('hackathon-schema.csv', delimiter=",", skiprows=1, dtype=str)
workspace_data[:, 1] = label_encoder.fit_transform(workspace_data[:, 1])
workspace_data[:, 2] = label_encoder.fit_transform(workspace_data[:, 2])
workspace_data[:, 3] = label_encoder.fit_transform(workspace_data[:, 3])
workspace_data[:, 4] = label_encoder.fit_transform(workspace_data[:, 4])

X = workspace_data[:, 1:3].astype(int)

for classifier in classifiers:

    print("Classifier:", classifier.__class__.__name__)
    #all day
    # y = workspace_data[:, 3:5].astype(int)
    #
    # X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.33, random_state=7)
    #
    # learn = classifier
    # learn.fit(X_train, y_train)
    #
    # pred = learn.predict(X_test)
    # acc = accuracy_score (y_test, pred)
    # print("Acc all day: %.2f%%" % (acc * 100.0))

    # only morning
    y = workspace_data[:, 3].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.33, random_state=7)

    learn = classifier
    learn.fit(X_train, y_train)

    pred = learn.predict(X_test)
    acc = accuracy_score (y_test, pred)
    print("Acc morning: %.2f%%" % (acc * 100.0))

    # only evening
    y = workspace_data[:, 4].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.33, random_state=42)

    learn = classifier
    learn.fit(X_train, y_train)

    pred = learn.predict(X_test)
    acc = accuracy_score (y_test, pred)
    print("Acc evening: %.2f%%" % (acc * 100.0))
