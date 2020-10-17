# FactoryLocation
Finding the best location for a factory using an evolutionary algorithm (1+1) based on the location of resources

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Description](#description)

## General info
Project realised with [@ppawel11](https://github.com/ppawel11) for the subject Fundamentals of Artificial Intelligence on the Warsaw University of Technology. Our goal was to get familiar with some methods and algorithms of artificial intelligence and to use it in practise.

## Screenshots
![Screenshot1](./img/screenshot1.png)![Screenshot2](./img/screenshot2.png)

## Technologies
* Python 3.7
* cycler - version 0.10.0
* kiwisolver - version 1.1.0
* matplotlib  - version 3.1.2
* numpy - version 1.17.4
* pyparsing - version 2.4.5
* python-dateutil - version 2.8.1
* six - version 1.13.0
* tkinter (to draw a chart)

## Setup
First, to generate input (txt file with data: resources locations and some data necessary to calculate cost of the transport of the resource) you need to run `input_maker` typing: `python input_maker.py NUMBER_OF_RESOURCES` or `python3 input_maker.py NUMBER_OF_RESOURCES` for Python 3 where NUMBER_OF_RESOURCES should be `int` variable. Then you can run `main.py`. 

To generate a chart you need to install requirements from `requirements.txt` and have `tkinter` installed.

## Description
Program can be used to calculate where a factory should be built to keep resources transportation as low as possible. It produces a lot of initial "bees" with initial location. Then using 1+1 evolutionary algorithm it produces new generations of "bees" with changed (or the same if the cost after change would be higher) location. So we can say that "bees" explore the board looking for the best location of the factory. At the end the program chooses the best "bee" with the lowest cost of transportation.

You can verify the result using `chart.py` to generate a chart which shows the location of resources and their costs of transportation. 
