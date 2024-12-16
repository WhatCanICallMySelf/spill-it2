class Cell:
    def __init__(self):
        """
        Initializes a Cell object.
        """
        self._neighbour_bombs = 0
        self._has_bomb = False
        self._has_flag = False
        self._is_cleared = False

    def __str__(self) -> str:
        """
        Returns a string representation of the cell's state.
        Depending on the state, returns:
        - The number of neighboring bombs if cleared
        - Flag indicator if flagged
        - An empty cell indicator if not cleared and not flagged
        """
        # Debug
        # if self._has_bomb:
        #    return "\033[41m[B]\033[0m"
        if self._is_cleared:
            return f"[{self._neighbour_bombs}]"
        elif self._has_flag:
            return "[f]"
        return "[ ]"

    @property
    def has_bomb(self) -> bool:
        """:return: True if the cell has a bomb, otherwise False."""
        return self._has_bomb

    @property
    def has_flag(self) -> bool:
        """:return: True if the cell is flagged, otherwise False."""
        return self._has_flag

    @property
    def is_cleared(self) -> bool:
        """:return: True if the cell has been cleared, otherwise False."""
        return self._is_cleared

    @property
    def neighbor_bombs(self) -> int:
        """:return: the number of bombs in neighboring 3x3 cells."""
        return self._neighbour_bombs

    def set_bomb(self, has_bomb: bool):
        """:param has_bomb: True to set the cell as a bomb, otherwise False."""
        self._has_bomb = has_bomb

    def set_flag(self, has_flag: bool):
        """:param has_flag: True to flag the cell, False to unflag it."""
        self._has_flag = has_flag

    def set_cleared(self, is_cleared: bool):
        """:param is_cleared: True to mark the cell as cleared, otherwise False."""
        self._is_cleared = is_cleared

    def set_neighbor_bombs(self, amount: int):
        """:param amount: The count of neighboring bombs."""
        self._neighbour_bombs = amount
