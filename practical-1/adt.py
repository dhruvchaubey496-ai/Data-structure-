import os
import time
from termcolor import colored,cprint

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
        print(colored(f"'{item}' has been pushed onto the stack.", "green"))
        self.animate_push(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an Empty stack")
        item = self.items.pop()
        print(colored(f"'{item}' has been popped from stack.", "red"))
        self.animate_pop(item)
        return item
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an Empty Stack")
        return self.items[-1]
    def size(self):
        return len(self.items)
    def __str__(self):
        return " <- ".join(reversed(self.items)) if self.items else "stack is empty"
    def animate_push(self, item):
        for i in range(3):
            print(colored(f"Pushing {item} into stack...", "yellow"))
            time.sleep(0.4)
            self.clear_screen()
    def animate_pop(self, item):
        for i in range(3):
            print(colored(f"Popping {item} into stack...", "pink"))
            time.sleep(0.4)
            self.clear_screen()
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

def stack_operations():
    stack = Stack()
    cprint("Welcome to my Interactive Stack Operations Program", "cyan", attrs=["bold"])
    cprint("You can Perform the following operations on the stack : ", "cyan")

    while True:
        print("\nCurrent Stack : ", colored(str(stack), "blue"))
        print(colored("1 - Push Element", "yellow"))
        print(colored("2 - pop Element", "yellow"))
        print(colored("3 - Peek Element", "yellow"))
        print(colored("4 - Check is Stack is Empty", "yellow"))
        print(colored("5 - Size of Stack ", "yellow"))
        print(colored("6 - Quit Program", "yellow"))

        try :
            choice = int(input(colored("Choose an Operation (1-6): ", "green")))
        except ValueError:
            cprint("Invalid Input, Please enter a number between 1 to 6", "red")
            continue
        if choice == 1:
            item = input(colored("Enter an element to push : ", "green"))
            stack.push(item)
        elif choice == 2:
            try :
                stack.pop()
            except IndexError as e:
                cprint(e, "red")
        elif choice == 3:
            try :
                cprint("Top Element : " + stack.peek(), "blue")
            except IndexError as e:
                cprint(e, "red")
        elif choice == 4:
            try :
                cprint("Is the Stack Empty ? " + ("yes" if stack.is_empty() else "No"), "blue")
            except IndexError as e:
                cprint(e, "red")
        elif choice == 5:
            try :
                cprint("Size of the Stack : " + str(stack.size()), "blue")
            except IndexError as e:
                cprint(e, "red")
        elif choice == 6:
            cprint("Exiting the Program", "cyan", attrs=["bold"])
            break
        else :
            cprint("Invalid Choice , Please enter a number from 1 and 6", "red")

if __name__ == "__main__":
    stack_operations()
