# adjacency list

### the adjacency list is a way of  representing graphics, in essence they are a list of lists, where a list of vertex is stored at each vertex.

### | vertex | data |
### | 1 |  2 -> 3 -> None |
### | 2 |  4 -> None |
### | 3 |  None |
### | 4 |  5 -> 6 -> None |
### | 5 |  6 -> none |
### | 6 |  None |


### Implementation with a dictionarie

graph = {
    1: [2, 3,  None ],
    2: [4, None],
    3: [None],
    4: [5, 6, None],
    5: [6, None],
    6: [None]
    }
