north_dc = [45, 30, 120, 15]   # downtime minutes per incident
south_dc = [60, 10, 25]

print("North DC total downtime:", sum(north_dc))
print("South DC total downtime:", sum(south_dc))
print("Most recent North DC incident:", north_dc[-1])

north_dc.append(int(input("Log a new North DC incident (minutes): ")))
print("New North DC total:", sum(north_dc))

