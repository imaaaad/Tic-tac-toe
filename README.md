# 🎮 Tic Tac Toe (Python OOP Project)

A simple command-line **Tic Tac Toe** game built in **Python** using **Object-Oriented Programming (OOP)** principles.

---

## 📁 Project Structure

```
tic_tac_toe/
├── main.py          # Entry point to start the game
├── match.py         # Handles the game logic, players, and turns
├── table.py         # Manages the 3x3 board grid and its operations
├── option.py        # Represents a player's symbol (X or O)
└── README.md        # Project documentation
```

---

## 🧠 OOP Concepts Used

- **Encapsulation**: Each class handles its own responsibilities.
- **Abstraction**: Game logic is separated from user interaction.
- **Modular Design**: Classes are defined in separate files for clarity and reuse.

---

## 🚀 How to Run

### ▶️ Step-by-step:

1. Make sure you have Python 3 installed.
2. Open a terminal in the project directory.
3. Run the game:
   ```bash
   python main.py
   ```

---

## 🎯 Game Rules

- The game is played on a 3x3 grid.
- Two players take turns placing **X** or **O**.
- The first to align three symbols (horizontally, vertically, or diagonally) wins.
- If all 9 cells are filled and no winner is found, the game ends in a **draw**.

---

## 🧪 Example Interaction

```
Welcome to Tic Tac Toe!
Current Board:
 | | 
-----
 | | 
-----
 | | 
-----
Player X, enter your move (row col): 0 1
Player O, enter your move (row col): 1 1
...
🎉 Player X wins!
```

---

## ✅ Features

- Input validation (only accepts correct coordinates and available cells).
- Turn-by-turn display.
- Win/draw detection.
- Fully object-oriented structure.

---

## 📌 Author

- **Imad Chabi**  


---

Enjoy the game! 🎉
