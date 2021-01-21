[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [](http://lbesson.bitbucket.org/) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/) [![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Naereen/badges)  [![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)
<p align="center">
  <img width="60%" src="res/logo.png">
</p>

#  Techstars challenge

> **(Schedule mentors and companies during the day.)**

Techstars challenge is one way to solve a scheduling problem by automating the matching section by using human logic.

<p style="font-size:25px; font-weight:bold"> 
<img style="display: inline-block;" src="/res/intro.png">
</p>
</center>

This project considers that a .csv file is generated that contains the information about the mentor, time, and the companies that the mentor has to work with, in any case, that any mentor hasn't booked the time slot yet, an option to add them later is visible on the app.

### Team 🎮

 [David Orejuela](https://github.com/daorejuela1) <br>  Software Developer|
| -------------- |
 ![David Orejuela](res/David.jpg)
| <a href="https://twitter.com/DavidOrejuela14" ><img style="display: inline-block;" src="res/twitter.png" width="35px"></a> &nbsp;<a href="https://www.linkedin.com/in/davidorejuela14/" ><img style="display: inline-block;" src="res/linkedin.png" width="42px"></a> <a href="https://medium.com/@daorejuela1" ><img style="display: inline-block;" src="res/medium.png" width="35px"></a>|

## Motivation 🏋

This software is a 3-day challenge created to grasp the rhythm of creating solutions in a quickly changing environment.

## Main logic 🧠

If we have to schedule in a calendar, what would be the basic logic to do it? this is the step by step:

 1. We generate the time lapses
 2. We scan for mentor collapses
	 3. If the mentor we want to input is not in the time-lapse, we continue.
	 4. If the mentor is already on the time slot we increase the offset into the next time slot
 3. We scan for company collapses
	 4. If the company is not there we match the company and the mentor together
	 5. If the company is already there we search for another company with that specific mentor that can be put in place

Finally, if we can assign all the companies we know that every match has been correctly applied, there may be algorithms with better time and spatial complexity, but as the input contains (75 mentors * 10 companies) the algorithm will perform quickly.

Having in mind that we know that every session is going to have **20 minutes** we start by considering that the day is starting from 8:00 - 11:59, let's check it with an example.

Considere that we have to match this 3 mentors with these 5 companies:

| Name | Day |AM/PM | Company| Company2|Company3|
|--|--|--|--|--|--|
|Aaron Schram  | Monday | AM | Avengers Inc | Pied Piper |SHIELD|
|Jackson Carson  | Monday | AM | Avengers Inc | Pied Piper |Justice League|
|Nick Hofmeister  | Undefined | Undefined| Avengers Inc | Pied Piper|

 1. Let's create our schedule template for Monday morning:
 ![Schedule template](/res/schedule_template.png)
	
 2. Add a space call [Break time] for mentors with less than 6 companies
  ![Schedule braks](/res/schedule_breaks.png)
 3. Start by adding the first mentor in a way that he doesn't manage two companies at the same time
 ![Schedule braks](/res/schedule_1mentor.png)
 4. Add the second mentor, as we can see Avengers is already at 8:00 A.M so what we do is rotate in the list of companies to the next available, that would be Pied Piper, and then we continue with the normal list.
 ![Schedule breaks](/res/schedule_2mentors.png)
 5. Let's suppose that we want to book Nick into the Monday morning group, as we notice both companies are in the time slot of the 8:00 A.M, so we have to search in the next available slot, that would be 8:40 A.M
 ![Schedule breaks](/res/schedule_3mentors.png)

By applying this logic the software automatically organize mentors with companies 1:1.

## Code style 👓


Pep8 ☞ [![Betty](https://badgen.net/badge/Python3/pep8/green?icon=github)](https://www.python.org/dev/peps/pep-0008/)

## Demo📷
<center>

## Loading example.csv
<p style="font-size:25px; font-weight:bold"> 
<img style="display: inline-block;" src="/res/example.gif">
</p>

--------------

## Loading default .csv
<p style="font-size:25px; font-weight:bold">
<img style="display: inline-block;" src="/res/default.gif">
</p>

---

## Tech used 🛠

![Django](res/python-django.png)

 - This problem could be solved by applying logic to the spreadsheet but I chose python since it gives more control to add new features in the future, like login
 - Django was used to handle the python logic since it automates the folder structure, which makes development faster

A Web app was preferred over a Desktop App, since a desktop App depends on the O.S of the user, while with a Web app while the user has a compatible browser (Not Internet Explorer) it will work.






## Requirements 📚

- Ubuntu 18.04+
- Python 3.6
- Django 2.3+

## Installation & Init 📖

Please make sure that you have installed the essentials before cloning:

```
sudo apt-get install python3-pip
```

1. Clone the repository: `git clone https://github.com/daorejuela1/techstars-challenge`
2. Go to the folder: `cd techstars-challenge`
3. Install requirements `pip3 install requirements.txt`
4. Run the server: `python3 manage.py runserver`

## Usage 💪

Get into the URL `127.0.0.1:8000` to start the web app, and provide a .csv file (If you don't have a .csv file just click upload and the default  .csv file will be used)

You can check by day the match between mentors and companies, if you want to add an unbooked mentor go to the bottom of the page select the name, time, and click the Book button.

## Features 📜
 
 ### Automate Match
 

 - The software will avoid collisions when matching

### Book

 - You can book mentors with the form at the bottom of the page

### Data search

 - If you need to search for an specific mentor or company in one day you can use the search field above the table

## Live 🧍



To check the usable software clic [here](https://techstars-challenge.herokuapp.com) 

## Related projects 💼

Here are some awesome projects I have been working on:

|[Mastermind Hackday Project](https://github.com/daorejuela1/mastermind)| [Daily tweet](https://github.com/daorejuela1/daily_tweet) | [Monty bytecode decoder](https://github.com/daorejuela1/monty) | [Serpent Algorithm](https://github.com/daorejuela1/serpent) | [Custom Shell v1](https://github.com/daorejuela1/simple_shell)
|--|--|--|--|--|
| ![Monty project](https://user-images.githubusercontent.com/55990484/93660905-3fd0db00-fa19-11ea-97db-fb3c0169cb4c.gif) | ![Tweet daily](/res/tweet_daily.png) | ![Monty](/res/Monty.jpg) | ![Serpent](/res/serpent.png) | ![Shell](https://user-images.githubusercontent.com/59972435/79511929-ec8bd400-8005-11ea-9361-c97aaccc0607.jpg) |

## Credits ✈

Special thanks to [Techstars.com](techstars.com/) for letting me be part of this awesome challenge.
