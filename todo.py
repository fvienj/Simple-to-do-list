tasks = []


def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Task added.")


def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{i}. [{mark}] {task['title']}")

def delete_task():
    view_tasks()
    number = int(input("Enter task number to delete: "))
    removed = tasks.pop(number - 1)
    print(f"Deleted: {removed['title']}")

def main():
    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()