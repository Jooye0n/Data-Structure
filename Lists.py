import sys


class SList:
    """Singly linked list implementation only with head."""
    class _Node:
        def __init__(self, element, next=None):
            self._element = element
            self._next = next
        
        def element(self):
            return self._element
        
        def next(self):
            return self._next
        
        def set_element(self, element):
            self._element = element
        
        def set_next(self, next):
            self._next = next
    
    def __init__(self, head=None):
        """Create a singly linked list that contains only head, not size"""
        self._head = head
    
    def __len__(self):
        """len(SList) returns the number of elements in SList"""
        length = 0
        node = self._head
        while node:
            length += 1
            node = node.next()
        return length
    
    def __str__(self):
        """Returns the string representation and the number of elements"""
        count = 0
        p = self._head
        rep = f''
        while p:
            rep += str(p.element()) + ' -> '
            p = p.next()
            count += 1
        rep += f'None: {count} element(s)'
        return rep
    
    def is_empty(self):
        return self._head is None
    
    def head(self):
        return self._head
    
    def search(self, element):
        """Search an element in self by link hopping through next"""
        p = self._head
        while p:
            if p.element() == element:
                return p  # found returns its position
            p = p.next()
        return None  # not found
    
    def insert_first(self, element):
        """Insert the node of element in front of head"""
        self._head = self._Node(element, self._head)
    
    def delete_first(self):
        """Delete the head node and return its element"""
        if self.is_empty():
            return None
        element = self._head.element()
        self._head = self._head.next()
        return element
    
    def insert_after(self, element, p):
        p._next = self._Node(element, p._next)
    
    def delete_after(self, p):
        temp = p.next().next()
        p.set_next(temp)
    
    def insert_last(self, element):
        newNode = self._Node(element)
        
        if self.is_empty():
            self._head = newNode
        else:
            temp = self._head
            while temp.next():
                temp = temp.next()
            temp.set_next(newNode)

def delete_last(self):
    if self.is_empty():
        return None
        if not self._head.next(): #self._head.next() is None:
            answer = self._head.element()
            self._head = None
    else:
        temp = self._head
            while temp.next().next():
                temp = temp.next()
        answer = temp.next().element()
            temp.set_next(None)
return answer
    
    
    def reverse_recursively(self, current):
        if current.next() == None:
            self._head = current
            return
        head = current
        tail = current.next()
        self.reverse_recursively(tail)
        tail.set_next(head)
        head.set_next(None)
    
    def reverse_iteratively(self, current):
        """Iteratively reverse the order of  nodes from current to the end in self."""
        predecessor = None
        while current:
            successor = current.next()
            current.set_next(predecessor)
            predecessor = current
            current = successor
        self._head = predecessor
    
    # 연습문제 2.12
    def find_middle(self):
        fastPtr = self._head
        slowPtr = self._head
        while fastPtr != None and fastPtr.next() != None:
            fastPtr = fastPtr.next().next()
            slowPtr = slowPtr.next()
        return slowPtr


# 연습문제 2.7
def merge_list(s1, s2):
    merge_list = SList();
    a = s1.head()
    B = s2.head()
    while a or b:
        if a != None:
            if (b and a.element() <= b.element()) or (b == None):
                merge_list.insert_last(a.element())
                a = a.next()
    
        if b != None:
            if (a and b.element() <= a.element()) or (a == None):
                merge_list.insert_last(b.element())
                b = b.next()

                    return merge_list

class DList:
    """Doubly linked list implementation with dummy header and trailer."""
    class _Node:
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
        
        def element(self):
            return self._element
        
        def next(self):
            return self._next
        
        def prev(self):
            return self._prev
        
        def set_element(self, element):
            self._element = element
        
        def set_next(self, next):
            self._next = next
        
        def set_prev(self, prev):
            self._prev = prev
    
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
    
    def size(self, current):
        if(not current):
            return 0
        else:
            if current.next() == self._trailer :
                return self.size(current.next())
            
            return 1 + self.size(current.next())

def __len__(self):
    return self.size(self.header().next())
    
    def __str__(self):
        """Returns the string representation and the number of elements"""
        count = 0
        p = self.header().next()
        rep = f'Header <-> '
        while p is not self.trailer():
            rep += str(p.element()) + ' <-> '
            p = p.next()
            count += 1
        rep += f'Trailer: {count} element(s)'
        return rep
    
    def is_empty(self):
        return self.header().next() == self.trailer()
    
    def header(self):
        return self._header
    
    def trailer(self):
        return self._trailer
    
    def search(self, element):
        """Search a node containing element in self."""
        p = self.header().next()
        while p is not self.trailer():
            if p.element() == element:
                return p
            p = p.next()
        return None
    
    def insert_between(self, element, predecessor, successor):
        """Add an element between predecessor and successor, and return a new node"""
        new_node = self._Node(element, predecessor, successor)
        predecessor.set_next(new_node)
        successor.set_prev(new_node)
        return new_node
    
    def insert_after(self, element, p):
        if p is self._trailer:
            return None
        else:
            return self.insert_between(element, p, p.next())

def insert_before(self, element, p):
    if p is self._header:
        return None
        else:
            return self.insert_between(element, p.prev(), p)
                
                def insert_first(self, element):
                    return self.insert_after(element, self._header)

def insert_last(self, element):
    return self.insert_before(element, self._trailer)
    
    def delete_node(self, node):
        """Delete non-sentinel node and return its element"""
        if (node is self._header) or (node is self._trailer):
            return None
        
        predecessor = node.prev()
        successor = node.next()
        predecessor.set_next(successor)
        successor.set_prev(predecessor)
        element = node.element()
        node._prev = node._next = node._element = None
        return element


if __name__ == "__main__":
    s1 = SList()
    s1.insert_first("graph")
    s1.insert_first("orange")
    s1.insert_first("cherry")
    s1.insert_first("apple")
    print(s1)
    s1.insert_after("elem", s1.find_middle())
    print(s1)
    s1.insert_last("ins_lst")
    print(s1)
    s1.insert_last("ins_lst2")
    print(s1)
    print(s1.find_middle().element())
    s1.delete_after(s1.find_middle())
    
    print("check")
    print(s1)
    s1.delete_last()
    print(s1)
    s1.delete_first()
    print(s1)
    
    s1.reverse_iteratively(s1.head())
    print(s1)
    
    try:
        s1.reverse_recursively(s1.head())
        print(s1)
    except NotImplementedError:
        print(f"Reversing SList recursively: {sys.exc_info()}")
    
    try:
        middle = s1.find_middle()
        print("middle")
        print(middle.element())
    except NotImplementedError:
        print(f"Finding middle in SList: {sys.exc_info()}")

    d1 = DList()
    print(d1.is_empty())
    d1.insert_last(1)
    d1.insert_last(2)
    d1.insert_last(3)
    d1.insert_last(4)
    d1.insert_last(5)

print(d1)

try:
    print("사이즈출력")
    print(len(d1))
    print(d1.size(d1.search(3)))
    except NotImplementedError:
        print(f"Counting nodes in DList: {sys.exc_info()}")
    
    p = d1.search(4)
    print(p)
    d1.delete_node(p)
    print(d1)
