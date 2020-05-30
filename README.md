# COVIDcatch

A catching isolation-inspired videogame made in Python using the Pygame libraries as part of the [OxfordHack](https://oxfordhack.co.uk/) Digithon 2020.
---

## Gameplay Rules

Your **goal** as the player is to achieve the highest score possible!

You control a set of hands (or masked face, depending on player selection) that moves horizontally across the screen, catching any falling objects that land in its grasp.

Catch a *mask*, *hand sanitizer* or *pair of gloves* and your score will **increase by 1!**.
However, catch a *virus* or *<2m sign* and the two people on each side of the screen will move a step closer to each other!

Let them get too close and it'll be **GAME OVER!**

Play against your friends, or even yourself, with an integrated score board that tracks the highest scores in a given session.
---

## Startup Instructions

Ensure the latest version of Python (Python3.8+) is installed.

Install Pygame libraries:
`python -m pip install -U pygame --user`

Ensure you're in the project directory:
`python ./covidcatch.py`

*It's as simple as that!*
