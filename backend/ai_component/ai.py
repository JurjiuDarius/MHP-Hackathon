import pickle
from datetime import datetime
from numpy import loadtxt
def get_day_of_week_numeric(date_str):
    # Convert the string to a datetime object
    date_object = datetime.strptime(date_str, '%d/%m/%Y')
    # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    day_of_week_numeric = date_object.weekday()
    return day_of_week_numeric

workspace_data = loadtxt('hackathon-schema.csv', delimiter=",", skiprows=1, dtype=str)

# desks = np.zeros(135)
desks = {}
number_days = 0

for row in workspace_data[:, :]:
    if row[3] == 'TRUE':
        deskweek = row[1] + " " + str(get_day_of_week_numeric(row[2]))
        if deskweek not in desks:
            desks[deskweek] = 0
        desks[deskweek] += 1

good_preds_count=0
sorted_desks = sorted(desks)

for desk in sorted_desks:
    print(desk, desks[desk]/13)

for key, value in desks.items():
    print(key, value)

correct_guesses = 0

for row in workspace_data[:, :]:
    deskweek = row[1] + " " + str(get_day_of_week_numeric(row[2]))
    if desks[deskweek]/13 >= 0.5:
        if row[3] == "TRUE":
            correct_guesses += 1
    else:
        if row[3] == "FALSE":
            correct_guesses += 1

pickle.dump(desks, open("models/desks-morning.pickle", "ab"))

print(f"Accuracy morning: {correct_guesses/workspace_data.shape[0]}")

desks = {}
for row in workspace_data[:, :]:
    deskweek = row[1] + " " + str(get_day_of_week_numeric(row[2]))
    if row[4] == 'TRUE':
        if deskweek not in desks:
            desks[deskweek] = 0
        desks[deskweek] += 1

good_preds_count=0
print(desks)
sorted_desks = sorted(desks)

for desk in sorted_desks:
    print(desk, desks[desk]/65)

correct_guesses = 0

for row in workspace_data[:, :]:
    deskweek = row[1] + " " + str(get_day_of_week_numeric(row[2]))
    if desks[deskweek]/13 >= 0.5:
        if row[4] == "TRUE":
            correct_guesses += 1
    else:
        if row[4] == "FALSE":
            correct_guesses += 1

pickle.dump(desks, open("models/desks-evening.pickle", "ab"))

print(f"Accuracy evening: {correct_guesses/workspace_data.shape[0]}")
#

print(f"Decent predicitons are{good_preds_count}, of {len(desks)}")

days = {}

for row in workspace_data[:, :]:
    if get_day_of_week_numeric(row[2]) not in days:
        days[get_day_of_week_numeric(row[2])] = 0
    if row[3] == 'TRUE':
        days[get_day_of_week_numeric(row[2])] += 1


sorted_days = sorted(days.items(), key=lambda x:x[1])


for key, value in days.items():

    print(key, value)


print("##############################")
for day in sorted_days:

    print(day[0], days[day[0]])

