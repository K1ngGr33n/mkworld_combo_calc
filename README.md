# MKWorld Combo Calculator
This program takes in the data from a run (with ground type and coin changes) and **calculates the time** each combo in the game would need for **that exact path**.

Note: This program **cannot calculate** time differences from **Acceleration, Handling or Mini-Turbo**, it is meant strictly for the difference in **Speed.**

You can find my own test results in [this document.](https://docs.google.com/document/d/1vZDuUWTfXXjkFKGuCVNkZw4yabM3KSRRKyNxEDxHIqA/edit?tab=t.wq6qf5cgyyrz)

This program works for these MKWorld versions: **1.7.0; 1.8.0**

_Inspired by a similar project from [cypress](https://github.com/cypress-city)_

<hr>

## How to use

Note: you need to have [Python](https://www.python.org/downloads/) installed to run this program. I haven't tested the older versions, but it should work on Python 3.14 and above.

### Step 1: Clone the GitHub repo
Make sure you have **git** installed.
Find the directory where you want the program files to be, then open it in a terminal and run:
```
git clone https://github.com/K1ngGr33n/mkworld_combo_calc.git
```

### Step 2: Create a text file called "timings.txt"
#### Combo

The first line contains the combo used in the run. You must encode it using 2 numbers that represent the character and vehicle:

```4 3```
(example: Toadette / Baby Blooper.)
~~You can find all the numbers here: [INDEXLIST.md](INDEXLIST.md)~~ TODO: ADD THIS, FOR NOW GO INTO THE CHARACTER/VEHILCLE STATS CSV AND FIND THE NUMBER RIGHT NEXT TO YOUR CHARACTER/VEHICLE

#### Events

Next, you must add a timestamp for every event in the run. 
Every time the **ground type changes** or the run **collects a coin**, you need to log it on a new line (this includes the very start of the run).

Every line must be structured like this: ```0:00.000 a```

The first part is the **timestamp of the event.** You can simply use the in-game timer for this.
The second part is a **tag** that marks the event. You can look them up in this list:
```
r - Road (Concrete, Wood, Asphalt...)
t - Terrain (Mud, Sand, Dirt... (NOT offroad))
w - Water (Places where your kart becomes a jetski, and sometimes shallow water)
g - Gliders

c - Coin collection

o - Offroad
rl - Rails
wl - Walls
x - None (Cannon Gliders)

h - item hit or respawn (-3 coins)
sh - shock hit (-2 coins)

e - End of the run
```

You can use ```#``` at the start of a line to skip that line. This can be used for comments. 
Putting the comment after the event will not ignore the line.
```
1:12.546 r
# lap 3     <-- this line will be ignored 
1:14.567 t
1:20.242 c # new strat    <-- this line will not be ignored
```

#### Ending
You must encode the **final time** of the run. **Use the tag "e"**: ```1:54.655 e```

Placing this in the middle of your file will ignore all lines below: 
```
1:50.130 r
2:01.009 e  <-- end
2:02.426 t  |
2:04.235 r  |   <-- program will skip these lines 
2:05.635 e  |
```


#### Final Result
After you are done, your file should look like this:
```
4 11
0:00.000 r
0:02.740 c
0:03.083 r
# comment 1
0:04.483 w
0:07.483 o
0:08.416 r # comment 2

...

1:54.665 e
```

### Step 3: Run the Script
Make sure your text file is in the **same directory** as the ```main.py``` file. Then **simply run** ```main.py```.

The result of the calculation will be a file called ```"results.txt"```, located in the same directory.
