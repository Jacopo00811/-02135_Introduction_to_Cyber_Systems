# 02135_Introduction_to_Cyber_Systems
Material for the course 02135 Introduction to Cyber Systems (Spring 22) at DTU.

## Assignments Presentation
This repository contains four different assignments completed as part of a course. Below is a brief description of each assignment.

## Assignment 1: Implementation of an FSMD Simulator in Python
This assignment requires implementing a cycle-based simulator for Finite State Machines with Datapath (FSMDs) in Python. The simulator should take input files specifying the description of the FSMD and the environment around it, and output the state of the variables at the end of the simulation. It should accept a maximum number of cycles to run and be able to handle input from external environment.

## Assignment 2: ISA Simulator Implementation in Python
This assignment requires implementing an instruction-set architecture (ISA) simulator for a simple processor in Python, which executes machine language commands. The simulator should be cycle-based and accept input arguments such as the number of cycles to run, program file, and data memory file. The structure of these files and expected output is also explained in the assignment.

## Assignment 3: Getting Started with the Huzzah32 board and with MicroPython
This assignment involves programming an embedded computer and controlling various I/O devices using MicroPython. There are 5 mandatory tasks which include blinking a red LED with a button, cyclically lighting 3 LEDs with a button press, controlling the LEDs with temperature sensor input, using Neopixel LEDs with temperature sensor input, and controlling the intensity of light of the two Neopixel LEDs with a potentiometer. The tasks involve using different resources such as resistors, GPIO pins, temperature sensor MCP9808, and analog input from a potentiometer.

## Assignment 4: IoT Node Implementation using Huzzah32 - ESP32 WiFi board and MicroPython
This assignment requires building a simple server with the Adafruit Feather Huzzah32 – ESP32 WiFi board, that provides a web server and API to control the board I/Os, demonstrating the workings of IoT devices. The program sets up the board as a WiFi access point and starts a simple Web server (HTML based) that reports the status of the board pins. The students also need to add lines to the web-table to show the status of the inputs and sensors set up in the previous assignment.
