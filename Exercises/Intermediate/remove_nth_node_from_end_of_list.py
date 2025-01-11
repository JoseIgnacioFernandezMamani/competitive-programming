from typing import Optional

# Definition for singly-linked list.
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res
        for _ in range(n):
            head = head.next
        while head:
            head = head.next
            dummy = dummy.next
        dummy.next = dummy.next.next
        return res.next
            
# Clase principal para probar la implementación
if __name__ == "__main__":
    # Crear dos listas enlazadas 
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    
    print(l1)

    # Crear una instancia de Solution y sumar las dos listas enlazadas
    solution = Solution()
    result = solution.removeNthFromEnd(l1, 2)

    # Mostrar el resultado
    print("Resultado de la suma:")
    print(result) 
