# Train-Notification #

## Desktop Notifier for Train departure ##

* Python 3.8.5
* requests
* plyer
* pytz


> **USE-CASES:**

Script runs between 17.00 and 18.00 pm.

Retrieves data of departures every one minute for the route from **S Südkreuz** to **S+U Potsdamer Platz**.

The data are retrieved from the service API [VBB](https://github.com/derhuerst/vbb-rest/blob/5/docs/readme.md)

There are many results in each call, only the first one is manipulated.

Retrieves current time in berlin that has always has to be greater than the train's departure time.


> **INSTALL**

Change Directory to TrainNotification folder and run in the terminal the below :

pip install -r requirements.txt


> **Run in the background**

pythonw.exe .\main.py
