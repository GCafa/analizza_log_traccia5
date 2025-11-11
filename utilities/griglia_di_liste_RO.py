# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 11:56:43 2025

@author: ianne
"""


from copy import copy


class Tabella2D_RO:
    '''
    Implementa una tabella bidimensionale in cui righe e
    colonne sono identificate da indici che partono da 0
    La tabella, dopo essere inizializzata, può essere 
    consultata, ma non modificata (Read-Only)
    '''
    
    def __init__(self, tabella: list[list[object]]):
        '''
        Costrutture
        La tabella è rappresentata da due liste di liste 
        organizzate a griglia

        Parameters
        ----------
        tabella : list[list[object]]
            tabella iniziale (lista di liste).

        Returns
        -------
        None.

        '''
        self._data4rows = tabella
        self._data4cols = [[tabella[i][j] for i in range(len(tabella))] for j in range(len(tabella[0]))]
    
    def size(self) -> tuple[int, int]:
        '''
        Restituisce il numero di righe e di colonne 
        della tabella

        Returns
        -------
        Numero di righe e di colonne

        '''
        return len(self._data4rows), len(self._data4cols)
    
    def get_cell(self, i: int, j: int) -> object:
        '''
        Dato l'indice di riga e di colonna di una cella 
        restituisce l'oggetto contenuto nella cella

        Parameters
        ----------
        i : int
            indice di riga.
        j : int
            indice di colonna.

        Returns
        -------
        object
            oggetto contanuto nella cella.

        '''
        return self._data4rows[i][j]
    
    def get_riga(self, i: int) -> list[object]:
        '''
        restituisce la lista che corrisponde a una riga
        della tabella

        Parameters
        ----------
        i : int
            indice di riga.

        Returns
        -------
        list[object]
            lista degli elementi contenuti nella riga.

        '''
        return copy(self._data4rows[i])
    
    def get_colonna(self, j: int) -> list[object]:
        '''
        restituisce la lista che corrisponde a una colonna
        della tabella       

        Parameters
        ----------
        j : int
            indice di colonna.

        Returns
        -------
        list[object]
            la lista degli elementi contenuti nella colonna.

        '''
        return copy(self._data4cols[j])
    
    
if __name__ == "__main__":
    t = Tabella2D_RO([[0, 0, 0],[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    i = 3
    j = 2
    print(f'Dimensioni: {t.size()}')
    print(f'Elemento ({i}, {j}): {t.get_cell(i,j)}')
    print(f'Riga {i}: {t.get_riga(i)}')
    print(f'Colonna {j}: {t.get_colonna(j)}')
    