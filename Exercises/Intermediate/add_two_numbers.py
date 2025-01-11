from typing import Optional

# Definición de ListNode
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

# Clase Solution con el método addTwoNumbers
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)  # Nodo inicial para construir la lista resultante
        curr = dummyHead
        carry = 0
        
        while l1 is not None or l2 is not None or carry != 0:
            l1Val = l1.val if l1 else 0  # Obtiene el valor de l1 o 0 si es None
            l2Val = l2.val if l2 else 0  # Obtiene el valor de l2 o 0 si es None
            
            columnSum = l1Val + l2Val + carry  # Suma los valores y el acarreo
            carry = columnSum // 10  # Calcula el nuevo acarreo
            
            newNode = ListNode(columnSum % 10)  # Crea un nuevo nodo con el dígito resultante
            curr.next = newNode  # Conecta el nuevo nodo a la lista resultante
            curr = newNode  # Avanza al nuevo nodo
            
            l1 = l1.next if l1 else None  # Avanza al siguiente nodo en l1
            l2 = l2.next if l2 else None  # Avanza al siguiente nodo en l2
        
        return dummyHead.next  # Retorna la lista resultante omitiendo el nodo inicial

# Clase principal para probar la implementación
if __name__ == "__main__":
    # Crear dos listas enlazadas para representar los números 342 y 465
    # Representación: (2 -> 4 -> 3) + (5 -> 6 -> 4)

    # Lista para el número 342 (2 -> 4 -> 3)
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    # Lista para el número 465 (5 -> 6 -> 4)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    # Crear una instancia de Solution y sumar las dos listas enlazadas
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # Mostrar el resultado
    print("Resultado de la suma:")
    print(result)  # Salida esperada: 7 -> 0 -> 8 -> None (representa el número 807)
