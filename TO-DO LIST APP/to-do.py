# Define a class to represent each task in the to-do list
class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

# Define a class to manage the linked list of tasks
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a new task to the end of the linked list
    def add_task(self, task):
        new_node = Node(task)
        if not self.head:
            # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            # Traverse the list to find the last node and append the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Method to view all tasks in the linked list
    def view_tasks(self):
        if not self.head:
            # If the list is empty, inform the user
            print("Your to-do list is empty!")
        else:
            # Traverse the list and print each task along with its index
            print("Your To-Do List:")
            current = self.head
            index = 1
            while current:
                print(f"{index}. {current.task}")
                current = current.next
                index += 1

    # Method to mark a task as completed and remove it from the linked list
    def complete_task(self, task_index):
        if not self.head:
            # If the list is empty, inform the user
            print("Your to-do list is empty!")
            return

        if task_index < 1:
            # If the provided task index is invalid, inform the user
            print("Invalid task number!")
            return

        if task_index == 1:
            # If the task to complete is the first one, update the head pointer
            completed_task = self.head.task
            self.head = self.head.next
            print(f"Task '{completed_task}' marked as completed!")
            return

        # Traverse the list to find the node at the specified index
        current = self.head
        prev = None
        index = 1
        while current and index < task_index:
            prev = current
            current = current.next
            index += 1

        if current:
            # If the node is found, remove it from the list
            completed_task = current.task
            prev.next = current.next
            print(f"Task '{completed_task}' marked as completed!")
        else:
            # If the provided task index is out of range, inform the user
            print("Invalid task number!")

# Main function to handle user interactions
def main():
    # Create an instance of LinkedList to manage the to-do list
    todo_list = LinkedList()

    # Main loop to display menu and process user input
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        # Prompt user for choice
        choice = input("Enter your choice: ")

        # Check user's choice and call appropriate methods
        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task number to mark as completed: "))
            todo_list.complete_task(task_index)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
