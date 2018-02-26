[![Build Status](https://travis-ci.org/Frazl/DCU-Timetable-Scraper.svg?branch=master)](https://travis-ci.org/Frazl/DCU-Timetable-Scraper) [![Maintainability](https://api.codeclimate.com/v1/badges/e77e7906a9e080dba93d/maintainability)](https://codeclimate.com/github/Frazl/DCU-Timetable-Scraper/maintainability)

## Description 

This program/module scrapes DCU's timetable and returns information based on the day, course and time. 

This program is intented to be used as a module. Although it does run standalone it was designed to be used in conjunction with a Facebook messenger bot.

This program was made using **Python 3.6.4**

## Dependencies

BeautifulSoup 4 is required and is obtainable through pip.

```
pip install beautifulsoup4
```

### Module Usage

This program uses requests, BeautifulSoup 4 and warnings.

## Guide

### Quickstart

Install dependencies listed above if not already installed.

Import bs4dcu into your own script. 

Call the run function like the example below

```
bs4dcu.run("mon", "10:00", "CA", "1")
```

### Functions

### run

#### Description

Run is the main function of this program.

Run returns either two things, a dictionary or a list(if no time specified).

If run returns a dictionary the keys are the times. 
````
(times.keys()) 
````

If run returns a list, a time has been given and the list will contain the possible modules on at that time. *Note that more than one module can be on at once with optional modules for courses and week dependent modules.*

e.g. Return for a list 

```
run("Thu","11:00", "CA", "1")

['Digital Innovation Management and Enterprise In GLA.L125, GLA.L128 With Ward M', 'Digital Innovation Management and Enterprise In GLA.QG15 With ANOTHER for MW']
```

#### Usage

```
run(day, time, code, year)
````
day: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

time (optional): 24hr format only takes the hour or half hour currently. 

e.g 17:00 and 14:30 but *not 14:31*

code (optional): Module code, e.g. CA = Computer Applications, AF = Accounting Finance 

Year(optional): The year code for the module, e.g. 1,2,3,4 (Must be in string format)

*Note: code defaults to CA if none entered and year defaults to 1*

### next

#### Description

Next runs run(day, time, code) with the current time and day and can return two things similiar to run.

If it is past 5:30PM next will return the timetable for tomorrow in the form of a dictionary with keys time.keys()

If it is before 5:30pm it will return a list of what is due to be on in the next hour. 

e.g. If it is currently 10AM it will see what is on at 11AM and send that back. 

#### Usage

```
next(code, year)
```

code(optional): Module code, e.g. CA = Computer Applications, AF = Accounting Finance

year(optional): The year code for the module, e.g. 1,2,3,4 (Must be in string format) 

*Note: code defaults to CA if none entered and year defaults to 1*


### beautify

#### Description

Beautify takes data i.e a list or dictionary and prints it out nicely. 

The main function of this is for testing and for standalone functionality.

e.g. beautify(run("Mon","11:00","AF", "1")) *More examples can be seen in the main() function // Run bs4dcu.py*

#### Usage 

```
beautify(datacontent)
```

datacontent: A list or dictionary - * Dictionary must be using keys times.keys() *

### responsehandler

#### Description

Takes in a list and returns neatly formatted text in the form of a string

### Usage

```
l = run("Mon","11:00","CA","1")
s = responsehandler(l)
```

l: a list usually from run or next functions.

### dictionaryhandler

### Description

Returns neartly formatted text from a dictionary in the form of a string. Usually data should be from the run function.
If there is nothing on that day, i.e. the dictionary was empty then it returns the string "Nothing On Today".

### Usage

```
d = run("Fri",None,"CA","1")
s = dictionaryhandler(d)
OR
s = dictionaryhandler(run("Fri",None,"CA","1"))
```

d: A dictionary usally the result of run function.
## Contributors

### Seán Fradl (Fraz)

Please let me know if you found this useful and use it! Send me a message or something!
