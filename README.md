# SudokuX 🧠🔥  
A blazing-fast Sudoku solver powered by Donald Knuth’s **Algorithm X** and **Dancing Links (DLX)** — built entirely in Python.

---

## 🚀 Features

- Models Sudoku as a 729×324 **Exact Cover problem**
- Implements **DLX (Dancing Links)** for ultra-efficient constraint resolution
- Solves any valid 9×9 puzzle in milliseconds
- Tracks total number of valid solutions (uniqueness detection)
- Clean, recursive architecture — easy to understand and extend
- Optional **Pygame GUI** for real-time visualization

---

## 📷 Screenshot  
<img src="screenshot.png" alt="sudoku gui" width="500"/>

---

## 🧩 Example Puzzle
```python
puzzle = [
    [3, 0, 0, 8, 0, 0, 1, 0, 0],
    [0, 0, 8, 0, 0, 4, 2, 0, 0],
    [0, 0, 0, 6, 3, 0, 0, 0, 0],
    [4, 0, 0, 0, 9, 6, 0, 5, 0],
    [0, 0, 3, 0, 0, 0, 0, 6, 0],
    [0, 0, 7, 0, 0, 1, 0, 9, 0],
    [0, 5, 0, 0, 0, 8, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 9, 7, 0, 0],
]

How to Run
git clone https://github.com/yourusername/sudokux.git
cd sudokux
pip install pygame
python SSX.py
