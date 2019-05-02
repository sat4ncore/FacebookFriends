# Friends Parser

## The program gets a list of friends on Facebook with their links.

Friends parser uses Selenium Web Driver for simulating browser actions, 
logging in to Facebook and getting a list of friends.

## Getting started

First of all, DON’T PANIC. 
It will take 2 minutes to get the gist of what Friends Parser is all about.

#### Requirements

##### Python

You need to have a recent version of Python installed. 
See the [Python](python.org) page for actual information.

To work with RabbitMQ and MySQL, you must also install additional Python modules using the command: 

```bash
python3 -m pip install -r requirements.txt
```

######  Selenium

The project uses Selenium and the driver for Firefox browser.
Please download the [driver](github.com/mozilla/geckodriver/releases) 
and transfer the executable file to the path /usr/local/bin on Linux.
[Instruction for Windows](seleniumhq.github.io/selenium/docs/api/py)

#### Running

An example of running the program:

```bash
python3 program.py login password
```

After completing all the actions, the program will display a list of friends with their links.

