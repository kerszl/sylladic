# Sylladic

![Screenshot](github-img/program.png)

## Table of contents
* [General info](#general-info)
* [Platforms](#platforms)
* [Technologies](#technologies)
* [Setup](#setup)
* [Docker](#docker)
* [How to use](#How-to-use)
* [Contact](#Contact)

## General info
Sylladic is a program which helps you to create dictionaries. A dictionary is made up of words and converted into syllables (thanx 4 great pyphen library) 


Why I made it?

I forgot a password, but I know it was non-dictionary and consisted of Polish syllables. This word was not in the regular dictionary. Unfortunately, I couldn't find the syllable dictionary, so I wrote a program to create it. When you create the dictionary, you can multiply syllables and other chars from file. 

## Platforms
Windows, Linux 

## Technologies
* Python 3.6.x (on the lower version the program does not work well)
* UTF-8 (it did not work well for others locales)

## Libraries
Project is created with great libraries:

* Pyphen 
* Tqdm
* Pathlib
* Argparse
* Itertools


	
## Setup
To run this project, download and install it locally: (Ubuntu)
```
$ sudo apt install python3
$ sudo apt install python3-pip
$ git clone https://github.com/kerszl/sylladic
$ cd sylladic
$ pip3 install -r requirements.txt
$ chmod +x sylladic.py
```
## Docker
```
wget https://raw.githubusercontent.com/kerszl/sylladic/master/Dockerfile
docker build . -t sylladic:alpine
docker run -ti --rm sylladic:alpine /bin/bash
```

## How to use
When you want create syllables from dictionary:
```
$ ./sylladic.py -d dict/dic.sample.pl.txt pl
```
* dic.sample.pl.txt - file with dictionary
* pl - contry code

![Screenshot](github-img/syll.png)

When you want multiply syllables or other chars:
```
$ ./sylladic.py -m digits.txt 4
```
* digits.txt - file to multiply chars
* 4 - how many times multiply

![Screenshot](github-img/mul.png)

You can see simple iterations graph:
```
$ ./sylladic.py -g
```
![Screenshot](github-img/iterations.png)
## Contact
![Screenshot](github-img/contact.png)
