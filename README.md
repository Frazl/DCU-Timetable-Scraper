## Description 

This program/module scrapes DCU's timetable and returns information based on the day, course and time. 

This program is intented to be used as a module. Although it does run standalone it was designed to be used in conjunction with a facebook messenger bot.

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
bs4dcu.run("mon", "11:00", "CA")
```

### Functions

### Run

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
run("Thu","11:00")

['Digital Innovation Management and Enterprise In GLA.L125, GLA.L128 With Ward M', 'Digital Innovation Management and Enterprise In GLA.QG15 With ANOTHER for MW']
```

#### Usage

```
run(day, time, code)
````
day: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

time (optional): 24hr format only takes the hour or half hour currently. 

e.g 17:00 and 14:30 but *not 14:31*

code (optional): Module code, e.g. CA = Computer Applications, AF = Accounting Finance 

*Note: code defaults to CA if none entered*

### next

#### Description

next runs run(day, time, code) with the current time and day and can return two things similiar to run.

If it is past 5:30PM next will return the timetable for tomorrow in the form of a dictionary with keys time.keys()

If it is before 5:30pm it will return a list of what is due to be on in the next hour. 

e.g. If it is currently 10AM it will see what is on at 11AM and send that back. 

#### Usage

```
next(code)
```

code(optional): Module code, e.g. CA = Computer Applications, AF = Accounting Finance 

*Note: code defaults to CA if none entered*

## Contributors

### Seán Fradl (Fraz)

Please let me know if you found this useful and use it! Send me a message or something!
