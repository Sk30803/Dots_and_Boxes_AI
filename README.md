# 🎮 Dots and Boxes AI Game

A Python-based implementation of the classic **Dots and Boxes** game with a competitive AI opponent. This project features a GUI built with Tkinter and an AI player powered by the **Minimax algorithm with Alpha-Beta pruning**. Designed for both single-player (vs AI) and two-player gameplay.

---

## 🚀 Features

- 🧠 **AI Opponent:** Uses Minimax with Alpha-Beta pruning for decision-making
- 🎯 **Difficulty Levels:** Easy, Medium, Hard (controls search depth and heuristic)
- 🖥️ **Graphical UI:** Built with Tkinter – clean and interactive
- 🔢 **Live Score Tracking:** Scores update in real-time
- 🧱 **6x6 Game Grid:** Automatically scales layout and move count

---

## 🛠️ Technologies Used

- Python 3
- Tkinter for GUI
- Algorithm: Minimax with Alpha-Beta pruning

---

## 📸 Screenshots

_(Optional: Add if you want – or skip this section)_

---

## 🧠 AI Strategy

- The AI simulates all possible moves using a depth-limited Minimax algorithm.
- Heuristics include point scoring, threat prevention, and board state evaluation.
- Difficulty levels affect how many moves ahead the AI looks:
  - **Easy:** shallow search
  - **Hard:** deeper search with custom heuristics

---

## 📦 How to Run

1. Make sure you have **Python 3** installed
2. Run the game:
   ```bash
   python dots_and_boxes.py

