def mph_and_minutes_to_miles(miles_per_hour , minutes_traveled):
    
    hours_traveled = minutes_traveled / 60.0
    miles_traveled = hours_traveled * miles_per_hour
    return miles_traveled
