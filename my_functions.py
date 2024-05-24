import pandas as pd

def read_activity_data():
    #load data
    activity_data = pd.read_csv('activity.csv', usecols=["Duration", "PowerOriginal"])
    

    return activity_data


if __name__ == "__main__":
    activity_data = read_activity_data()
    