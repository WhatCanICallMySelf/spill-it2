"""
pseudokode for funskjonen clear_cell, fra game.py

Funksjon clear_cell(cell, x, y):
    Hvis cellen allerede er klarert:
        Returner

    Sett cellen som klarert
    Øk telleren for antall klarerte celler

    For hver nabo i en 3x3 rute rundt den nåværende cellen:
        For dx fra -1 til 1:
            For dy fra -1 til 1:
                Hvis dx og dy begge er 0 (nåværende celle):
                    Fortsett til neste iterasjon

                Beregn naboens koordinater: nx = x + dx, ny = y + dy
                Hent naboen fra rutenettet basert på nx og ny

                Hvis naboen eksisterer:
                    Hvis naboen ikke har en bombe og den nåværende cellen har 0 nabobomber:
                        Start funksjonen på nabo med clear_cell(nabo, nx, ny)
"""