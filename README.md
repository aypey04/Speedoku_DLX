# Speedoku_DLX 🔢
An ultra-efficient Sudoku solver built entirely in Python using **Donald Knuth’s Algorithm X** and the **Dancing Links (DLX)** technique.  
This project models Sudoku as an **Exact Cover** problem and solves it with blazing speed and elegant recursion.

---

##  Features

- Translates Sudoku into a **729×324 binary constraint matrix**
- Implements **DLX** (Dancing Links) for constant-time cover/uncover operations
- Solves any standard 9×9 puzzle in real time
- Supports full **solution enumeration** and uniqueness detection
- Built with a **modular, recursive architecture** — perfect for learning or extension
- Includes an optional **Pygame GUI** to visualize solutions instantly

---

##  Example Puzzle

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
```

---

## 🛠️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sudokux.git
cd sudokux
```

### 2. Install Requirements

```bash
pip install pygame
```

### 3. Run the Solver

```bash
python SSX.py
```

 If you want to run without the GUI, just comment out the `gui.run()` line at the bottom of the script.

---

## Tech Stack

- Python 3
- Algorithm X
- Dancing Links (DLX)
- Exact Cover theory
- Pygame *(optional, for GUI)*

---

##  License

MIT License. Feel free to use, modify, or contribute.
