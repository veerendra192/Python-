class Stack:
    def __init__(self):
        self.items = []
        self.min_items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        if len(self.min_items) == 0 or item <= self.min_items[-1]:
            self.min_items.append(item)

    def pop(self):
        if not self.is_empty():
            item = self.items.pop()
            if item == self.min_items[-1]:
                self.min_items.pop()
            return item

    def top(self):
        if not self.is_empty():
            return self.items[-1]

    def minimum(self):
        if not self.is_empty():
            return self.min_items[-1]

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack items (top to bottom):")
            for item in reversed(self.items):
                print(item,end=" ")

stack = Stack()

while True:
    print("push")
    print("pop")
    print("top")
    print("min")
    print("display")
    print("exit")
    choice = input("Enter your choice: ")

    if choice == "push":
        item = int(input("Enter item to push: "))
        stack.push(item)
        print("Item pushed to stack.")
    elif choice == "pop":
        item = stack.pop()
        if item is None:
            print("Stack is empty.")
        else:
            print("Popped item: ", item)
    elif choice == "top":
        item = stack.top()
        if item is None:
            print("Stack is empty.")
        else:
            print("Top item: ", item)
    elif choice == "min":
        item = stack.minimum()
        if item is None:
            print("Stack is empty.")
        else:
            print("Minimum item: ", item)
    elif choice == "display":
        stack.display()
    elif choice == "exit":
        break
    else:
        print("Invalid choice. Try again.")
