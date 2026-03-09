from abc import ABC, abstractmethod

class Solver(ABC):
    def __init__(self, initial_grid: list[list[int]], grid_size: int):
        self.grid_size = grid_size
        # Convert the starting grid into a tuple of tuples so it is immutable and hashable
        self.initial_state = tuple(tuple(row) for row in initial_grid)
        self.is_finished = False
        self.is_solved = False

    @abstractmethod
    def get_next_step(self) -> tuple[tuple, str]:
        """
        Executes one single step of the algorithm.
        Returns the current evaluated state (2D tuple) and a status message.
        """
        pass
    
    def is_valid_partial_state(self, state: tuple) -> bool:
        """
        Checks if the current grid breaks any Binairo rules.
        """
        max_count = self.grid_size // 2

        # Check rows
        for row in state:
            if row.count(1) > max_count or row.count(2) > max_count:
                return False
            for i in range(self.grid_size - 2):
                if row[i] != 0 and row[i] == row[i+1] == row[i+2]:
                    return False

        # Check columns
        for col_idx in range(self.grid_size):
            col = [state[row_idx][col_idx] for row_idx in range(self.grid_size)]
            if col.count(1) > max_count or col.count(2) > max_count:
                return False
            for i in range(self.grid_size - 2):
                if col[i] != 0 and col[i] == col[i+1] == col[i+2]:
                    return False

        # Note: Duplicate rows/cols are usually checked only when the board is fully filled 
        # to save performance during the search.
        return True