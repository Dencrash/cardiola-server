# cardiola-server

This server is made for the cardiola-app, which is a prototyped medical app for the AppleTV. It is used to collect the data about blood-pressure and heart-rate of a user, that is send by the app. The server also has an API for cardiac-disease prediction based on the collected data and further information about the user.

DISCLAIMER: The machine learning model that is used to predict, if a user suffers from a cardiac-disease is only a non-valitated prototype. While the model was trained on a real medical dataset, it is not validated by experts in any way and there is not enough available data for a high confidence in the model.

The cardiola-app can be found here: ...

## Setup

First install the requirements of the project using:

```pip install -r requirements.txt```

Note: The Scipy-stack will require additional C-libraries to be installed for a pip-installation. Please get further information from their website.

Then setup and seed the database:

```
python db_create.py
python db_seed.py
```

Run the app using:

```
python app.py
```
