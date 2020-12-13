import time
import requests
import pytz
from plyer import notification # for getting notification on your PC
from journey_response import JourneyResponse
from datetime import datetime, tzinfo # for reading present date

def get_journey_data():
    journeyData = None
    response = None
    try:
        journeyData = requests.get("https://v5.vbb.transport.rest/journeys?from=900000058101&to=900000110005&&results=1")
        print("journeyData",journeyData)
    except:
        # if the data is not fetched.
        print("Something went wrong!")

    if (journeyData != None):
        # Converting data into JSON format
        data = journeyData.json()

        # Mapping json data to object .
        response = JourneyResponse(**data)

    return response


def get_time_difference(current_time, time_to_compare:str):

    # Convert from string to date.
    datetime_object = datetime.fromisoformat(time_to_compare)

    time_difference = datetime_object - current_time

    return time_difference


if __name__ == '__main__':

    # Current Time in Berlin.
    timezone = pytz.timezone('Europe/Berlin')
    berlin_now = datetime.now(timezone).replace(microsecond=0)

    # Repeat showing the Notification in a specific time of the day.
    while (17>berlin_now.hour>=16):
        response = get_journey_data()
        departure = response.journeys[0].legs[0].departure
        print("berlin_now           >>>>>", berlin_now)
        print("departure time       >>>>>", datetime.fromisoformat(departure))

        while (berlin_now < datetime.fromisoformat(departure)):

            time_difference = get_time_difference(berlin_now, departure)

            notification.notify(
                # title of the notification,
                title="Train is Leaving in :",
                # the body of the notification
                message="\n{time_difference} \nRoute time: {departure}".format(
                    time_difference=time_difference,
                    departure=departure
                    ),

                # Icon for the notification
                app_icon="Awicons-Vista-Artistic-1-Normal-Train.ico",
                # The notification stays for 70 sec
                timeout=500
            )
            # sleep for 1 min => 60 sec
            # notification repeats after every 4hrs
            time.sleep(60)

            # Current Time in Berlin.
            timezone = pytz.timezone('Europe/Berlin')
            berlin_now = datetime.now(timezone).replace(microsecond=0)
            print("time  now berlin           >>>>", berlin_now)

            response = get_journey_data()
            departure = response.journeys[0].legs[0].departure