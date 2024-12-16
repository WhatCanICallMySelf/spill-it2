# IT2 Game
- Smidig utvikling

## Minesweeper
Målet med spillet er å få vekk minene i et minefelt uten at de sprenger. Dette kan man få til ved å se på tallene i minefeltet som viser hvor mange miner som er rundt denne ruten. Med denne informasjonen skal det være mulig å kunne unngå å sprenge minene. 

### Flowchart
```mermaid
 flowchart TD
    A[Start Game] --> B[Initialize Game]
        B --> C[Main Game Loop]
        C --> D{Is Player Alive?}
        D -- Yes --> E[Display Grid]
        E --> F[Print Instructions]
        F --> G[Get Player Input]
        G --> H{Is Valid Input?}
        H -- No --> I[Display Error Message]
        I --> C
        H -- Yes --> J[Parse Command]
        J --> K{Command Type}
        
        K -- o --> L[Open Cell]
        L --> M{Is First Move?}
        M -- Yes --> N[Randomize Bombs ignoring 3x3 area around opened cell and Set Neighbor Bombs]
        N --> O
        M -- No --> O{Is Cell a Bomb?}
        
        O -- Yes --> P[Display BOOOOOM]
        P --> Q[Set Alive to False]
        O -- No --> R[Clear Cell]
        
        R --> S{All cells cleared?}
        S -- Yes --> T[Display YOU WIN]
        S -- No --> C
        
        K -- f --> U[Flag Cell]
        U -- Yes --> V[Set Flag to True]
        
        K -- r --> Y[Remove Flag]
        Y --> Z{Does Cell have Flag?}
        Z -- Yes --> AA[Remove Flag]
        Z -- No --> AB[Display No Flag Message]
        
        K -- q --> AC[Set Alive to False]
        
        D -- No --> AD[End Game]
```

### Classes:
```mermaid
classDiagram
class Cell {
        - _neighbour_bombs : int
        - _has_bomb : bool
        - _has_flag : bool
        - _is_cleared : bool
        + __init__()
        + __str__() : String
        + has_bomb() : bool
        + has_flag() : bool
        + is_cleared() : bool
        + neighbor_bombs() : int
        + set_bomb(has_bomb: bool)
        + set_flag(has_flag: bool)
        + set_cleared(is_cleared: bool)
        + set_neighbor_bombs(amount: int)
    }

    class Grid {
        - _size : int
        - _grid : Cell[][]
        + __init__(size: int)
        + __str__() : String
        + get_cell(x: int, y: int) : Cell | None
    }

    class Game {
        - _grid : Grid
        - _alive : bool
        - _generated_bombs : bool
        - _start_time : float
        - _cleared_cells : int
        + __init__()
        + play()
        + clear_cell(cell: Cell, x: int, y: int)
        + randomize_bombs(bombs_to_place: int, safe_x: int, safe_y: int)
        + set_neighbor_bombs()
        + do_turn()
    }
```