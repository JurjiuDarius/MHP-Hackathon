<h4>Backend</h4>

To start the app, you need to create the environment we are using
To begin with, in the backend folder, run the following commands
<br>
<code>>python -m venv venv</code> <br>
<code>>venv/Scripts/activate</code> <br>
<code>>pip install -r requirements.txt</code> <br>
Starting the backend is quite simple: one would open a command line of their choice, navigate to the backend folder and execute:

<code>>python app.py</code>

Upon successful completion one shall see something among the lines of:
![img.png](img.png)

<h4>Frontend</h4>

You need to install the node packages we are using. Go to the frontend folder and run <br>
<code>>npm install</code>

The app should start upon executing the following in the frontend folder:

<code>>ng serve</code>

After some waiting the app should be running and the command line should display:
![img_1.png](img_1.png)



<h4>The app itself</h4>

Upon connecting to the website the user should log in with the credentials provided by the one running the app as well as select their role.
![img_2.png](img_2.png)

After logging in they will be greeted with the map of the office.
![img_3.png](img_3.png)

Selecting the date of a booking in the top left corner and clicking on an available desk will enable them to book that seat to themselves. Clicking on a meeting room will enable them to add other participants for the given room. For both types of bookings an user can see the other bookings as well as pick a starting and ending time for his booking.
![img_4.png](img_4.png)

<h4>AI Development</h4>
## Feature engineering

Considering that the dataset was very simple, we decided to add and extract meaningful features, such as seat adjacency and weekdays.
### 15.03.2024<br>
We simply tried running the database through different classifiers, from Random Forest Classifier to XGBClassifier to MLPClassifier, provided by Scikit-Learn only obtaining accuracies around 50%. Then we tried using TensorFlow to create a neural network to predict initially obtaining better accuracy, but realising something in our approach was flawed.


### 16.03.2024<br>

We corrected our approach and ran it through the same classifiers obtaining better results of 56% at best and realised we could obtain the same accuracy, if not better if we just coded a guess based on the percentage of occupation of given seats.
<br> <br> 
We then started looking at the data more closely and realised that seat groups may be significant, and we investigated that finding out that they do not have as great a significance as we believed
In the end we settled for a probability-based model for estimating if a given desk will be occupied also considering the day of the week for which we’re estimating as this has proven to have consistent 61% accuracy.
<br> <br> 
This was an insightful approach, because the dataset was very simple. Basically, if a model were to learn the dataset perfectly when using the weekday feature, it would be impossible for it to reach a higher accuracy than this.
<br> <br>
Conference rooms were estimated with a neural network trained for each interval for which data was available having an accuracy of between 56-62%. Each has its own slightly different neural network as none was able to have high accuracy for all intervals.
<br> <br>
We also added a model for predicting office occupation, which could be useful for admins.