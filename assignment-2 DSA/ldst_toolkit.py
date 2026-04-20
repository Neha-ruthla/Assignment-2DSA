# ----------- Dynamic Array -----------

class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.arr = [0] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = x
        self.size += 1

    def resize(self):
        print("Resizing from", self.capacity, "to", self.capacity * 2)
        new_arr = [0] * (self.capacity * 2)

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity *= 2

    def pop(self):
        if self.size == 0:
            return "Empty"
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def show(self):
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print()


# ----------- Singly Linked List -----------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None

    def insert_begin(self, x):
        n = Node(x)
        n.next = self.head
        self.head = n

    def insert_end(self, x):
        n = Node(x)

        if self.head is None:
            self.head = n
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = n

    def delete_val(self, x):
        temp = self.head

        if temp and temp.data == x:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    def show(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# ----------- Doubly Linked List -----------

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLL:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        n = DNode(x)

        if self.head is None:
            self.head = n
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = n
        n.prev = temp

    def insert_after(self, target, x):
        temp = self.head
        while temp:
            if temp.data == target:
                n = DNode(x)
                n.next = temp.next
                n.prev = temp

                if temp.next:
                    temp.next.prev = n

                temp.next = n
                return
            temp = temp.next

    def delete_pos(self, pos):
        temp = self.head

        for i in range(pos):
            temp = temp.next

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    def show(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# ----------- Stack -----------

class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        n = Node(x)
        n.next = self.head
        self.head = n

    def pop(self):
        if self.head is None:
            return "Empty"
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        if self.head:
            return self.head.data
        return "Empty"


# ----------- Queue -----------

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        n = Node(x)
        if self.tail is None:
            self.head = self.tail = n
            return
        self.tail.next = n
        self.tail = n

    def dequeue(self):
        if self.head is None:
            return "Empty"
        val = self.head.data
        self.head = self.head.next
        return val

    def front(self):
        if self.head:
            return self.head.data
        return "Empty"


# ----------- Parentheses Checker -----------

def is_balanced(s):
    st = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in "({[":
            st.push(ch)
        else:
            if st.peek() == pairs.get(ch):
                st.pop()
            else:
                return False

    return st.head is None


# ----------- MAIN -----------

def main():
    print("DYNAMIC ARRAY")
    da = DynamicArray()

    for i in range(1, 11):
        da.append(i)

    da.show()

    print("Pop:", da.pop())
    print("Pop:", da.pop())
    da.show()

    print("\nSINGLY LINKED LIST")
    sll = SinglyLL()
    sll.insert_begin(10)
    sll.insert_begin(20)
    sll.insert_end(30)
    sll.insert_end(40)
    sll.show()

    sll.delete_val(30)
    sll.show()

    print("\nDOUBLY LINKED LIST")
    dll = DoublyLL()
    dll.insert_end(1)
    dll.insert_end(2)
    dll.insert_end(3)
    dll.insert_after(2, 5)
    dll.show()

    dll.delete_pos(1)
    dll.show()

    print("\nSTACK")
    st = Stack()
    st.push(10)
    st.push(20)
    print("Peek:", st.peek())
    print("Pop:", st.pop())

    print("\nQUEUE")
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    print("Front:", q.front())
    print("Dequeue:", q.dequeue())

    print("\nPARENTHESES CHECK")
    tests = ["([])", "([)]", "(((", ""]
    for t in tests:
        print(t, "->", "Balanced" if is_balanced(t) else "Not Balanced")


main()