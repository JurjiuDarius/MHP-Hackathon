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
    workspace_data[:, 1] = label_encoder.fit_transform(workspace_data[:, 1])
    workspace_data[:, 3] = label_encoder.fit_transform(workspace_data[:, 3])
    workspace_data[:, 4] = label_encoder.fit_transform(workspace_data[:, 4])

    for i in range(workspace_data.shape[0]):
        workspace_data[i, 2] = workspace_data[i, 2].split('/')[0]

    X = workspace_data[:, 1:3].astype(int)
    y = workspace_data[:, 3].astype(int)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

    learn = classifier
    learn.fit(X_train, y_train)

    pred = learn.predict(X_test)
    acc = accuracy_score (y_test, pred)
    print("Acc morning: %.2f%%" % (acc * 100.0))

    y = workspace_data[:, 4].astype(int)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

    learn = classifier
    learn.fit(X_train, y_train)

    pred = learn.predict(X_test)
    acc = accuracy_score (y_test, pred)
    print("Acc evening: %.2f%%" % (acc * 100.0))


    workspace_data = loadtxt('meeting-rooms.csv', delimiter=",", skiprows=1, dtype=str)

    def convert_to_int(value):
        if value.strip():  # Check if the string is not empty after stripping whitespace
            return int(value)
        else:
            return 0

    label_encoder = LabelEncoder()
    workspace_data[:, 1] = label_encoder.fit_transform(workspace_data[:, 1])
    workspace_data[:, 2] = workspace_data[:, 2].astype(int)
    workspace_data[:, 4] = label_encoder.fit_transform(workspace_data[:, 4])
    workspace_data[:, 5] = [convert_to_int(val) for val in workspace_data[:, 5]]
    workspace_data[:, 6] = label_encoder.fit_transform(workspace_data[:, 6])
    workspace_data[:, 7] = [convert_to_int(val) for val in workspace_data[:, 7]]
    workspace_data[:, 8] = label_encoder.fit_transform(workspace_data[:, 8])
    workspace_data[:, 9] = [convert_to_int(val) for val in workspace_data[:, 9]]
    workspace_data[:, 10] = label_encoder.fit_transform(workspace_data[:, 10])
    workspace_data[:, 11] = [convert_to_int(val) for val in workspace_data[:, 11]]

    for i in range(workspace_data.shape[0]):
        workspace_data[i, 3] = workspace_data[i, 3].split('/')[0]

    X = workspace_data[:, 1:4].astype(int)
    y = workspace_data[:, 4].astype(int)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

    learn = classifier
    learn.fit(X_train, y_train)

    pred = learn.predict(X_test)
    acc = accuracy_score (y_test, pred)
    print("Acc nineToEleven: %.2f%%" % (acc * 100.0))

    y = workspace_data[:, 6].astype(int)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

    learn = classifier
    learn.fit(X_train, y_train)

    pred = learn.predict(X_test)
    acc = accuracy_score (y_test, pred)
    print("Acc elevenToOne: %.2f%%" % (acc * 100.0))

    y = workspace_data[:, 8].astype(int)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

    learn = classifier
    learn.fit(X_train, y_train)

    pred = learn.predict(X_test)
    acc = accuracy_score (y_test, pred)
    print("Acc oneToThree: %.2f%%" % (acc * 100.0))

    y = workspace_data[:, 10].astype(int)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

    learn = classifier
    learn.fit(X_train, y_train)

    pred = learn.predict(X_test)
    acc = accuracy_score (y_test, pred)
    print("Acc threeToFive: %.2f%%" % (acc * 100.0))



# classifiers = [
#     KNeighborsClassifier(4),
#     SVC(kernel="linear", C=0.025, random_state=42),
#     SVC(gamma=2, C=1, random_state=42),
#     GaussianProcessClassifier(1.0 * RBF(1.0), random_state=42),
#     DecisionTreeClassifier(max_depth=5, random_state=42),
#     RandomForestClassifier(
#         max_depth=5, n_estimators=10, max_features=1, random_state=42
#     ),
#     MLPClassifier(alpha=1, max_iter=10000, random_state=42),
#     AdaBoostClassifier(algorithm="SAMME", random_state=42),
#     GaussianNB(),
#     QuadraticDiscriminantAnalysis(),
#     XGBClassifier(),
# ]

# for classifier in classifiers:
#
#     print("Classifier:", classifier.__class__.__name__)
#     #all day
#     # y = workspace_data[:, 3:5].astype(int)
#     #
#     # X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.33, random_state=7)
#     #
#     # learn = classifier
#     # learn.fit(X_train, y_train)
#     #
#     # pred = learn.predict(X_test)
#     # acc = accuracy_score (y_test, pred)
#     # print("Acc all day: %.2f%%" % (acc * 100.0))
#
#     # only morning
#     y = workspace_data[:, 3].astype(int)
#
#     X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.33, random_state=7)
#
#     learn = classifier
#     learn.fit(X_train, y_train)
#
#     pred = learn.predict(X_test)
#     acc = accuracy_score (y_test, pred)
#     print("Acc morning: %.2f%%" % (acc * 100.0))
#
#     # only evening
#     y = workspace_data[:, 4].astype(int)
#
#     X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.33, random_state=42)
#
#     learn = classifier
#     learn.fit(X_train, y_train)
#
#     pred = learn.predict(X_test)
#     acc = accuracy_score (y_test, pred)
#     print("Acc evening: %.2f%%" % (acc * 100.0))

