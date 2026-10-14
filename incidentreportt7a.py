north_dc = [45, 30, 120, 15]   # downtime minutes per incident
south_dc = [60, 10, 25]

print("North DC total downtime:", sum(north_dc))
print("South DC total downtime:", sum(south_dc))
print("Most recent North DC incident:", north_dc[-1])

while True:
    entry = input("Log a new North DC incident (minutes): ")
    try:
        minutes = int(entry)
        if minutes < 0:
            print("Downtime can't be negative. Try again.")
            continue
        break
    except ValueError:
        print("Please enter a whole number of minutes.")

north_dc.append(minutes)
print("New North DC total:", sum(north_dc))

def calculate_total(minutes_list):
    total = 0
    for m in ______:
        total = total + m
    return ______

print("North DC total downtime:", calculate_total(north_dc))
