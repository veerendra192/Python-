class Stack:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, item):
        self.queue.append(item)
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack: ", self.queue)

stack = Stack()

while True:
    print("push")
    print("pop")
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
            print("Popped value: ", item)
    elif choice == "display":
        stack.display()
    elif choice == "exit":
        break
    else:
        print("Invalid choice. Try again.")
