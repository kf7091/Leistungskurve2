import pandas as pd

def read_activity_data():
    '''
    returns a pandas dataframe with the activity data from the activity.csv file
    '''

    #load data
    activity_data = pd.read_csv('activity.csv', usecols=["Duration", "PowerOriginal"])

    activity_data.at[0, "Time"] = 0
    for i in range(1, len(activity_data)):
        activity_data.at[i, "Time"] = activity_data["Duration"][i] + activity_data["Time"][i-1]
    return activity_data


if __name__ == "__main__":
    activity_data = read_activity_data()
    print(activity_data)