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

## Example

# Definition for singly-linked list.
class ListNode:
    def __init__(self, current_val=0, next=None):
        self.head = None
        self.current_val = current_val
        self.next = next
        
    def append(self, node):
        if self.head == None:
            self.val = node
            self.next = None    
        for current_node in self:
            pass
        current_node.next = node
        
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
        

#class Solution:
#    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        
            
if __name__ == "__main__":
    # Crear una lista enlazada
    linked_list = ListNode()

    # Agregar elementos a la lista
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    print("Lista después de agregar elementos:")
    print(linked_list)
        
        
        
        
        