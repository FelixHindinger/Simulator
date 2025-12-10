# Simulator

This repository contains a modified implementation of the mix network simulator proposed by Piotrowska (https://github.com/aniampio/Simulator).

The implementation is done using Python 3. 
Before running the code remember to make sure that you have all the dependencies installed.

To install the dependencies run

`pip3 install -r requirements.txt`

To run the simulator you need the command

`python3 playground.py`

You can change the parameters of the simulation in file `test_config.json`

The functionality of this simulator has only been tested for the stratified topology used in my thesis.
Measurements can only be taken for one traffic type per simulation run at the moment.
In order to take measurements for a configurations, the parameters for the traffic type that should be measured are put into the configuration file as values for the "_1"-parameters. 
