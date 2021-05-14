# Sylladic

![Screenshot](program.png)

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Use](#use)

# Installation

## General info
Sylladic is a program which helps you to create dictionaries. A dictionary is made up of words and converted into syllables (thanx 4 great pyphen library) 
E.g. (word from Polish dictionary): word = abolicjonistyczną, syllab = abo-li-cjo-ni-stycz-ną

When you create the dictionary, you can multiply syllables and other chars from file. 

	
## Technologies
Project is created with:
* Python 3.x
* Pyphen library
* Tqdm library

	
## Setup
To run this project, download and install it locally:
```
$ sudo git clone https://github.com/kerszl/sylladic
$ cd sylladic
$ pip3 install -r requirements.txt
$ chmod +x sylladic.py
```

## Use
When you want create syllables from dictionary:
```
$ ./sylladic.py -d dic.sample.pl.txt pl
```
* dic.sample.pl.txt - file with dictionary (must be in "dict" directory)
* pl - contry code

![Screenshot](syll.png)

When you want multiply syllables or other chars:
```
$ ./sylladic.py -m digits.txt 4
```
* digits.txt - file to multiply chars
* 4 - how many times multiply

![Screenshot](mul.png)

You can see simple iterations graph:
```
$ ./sylladic.py -g
```
