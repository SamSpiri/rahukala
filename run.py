#! /usr/bin/env python
# -*- coding: utf-8 -*-

from Sun import Sun
from datetime import timedelta, date, datetime
import uuid

def forceRange( v, max ):
  # force v to be >= 0 and < max
  if v < 0:
    return v + max
  elif v >= max:
    return v - max

  return v

def hm(UT):
  hr = forceRange(int(UT), 24)
  min = round((UT - int(UT))*60,0)
  return [hr,min]


#coords = {'latitude' : 55.760185, 'longitude' : 37.615638 }
coords = {'latitude' : 51.5078636, 'longitude' : 7.4002233 }

#TIMEZONE = 3
#TIMEZONE = 1

sun = Sun()


def daterange(start_date, end_date):
  for n in range(int ((end_date - start_date).days)+1):
    yield start_date + timedelta(n)

#start_date = date(2019, 1, 1)
#end_date = date(2019, 12, 31)
start_date = date(2020, 11, 1)
end_date = date(2020, 12, 31)

date = datetime.now()
gy = int(date.strftime("%Y"))
gm = int(date.strftime("%m"))
gd = int(date.strftime("%d"))

print "BEGIN:VCALENDAR"
print "PRODID:calendar-201901"
print "VERSION:2.0"

for single_date in daterange(start_date, end_date):
  #print single_date.strftime("%Y-%m-%d")

  dy = int(single_date.strftime("%Y"))
  dm = int(single_date.strftime("%m"))
  dd = int(single_date.strftime("%d"))

  sunrise = sun.getSunriseTime( coords, single_date )['decimal']# + TIMEZONE
  sunset = sun.getSunsetTime( coords, single_date )['decimal']# + TIMEZONE
  daylong = sunset - sunrise
  #print daylong
  hora = daylong/8
  #print hm(hora)
  #print hm(sunrise)


  print "BEGIN:VEVENT"
  print "UID:"+uuid.uuid4().hex+"@rahukaal.spiridonov.simon"
  print "CLASS:PUBLIC"
#  print "DESCRIPTION:Quiet hour (Rahu Kaal)"
  print "DTSTAMP;VALUE=DATE-TIME:%d%02d%02dT090000" % (gy,gm,gd)

  #print single_date.weekday()
  if single_date.weekday() == 0:
    [sh,sm] = hm(sunrise + hora)
    [eh,em] = hm(sunrise + hora*2)
  if single_date.weekday() == 1:
    [sh,sm] = hm(sunrise + hora*6)
    [eh,em] = hm(sunrise + hora*7)
  if single_date.weekday() == 2:
    [sh,sm] = hm(sunrise + hora*4)
    [eh,em] = hm(sunrise + hora*5)
  if single_date.weekday() == 3:
    [sh,sm] = hm(sunrise + hora*5)
    [eh,em] = hm(sunrise + hora*6)
  if single_date.weekday() == 4:
    [sh,sm] = hm(sunrise + hora*3)
    [eh,em] = hm(sunrise + hora*4)
  if single_date.weekday() == 5:
    [sh,sm] = hm(sunrise + hora*2)
    [eh,em] = hm(sunrise + hora*3)
  if single_date.weekday() == 6:
    [sh,sm] = hm(sunrise + hora*7)
    [eh,em] = hm(sunrise + hora*8)
  print "DTSTART;VALUE=DATE-TIME:%d%02d%02dT%02d%02d00Z" % (dy,dm,dd,sh,sm)
  print "DTEND;VALUE=DATE-TIME:%d%02d%02dT%02d%02d00Z" % (dy,dm,dd,eh,em)
#  print "LOCATION:Dortmund, Germany"
  print "SUMMARY;LANGUAGE=en-us:Quiet hours"
  print "TRANSP:OPAQUE"
  print "END:VEVENT"



#   print "BEGIN:VEVENT"
#   print "UID:"+uuid.uuid4().hex+"@rahukaal.spiridonov.simon"
#   print "CLASS:PUBLIC"
# #  print "DESCRIPTION:Quiet hour (Rahu Kaal)"
#   print "DTSTAMP;VALUE=DATE-TIME:%d%02d%02dT090000" % (gy,gm,gd)
#
#   #print hm(sunset)
#   #print hm(sunset + hora)
#   [sh,sm] = hm(sunset)
#   [eh,em] = hm(sunset + hora)
#
#   print "DTSTART;VALUE=DATE-TIME:%d%02d%02dT%02d%02d00Z" % (dy,dm,dd,sh,sm)
#   print "DTEND;VALUE=DATE-TIME:%d%02d%02dT%02d%02d00Z" % (dy,dm,dd,eh,em)
# #  print "LOCATION:Dortmund, Germany"
#   print "SUMMARY;LANGUAGE=en-us:quiet h2"
#   print "TRANSP:OPAQUE"
#   print "END:VEVENT"

print "END:VCALENDAR"
