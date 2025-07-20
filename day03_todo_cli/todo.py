# Day 3 - CLI To-Do App

tasks = []

while True:
    action = input("Add/View/Remove/Quit: ").lower()
    if action == "add":
        task = input("Enter task: ")
        tasks.append(task)
    elif action == "view":
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
    elif action == "remove":
        num = int(input("Enter task number to remove: ")) - 1
        if 0 <= num < len(tasks):
            tasks.pop(num)
    elif action == "quit":
        break
    else:
        print("Invalid command")
