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


coords = {'longitude' : 37.615638, 'latitude' : 55.760185 }
TIMEZONE = 3

sun = Sun()


def daterange(start_date, end_date):
  for n in range(int ((end_date - start_date).days)+1):
    yield start_date + timedelta(n)

#start_date = date(2019, 1, 1)
#end_date = date(2019, 12, 31)
start_date = date(2019, 2, 10)
end_date = date(2019, 2, 28)

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

  sunrise = sun.getSunriseTime( coords, single_date )['decimal'] + TIMEZONE
  sunset = sun.getSunsetTime( coords, single_date )['decimal'] + TIMEZONE
  daylong = sunset - sunrise
  #print daylong
  hora = daylong/8
  #print hm(hora)
  #print hm(sunrise)


  print "BEGIN:VEVENT"
  print "UID:"+uuid.uuid4().hex+"@rahukala.spiridonov.semion"
  print "CLASS:PUBLIC"
  print "DESCRIPTION:Постарайтесь не планировать важные дела на этот временной промежуток."
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
  print "DTSTART;VALUE=DATE-TIME:%d%02d%02dT%02d%02d00" % (dy,dm,dd,sh,sm)
  print "DTEND;VALUE=DATE-TIME:%d%02d%02dT%02d%02d00" % (dy,dm,dd,eh,em)
  print "LOCATION:Москва, Россия"
  print "SUMMARY;LANGUAGE=en-us:Раху Кала неблагоприятное время"
  print "TRANSP:OPAQUE"
  print "END:VEVENT"



  print "BEGIN:VEVENT"
  print "UID:"+uuid.uuid4().hex+"@rahukala.spiridonov.semion"
  print "CLASS:PUBLIC"
  print "DESCRIPTION:Постарайтесь не планировать важные дела на этот временной промежуток."
  print "DTSTAMP;VALUE=DATE-TIME:%d%02d%02dT090000" % (gy,gm,gd)

  #print hm(sunset)
  #print hm(sunset + hora)
  [sh,sm] = hm(sunset)
  [eh,em] = hm(sunset + hora)

  print "DTSTART;VALUE=DATE-TIME:%d%02d%02dT%02d%02d00" % (dy,dm,dd,sh,sm)
  print "DTEND;VALUE=DATE-TIME:%d%02d%02dT%02d%02d00" % (dy,dm,dd,eh,em)
  print "LOCATION:Москва, Россия"
  print "SUMMARY;LANGUAGE=en-us:Раху Кала после заката неблагоприятное время"
  print "TRANSP:OPAQUE"
  print "END:VEVENT"

print "END:VCALENDAR"
