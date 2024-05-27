import pandas as pd

def read_activity_data():
    '''
    returns a pandas dataframe with the activity data from the activity.csv file in working directory
    '''

    #load data
    activity_data = pd.read_csv('activity.csv', usecols=["Duration", "PowerOriginal"])

    # create absolute time
    activity_data.at[0, "Time"] = 0
    for i in range(1, len(activity_data)):
        activity_data.at[i, "Time"] = activity_data["Duration"][i] + activity_data["Time"][i-1]
    return activity_data


def create_powercurve(power_data: list, time: list):
    '''
    returns a pandas dataframe with the power curve data

    power_data: list with the power data
    time: list with the time data

    power_data and time must have the same length
    '''

    power_levels = []
    durations = []

    # check time for powervalues in 10W steps and save maximum value
    for power_level in range(0, int(power_data.max()), 10):

        start = None
        end = None
        current_durations = [0]

        for index in range(len(power_data)):
            if power_data[index] > power_level and start == None:
                start = time[index]
            elif power_data[index] <= power_level and start != None:
                end = time[index]
                current_durations.append(end - start)
                start = None
                end = None
        
        power_levels.append(power_level)
        durations.append(max(current_durations))

    return pd.DataFrame({"Duration": durations, "Power": power_levels})


# for testing
if __name__ == "__main__":
    activity_data = read_activity_data()
    print(activity_data)
    power_curve = create_powercurve(activity_data["PowerOriginal"], activity_data["Time"])
    print(power_curve)