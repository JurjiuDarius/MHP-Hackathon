from numpy import loadtxt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf

workspace_data = loadtxt('hackathon-schema.csv', delimiter=",", skiprows=1, dtype=str)

label_encoder = LabelEncoder()
workspace_data[:, 1] = label_encoder.fit_transform(workspace_data[:, 1])
workspace_data[:, 3] = label_encoder.fit_transform(workspace_data[:, 3])
workspace_data[:, 4] = label_encoder.fit_transform(workspace_data[:, 4])

for i in range(workspace_data.shape[0]):
    workspace_data[i, 2] = workspace_data[i, 2].split('/')[0]

X = workspace_data[:, 1:3].astype(int)
y = workspace_data[:, 3:5].astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16 , activation='relu'),
    tf.keras.layers.Dense(8 , activation='relu'),
    tf.keras.layers.Dense(2, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=50, batch_size=2)

loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)

predictions = model.predict(X_test)
print("Predictions:", predictions)

model.save("C:/Users/Mihai/PycharmProjects/ai/mhp hackathon/backend/ai_component/hackathon-schema.keras")