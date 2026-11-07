timetable = {
    101: {
        "name": "Chennai Express",
        "stops": [
            ("Chennai", "06:00", "06:15"),
            ("Katpadi", "08:00", "08:05"),
            ("Bangalore", "11:00", "11:15")
        ],
        "days": {"Monday", "Wednesday", "Friday"}
    },

    102: {
        "name": "Pandian Express",
        "stops": [
            ("Madurai", "05:00", "05:10"),
            ("Trichy", "07:00", "07:05"),
            ("Chennai", "10:00", "10:15")
        ],
        "days": {"Tuesday", "Thursday", "Saturday"}
    },

    103: {
        "name": "Kovai Express",
        "stops": [
            ("Chennai", "06:30", "06:40"),
            ("Salem", "09:00", "09:05"),
            ("Coimbatore", "11:00", "11:10")
        ],
        "days": {"Monday", "Tuesday", "Wednesday"}
    },

    104: {
        "name": "West Coast Express",
        "stops": [
            ("Chennai", "07:00", "07:10"),
            ("Katpadi", "09:00", "09:05"),
            ("Bangalore", "12:00", "12:10")
        ],
        "days": {"Friday", "Saturday", "Sunday"}
    },

    105: {
        "name": "Cholan Express",
        "stops": [
            ("Thanjavur", "05:30", "05:40"),
            ("Trichy", "07:30", "07:35"),
            ("Chennai", "11:30", "11:45")
        ],
        "days": {"Monday", "Thursday", "Sunday"}
    }
}

# Find trains stopping at a station on a given day
station = input("Enter station: ")
day = input("Enter day: ").capitalize()

result = []

for train_no, details in timetable.items():
    if day in details["days"]:
        for stop in details["stops"]:
            if stop[0].lower() == station.lower():
                result.append((train_no, details["name"], stop[1], stop[2]))

# Sort trains by departure time
result = sorted(result, key=lambda x: x[3])

print("\nTrains stopping at", station, "on", day)

if result:
    for train in result:
        print("Train No:", train[0],
              "| Name:", train[1],
              "| Arrival:", train[2],
              "| Departure:", train[3])
else:
    print("No trains available.")
