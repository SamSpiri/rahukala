from Sun import Sun

coords = {'longitude' : 37.615638, 'latitude' : 55.760185 }

sun = Sun()

# Sunrise time UTC (decimal, 24 hour format)
print sun.getSunriseTime( coords )['hr']+3
print sun.getSunriseTime( coords )['min']


# Sunset time UTC (decimal, 24 hour format)
print sun.getSunsetTime( coords )['decimal']+3
