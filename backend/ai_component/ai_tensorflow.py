from datetime import datetime

from numpy import loadtxt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
import numpy as np

def get_desk_number(desk):
    if desk == "CLUJ_5_beta_18_5":
        return 134
    if desk == "CLUJ_5_beta_19_5":
        return 133
    if desk == "CLUJ_5_beta_19_6":
        return 132
    desk_number = (int(desk.split("_")[3]) - 1) * 4 + (int(desk.split("_")[4]) - 1)
    return desk_number


def one_hot_encode_desk(desk_number):
    # Define the number of classes (days of the week)
    num_classes = 135
    # Create one-hot encoding
    one_hot = tf.one_hot(desk_number, num_classes)
    return one_hot

def get_day_of_week_numeric(date_str):
    # Convert the string to a datetime object
    date_object = datetime.strptime(date_str, '%d/%m/%Y')
    # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    day_of_week_numeric = date_object.weekday()
    return day_of_week_numeric

def one_hot_encode(day_of_week_numeric):
    # Define the number of classes (days of the week)
    num_classes = 135
    # Create one-hot encoding
    one_hot = tf.one_hot(day_of_week_numeric, num_classes)
    return one_hot

def one_hot_encode_Dg(day_of_week_numeric):
    # Define the number of classes (days of the week)
    num_classes = 33
    # Create one-hot encoding
    one_hot = tf.one_hot(day_of_week_numeric, num_classes)
    return one_hot

workspace_data = loadtxt('hackathon-schema.csv', delimiter=",", skiprows=1, dtype=str)
label_encoder = LabelEncoder()
desk_data = np.array([[one_hot_encode_desk(get_desk_number(workspace_data[i, 1])),
                       one_hot_encode(int(workspace_data[i, 1].split(".")[0].split("_")[3])),
                       one_hot_encode(get_day_of_week_numeric(workspace_data[i, 2]))] for i in
                       range(workspace_data.shape[0])])

X = np.array([data_entry.flatten() for data_entry in desk_data])
y = label_encoder.fit_transform(workspace_data[:, 3]).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(810, activation='relu'),
    tf.keras.layers.Dense(1500, activation='gelu'),
    tf.keras.layers.Dense(1000, activation='relu'),
    tf.keras.layers.Dense(800, activation='gelu'),
    tf.keras.layers.Dense(400, activation='gelu'),
    tf.keras.layers.Dense(400, activation='gelu'),
    tf.keras.layers.Dense(100, activation='gelu'),
    tf.keras.layers.Dense(50, activation='tanh'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(8, activation='gelu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=500, batch_size=1)

loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)



predictions = model.predict(X_test)
correct_predictions = 0

for i in range(len(predictions)):
    if predictions[i] < 0.5:
        if y_test[i] == 0:
            correct_predictions+=1
    else:
        if y_test[i] == 1:
            correct_predictions+=1

print("Predictions:", correct_predictions/len(predictions))

formatted_accuracy="{:.2f}".format(accuracy)

model.save(f"C:/Users/Mihai/PycharmProjects/ai/mhp hackathon/backend/ai_component/hackathon-schema-morning-{formatted_accuracy}.keras")

y = label_encoder.fit_transform(workspace_data[:, 4]).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

model.fit(X_train, y_train, epochs=500, batch_size=10)

loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)

predictions = model.predict(X_test)
correct_predictions = 0

for i in range(len(predictions)):
    if predictions[i] < 0.5:
        if y_test[i] == 0:
            correct_predictions += 1
    else:
        if y_test[i] == 1:
            correct_predictions += 1

print("Predictions:", correct_predictions / len(predictions))

formatted_accuracy="{:.2f}".format(accuracy)

model.save(f"C:/Users/Mihai/PycharmProjects/ai/mhp hackathon/backend/ai_component/hackathon-schema-evening-{formatted_accuracy}.keras")