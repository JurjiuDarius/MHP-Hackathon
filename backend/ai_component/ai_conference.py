from numpy import loadtxt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from numpy import delete

def convert_to_int(value):
    return 0

workspace_data = loadtxt('meeting-rooms.csv', delimiter=",", skiprows=1, dtype=str)

label_encoder = LabelEncoder()
workspace_data[:, 1] = label_encoder.fit_transform(workspace_data[:, 1])
workspace_data[:, 2] = workspace_data[:, 2].astype(int)
workspace_data[:, 4] = label_encoder.fit_transform(workspace_data[:, 4])
workspace_data[:, 5] = [0 for val in workspace_data[:, 5]]
workspace_data[:, 6] = label_encoder.fit_transform(workspace_data[:, 6])
workspace_data[:, 7] = [0 for val in workspace_data[:, 7]]
workspace_data[:, 8] = label_encoder.fit_transform(workspace_data[:, 8])
workspace_data[:, 9] = [0 for val in workspace_data[:, 9]]
workspace_data[:, 10] = label_encoder.fit_transform(workspace_data[:, 10])
workspace_data[:, 11] = [0 for val in workspace_data[:, 11]]

workspace_data = delete(workspace_data, [5, 7, 9, 11], axis=1)

for i in range(workspace_data.shape[0]):
    workspace_data[i, 3] = workspace_data[i, 3].split('/')[0]

X = workspace_data[:, 1:4].astype(int)
y = workspace_data[:, 4:12].astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(27 , activation='relu6'),
    tf.keras.layers.Dense(4 , activation='gelu'),
    tf.keras.layers.Dense(12 , activation='relu6'),
    tf.keras.layers.Dense(4 , activation='sigmoid')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=50, batch_size=10)

loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)

#predictions = model.predict(X_test)
#print("Predictions:", predictions)

model.save("C:/Users/Mihai/PycharmProjects/ai/mhp hackathon/backend/ai_component/meeting-rooms.keras")