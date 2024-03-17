from datetime import datetime

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
import tensorflow as tf
# #
def get_day_of_week_numeric(date_str):
    # Convert the string to a datetime object
    date_object = datetime.strptime(date_str, '%d/%m/%Y')
    # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    day_of_week_numeric = date_object.weekday()
    return day_of_week_numeric
#
def one_hot_encode(day_of_week_numeric):
    # Define the number of classes (days of the week)
    num_classes = 135
    # Create one-hot encoding
    one_hot = tf.one_hot(day_of_week_numeric, num_classes)
    return one_hot

def one_hot_encode_small(day_of_week_numeric):
    # Define the number of classes (days of the week)
    num_classes = 6
    # Create one-hot encoding
    one_hot = tf.one_hot(day_of_week_numeric, num_classes)
    return one_hot

def get_conference_room_number(conference_room):
    if conference_room == "Quick 8":
        return 0
    if conference_room == "Pit-Lane":
        return 1
    if conference_room == "Dry-lane":
        return 2
    if conference_room == "Joker Lap":
        return 3
    if conference_room == "Pole Position":
        return 4
    if conference_room == "Cockpit":
        return 5
def one_hot_encode_conference(conference_room_number):
    # Define the number of classes (days of the week)
    num_classes = 6
    # Create one-hot encoding
    one_hot = tf.one_hot(conference_room_number, num_classes)
    return one_hot

def get_desk_number(desk):
    if desk == "CLUJ_5_beta_18.5":
        return 134
    if desk == "CLUJ_5_beta_19.5":
        return 133
    if desk == "CLUJ_5_beta_19.6":
        return 132
    desk_number = desk.split("_")[3]
    desk_number = (int(desk_number.split(".")[0]) - 1) * 4 + (int(desk_number.split(".")[1]) - 1)
    return desk_number
#
#
def one_hot_encode_desk(desk_number):
    # Define the number of classes (days of the week)
    num_classes = 135
    # Create one-hot encoding
    one_hot = tf.one_hot(desk_number, num_classes)
    return one_hot


classifiers = [
    KNeighborsClassifier(4),
    SVC(kernel="linear", C=0.025, random_state=42),
    SVC(gamma=2, C=1, random_state=42),
    # GaussianProcessClassifier(1.0 * RBF(1.0), random_state=42),
    DecisionTreeClassifier(max_depth=5, random_state=42),
    RandomForestClassifier(
        max_depth=5, n_estimators=10, max_features=1, random_state=42
    ),
    MLPClassifier(solver='adam', hidden_layer_sizes=(5, 10), random_state=4, alpha=0.5, activation='relu'),
    AdaBoostClassifier(algorithm="SAMME", random_state=42),
    GaussianNB(),
    QuadraticDiscriminantAnalysis(),
    XGBClassifier(),
]

for classifier in classifiers:
    print(classifier.__class__.__name__)
    workspace_data = loadtxt('hackathon-schema.csv', delimiter=",", skiprows=1, dtype=str)
    label_encoder = LabelEncoder()
    desk_data = np.array([[one_hot_encode_desk(get_desk_number(workspace_data[i, 1])),
                           one_hot_encode(int(workspace_data[i, 1].split(".")[0].split("_")[3])),
                           one_hot_encode(get_day_of_week_numeric(workspace_data[i, 2]))] for i in
                          range(workspace_data.shape[0])])

    X = np.array([data_entry.flatten() for data_entry in desk_data])
    y = label_encoder.fit_transform(workspace_data[:, 3]).astype(int)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

    learn = classifier
    learn.fit(X_train, y_train)

    pred = learn.predict(X_test)
    acc = accuracy_score (y_test, pred)
    print("Acc morning: %.2f%%" % (acc * 100.0))

    y = label_encoder.fit_transform(workspace_data[:, 4]).astype(int)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

    learn = classifier
    learn.fit(X_train, y_train)

    pred = learn.predict(X_test)
    acc = accuracy_score (y_test, pred)
    print("Acc evening: %.2f%%" % (acc * 100.0))

    workspace_data = loadtxt('meeting-rooms.csv', delimiter=",", skiprows=1, dtype=str)
    label_encoder = LabelEncoder()

    conference_data = np.array([[one_hot_encode_conference(get_conference_room_number(workspace_data[i, 1])),
                                 one_hot_encode_small(get_day_of_week_numeric(workspace_data[i, 3]))] for i in
                                range(workspace_data.shape[0])])
    conference_nineToEleven = label_encoder.fit_transform(workspace_data[:, 4])
    conference_elevenToOne = label_encoder.fit_transform(workspace_data[:, 6])
    conference_oneToThree = label_encoder.fit_transform(workspace_data[:, 8])
    conference_threeToFive = label_encoder.fit_transform(workspace_data[:, 10])

    X = np.array([data_entry.flatten() for data_entry in conference_data])
    y = conference_nineToEleven
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

    learn = classifier
    learn.fit(X_train, y_train)

    pred = learn.predict(X_test)
    acc = accuracy_score (y_test, pred)
    print("Acc nineToEleven: %.2f%%" % (acc * 100.0))

    y = conference_elevenToOne
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

    learn = classifier
    learn.fit(X_train, y_train)

    pred = learn.predict(X_test)
    acc = accuracy_score (y_test, pred)
    print("Acc elevenToOne: %.2f%%" % (acc * 100.0))

    y = conference_oneToThree
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

    learn = classifier
    learn.fit(X_train, y_train)

    pred = learn.predict(X_test)
    acc = accuracy_score (y_test, pred)
    print("Acc oneToThree: %.2f%%" % (acc * 100.0))

    y = conference_threeToFive
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

    learn = classifier
    learn.fit(X_train, y_train)

    pred = learn.predict(X_test)
    acc = accuracy_score (y_test, pred)
    print("Acc threeToFive: %.2f%%" % (acc * 100.0))



