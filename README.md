# MKWorld Combo Calculator
This program takes in the data from a run (with ground type and coin changes) and **calculates the time** each combo in the game would need for **that exact path**.

Note: This program **cannot calculate** time differences from **Acceleration, Handling or Mini-Turbo**, it is meant strictly for the difference in **Speed.**

<hr>

## How to use
### Step 1: Clone the GitHub repo
Make sure you have **git** installed.
Find the directory where you want the program files to be, then open it in a terminal and run:
```
git clone https://github.com/K1ngGr33n/mkworld_combo_calc.git
```

### Step 2: Create a text file called "timings.txt"
#### Combo

The first line contains the combo used in the run. You must encode it using 2 numbers that represent the character and vehicle:

```4 11```
<sup>(example: Toadette / Baby Blooper.)</sup>
~~You can find all the numbers here: [INDEXLIST.md](INDEXLIST.md)~~ TODO: ADD THIS

#### Events

Next, you must add a timestamp for every event in the run. 
Every time the **ground type changes** or the run **collects a coin**, you need to log it on a new line (this includes the very start of the run).

Every line must be structured like this: ```0:00.000 a```

The first part is the **timestamp of the event.** You can simply use the in-game timer.
The second part is a **letter** that stands for the event, which you can look up in this list:
```
r - Road (Concrete, Wood, Asphalt...)
t - Terrain (Mud, Sand, Dirt... (NOT offroad))
w - Water (Places where your kart becomes a jetski, and sometimes shallow water)

n - Neutral (Rails, Walls and Gliders)
o - Offroad

x - None (Cannon Gliders)
e - End of the run
```

#### Ending
You must encode the **final time** of the run at the very end. Use the **letter "e"** here: ```1:54.655 e```

<br>

After you have done all of these steps, your file should look like this:
```
4 11
0:00.000 r
0:02.740 c
0:03.083 r
0:04.483 w
0:07.483 o
0:08.416 r
...
1:54.665 e
```

### Step 3: Run the Script
Note: you must have the libraries **numpy** and **pandas** installed. If you do not, you need to install them:
```
pip install numpy
pip install pandas
```

Make sure your text file is in the **same directory** as the ```main.py``` file. If that is the case, **simply run** ```main.py```, and wait a few seconds.

The result of the calculation will be a file called ```"results.txt"```, located in the same directory.