# IT2 Game
- Smidig utvikling
## Possible games?
- Pong
- Yatzi
- Minesweeper
- Flappy bird

## Minesweeper
Målet med spillet er å få vekk minene i et minefelt uten at de sprenger. Dette kan man få til ved å se på tallene i minefeltet som viser hvor mange miner som er rundt denne ruten. med denne informasjonen skal det være mulig å kunne unngå å sprenge minene. 

### Flowchart
```mermaid
flowchart TD
    A[Start Minesweeper] --> B[Initialise grid with adjustable size]
    B --> C[Randomly place bombs on the grid]
    C --> D[Display grid to the player]
    D --> E[Input coordinates to open or flag a cell]
    
    E --> F{Is the cell a bomb?}
    F -- Yes --> G[Trigger explosion]
    G --> H[Reveal all bombs on the grid]
    H --> I[Game Over!]
    
    F -- No --> J[Reveal number in the cell]
    J --> K{Is the number 0?}
    
    K -- Yes --> L[Expand to adjacent cells]
    K -- No --> M[End turn]

    L --> N[Continue revealing adjacent cells if they are zeros]
    M --> D
```

### Classes:
```mermaid
classDiagram
    class Cell {
        neibour_bombs: int
        has_bomb: bool
        flagged: bool
        set_bomb()
        set_flag()
        calculate_neibour_bombs()
    }

    class Grid {
        grid: 2D array with cells
        create_grid()
        restart()
        wipe_grid()
    }
```
## arbeidsoppgaver 
- Alexander
    - Lage klassen "grid"

- Ulrik
    - Lage klassediagram for game
    - Lage klassen "game"

- Dina
    - Lage klassen "cell"