# merge two sorted lists
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        """Representación en cadena de la lista enlazada a partir de este nodo."""
        nodes = []
        current = self
        while current:
            nodes.append(current.val)
            current = current.next
        return " -> ".join(map(str, nodes)) + " -> None"
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        while list1 is not None and list2 is not None:
            if list1.val == list2.val or list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        # Agregar nodos restantes de una de las listas
        if list1 is not None:
            curr.next = list1
        elif list2 is not None:
            curr.next = list2
  
        return dummyHead.next
        
# Clase principal para probar la implementación
if __name__ == "__main__":
    # Crear dos listas enlazadas 
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)


    # Crear una instancia de Solution
    solution = Solution()
    result = solution.mergeTwoLists(l1, l2)

    # Mostrar el resultado
    print("Resultado de la suma:")
    print(result)        