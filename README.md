# 🍎 Fruit Catcher

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pygame](https://img.shields.io/badge/Pygame-Game%20Engine-red)
![Status](https://img.shields.io/badge/Status-Completed-green)

> **Course Project:** Introduction to Computer Engineering  
> **University:** Da Nang University of Science and Technology (DUT)

## 📖 Introduction

**Fruit Catcher** is a fun arcade-style game built with Python and the Pygame library. Players control a bucket to catch falling fruits, accumulate scores, and survive through increasingly difficult levels.

This project demonstrates fundamental game development concepts, including collision detection, state management, game loops, and software packaging using PyInstaller.

## 🚀 Key Features

* **4 Seasons System:** The background environment changes dynamically based on the score (Spring, Summer, Autumn, Winter).
* **Special Items:**
    * 🍌 **Banana:** Restores 1 life (Max 5 lives).
    * 🍎 **Apple:** Activates a **Shield** for 3 seconds (blocks bombs).
    * 💣 **Bomb:** Decreases life if caught (unless the shield is active).
* **Visual Effects:** Floating text for scores/damage and visual indicators for the shield status.
* **Progressive Difficulty:** Falling speed and fruit spawn rate increase as you level up.
* **Audio:** Background music and sound effects for interactions (scoring, damage, game over).

## 🛠️ Tech Stack

* **Language:** Python
* **Core Library:** Pygame (Graphics and Audio)
* **Packaging:** PyInstaller (Executable creation)

## ⚙️ Installation & Usage

### Option 1: Run from Source Code

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/DUTVcore/Game_baitapnhapmonnganh.git](https://github.com/DUTVcore/Game_baitapnhapmonnganh.git)
    cd Game_baitapnhapmonnganh
    ```

2.  **Install dependencies:**
    Ensure Python is installed, then run:
    ```bash
    pip install pygame
    ```

3.  **Run the game:**
    ```bash
    python game.py
    ```

### Option 2: Run Executable (Windows)

If you have built the project or downloaded the release, simply open `game.exe` in the `dist` folder to play without installing Python.
*(The `game.spec` configuration file is included for packaging resources)*.

## 🎮 How to Play

* **Controls:** Use the **LEFT** (⬅️) and **RIGHT** (➡️) arrow keys to move the bucket.
* **Rules:**
    * Catch normal fruits: +1 Point.
    * Catch Bananas: Heal +1 Heart.
    * Catch Apples: Activate Shield (Temporary Invincibility).
    * Avoid Bombs: Touching a bomb costs 1 life.
    * Do not let fruits hit the ground (You lose a life if you miss).
    * **Game Over** when you run out of lives.

## 📂 Project Structure

```text
├── imgs/               # Images (backgrounds, fruits, icons)
├── sounds/             # Background music and sound effects
├── game.py             # Main game logic entry point
├── settings.py         # Configuration (screen size, colors, items)
├── game.spec           # PyInstaller configuration
└── README.md           # Documentation
```
---
**👨‍💻 Authors:**
DUTVcore & TranHuuLai
