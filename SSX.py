import time # IMPORT: For timing the solver

class Node:
    def __init__(self):
        self.left = self.right = self.up = self.down = self
        self.column = None
        self.row_id = None

class ColumnNode(Node):
    def __init__(self, name=""):
        super().__init__()
        self.size = 0
        self.name = name

class DLXSolver:
    def __init__(self):
        self.root = ColumnNode('root')
        self.solution = []
        self.solution_count = 0
        self.first_solution = None

    def _iterate_right(self, start_node):
        curr = start_node.right
        while curr != start_node:
            yield curr
            curr = curr.right

    def _iterate_left(self, start_node):
        """Iterates left from a node until it returns to the start."""
        curr = start_node.left
        while curr != start_node:
            yield curr
            curr = curr.left

    def _iterate_down(self, start_node):
        curr = start_node.down
        while curr != start_node:
            yield curr
            curr = curr.down

    def build_matrix(self, matrix, row_ids):
        if not matrix or not matrix[0]:
            return

        num_cols = len(matrix[0])
        columns = [ColumnNode(str(i)) for i in range(num_cols)]

        for i in range(num_cols):
            col = columns[i]
            col.left = columns[i-1] if i > 0 else self.root
            col.right = columns[(i + 1) % num_cols] if i < num_cols - 1 else self.root
            col.left.right = col
            col.right.left = col
            col.column = col

        self.root.right = columns[0]
        self.root.left = columns[-1]

        for i, row in enumerate(matrix):
            first_node_in_row = None
            for j, value in enumerate(row):
                if value == 1:
                    col = columns[j]
                    new_node = Node()
                    new_node.row_id = row_ids[i]
                    
                    new_node.column = col
                    new_node.up = col.up
                    new_node.down = col
                    col.up.down = new_node
                    col.up = new_node
                    col.size += 1

                    if first_node_in_row is None:
                        first_node_in_row = new_node
                    else:
                        new_node.left = first_node_in_row.left
                        new_node.right = first_node_in_row
                        first_node_in_row.left.right = new_node
                        first_node_in_row.left = new_node


    def cover(self, col_header):
        col_header.right.left = col_header.left
        col_header.left.right = col_header.right
        for row_node in self._iterate_down(col_header):
            for right_node in self._iterate_right(row_node):
                right_node.up.down = right_node.down
                right_node.down.up = right_node.up
                right_node.column.size -= 1

    def uncover(self, col_header):
        for row_node in self._iterate_down(col_header):
            for left_node in self._iterate_right(row_node):
                left_node.column.size += 1
                left_node.up.down = left_node
                left_node.down.up = left_node
        col_header.right.left = col_header
        col_header.left.right = col_header

    def search(self):
        """Recursively search for all exact cover solutions."""
        if self.root.right == self.root:
            self.solution_count += 1
            if self.first_solution is None:
                self.first_solution = list(self.solution)
            return

        col_to_cover = min(self._iterate_right(self.root), key=lambda c: c.size)

        if col_to_cover.size == 0:
            return

        self.cover(col_to_cover)

        for row_node in self._iterate_down(col_to_cover):
            self.solution.append(row_node)
            for right_node in self._iterate_right(row_node):
                self.cover(right_node.column)
            
            self.search() # Continue search

            # Backtrack
            for left_node in self._iterate_left(row_node): # Use iterate_left
                self.uncover(left_node.column)
            self.solution.pop()
        
        self.uncover(col_to_cover)

    def solve(self, puzzle):
        if not puzzle or len(puzzle) != 9 or any(len(row) != 9 for row in puzzle):
            raise ValueError("Invalid puzzle: must be a 9x9 grid")

        matrix, row_ids = sudoku_to_exact_cover(puzzle)
        self.build_matrix(matrix, row_ids)

        self.search() 

        if self.solution_count > 0:
            result = [[0] * 9 for _ in range(9)]
            for node in self.first_solution: 
                r, c, d = node.row_id
                result[r][c] = d
            return result
        else:
            return None

def sudoku_to_exact_cover(grid):
    matrix = []
    row_ids = []
    
    def cell_constraint(r, c): return r * 9 + c
    def row_constraint(r, d): return 81 + r * 9 + (d - 1)
    def col_constraint(c, d): return 162 + c * 9 + (d - 1)
    def box_constraint(r, c, d): return 243 + (3 * (r // 3) + (c // 3)) * 9 + (d - 1)

    for r in range(9):
        for c in range(9):
            digit = grid[r][c]
            possible_digits = range(1, 10) if digit == 0 else [digit]
            
            for d in possible_digits:
                row = [0] * 324
                row[cell_constraint(r, c)] = 1
                row[row_constraint(r, d)] = 1
                row[col_constraint(c, d)] = 1
                row[box_constraint(r, c, d)] = 1
                matrix.append(row)
                row_ids.append((r, c, d))
                
    return matrix, row_ids

if __name__ == "__main__":
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

    try:
        solver = DLXSolver()
        
        start_time = time.time()
        solution = solver.solve(puzzle)
        end_time = time.time()
        
        duration = end_time - start_time

        if solution:
            print("First solution found:")
            for row in solution:
                print(row)
            print("-" * 25)
            print(f"Time taken: {duration:.4f} seconds")
        else:
            print("No solution exists for the given puzzle.")
            print(f"Time taken: {duration:.4f} seconds")
            
    except Exception as e:
        print(f"An error occurred: {e}")
