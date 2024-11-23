class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None


# Розширення Stack для підрахунку операцій pop
class StackWithCounter(Stack):
    def __init__(self):
        super().__init__()
        self._pop_count = 0  # Лічильник операцій pop

    def pop(self):
        item = super().pop()
        if item is not None:
            self._pop_count += 1
        return item

    def get_counter(self):
        return self._pop_count


# Тестування
stack = StackWithCounter()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # 3
print(stack.pop())  # 2
print("Pop operations count:", stack.get_counter())  # 2


class QueueError(Exception):
    """Виняток для черги"""
    pass


class Queue:
    def __init__(self):
        self.items = []

    def put(self, element):
        self.items.append(element)

    def get(self):
        if not self.items:
            raise QueueError("Queue is empty")
        return self.items.pop(0)  # Видаляємо з початку списку

    def is_empty(self):
        return len(self.items) == 0


# Тестування
queue = Queue()
queue.put(1)
queue.put("dog")
queue.put(False)

print(queue.get())  # 1
print(queue.get())  # "dog"
print(queue.is_empty())  # False

try:
    queue.get()
    queue.get()  # Тут буде викликано QueueError
except QueueError as e:
    print(e)  # Queue is empty


class QueueError(Exception):
    """Виняток для черги"""
    pass


class Queue:
    def __init__(self):
        self.items = []

    def put(self, element):
        self.items.append(element)

    def get(self):
        if not self.items:
            raise QueueError("Queue is empty")
        return self.items.pop(0)  # Видаляємо з початку списку

    def is_empty(self):
        return len(self.items) == 0


# Тестування
queue = Queue()
queue.put(1)
queue.put("dog")
queue.put(False)

print(queue.get())  # 1
print(queue.get())  # "dog"
print(queue.is_empty())  # False

try:
    queue.get()
    queue.get()  # Тут буде викликано QueueError
except QueueError as e:
    print(e)  # Queue is empty
