# linked list

### las listas enlazadas se diferencian de las listas normales en la forma en la que almacenan los elementos en la memoria

### Los elementos de una lista enlazada se denominan nodos y cada nodo tiene 2 partes: date (datos) y next (referencia)

### [ (head) data ][ next ] -> [ data ][ next ] -> [ (last) data ][ next ] -> [None]

### uso: cuando se tienen que insertar y eliminar elementos al final o inicio de la lista constantemente.
### listas normales: cuando se quiere buscar un elemento especifico de la lista.

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
        
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def add_first(self, node):
        node.next = self.head
        self.head = node
        
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
    
    def add_after_node(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '%s' not found" % target_node_data_data)
    
    def add_before_node(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List empty")
        if self.head == target_node_data:
            return self.add_first(new_node)
        prev_nodex = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node    
        raise Exception("Node with data '%s' not found" % target_node_data)
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("Linked list is empty")
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node
        raise Exception("Node with data '%s' not found" % target_node_data)
        
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data
    
llist = LinkedList()
n1 = Node("a")
n2 = Node("b")
n3 = Node("c")
n4 = Node("d")
n5 = Node("e")
llist.head = n1

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print(llist)

llist.remove_node("c")

print(llist)
    
    
    
    
    