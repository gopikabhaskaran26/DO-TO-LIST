def edit_task(tasks):
    display_tasks(tasks)
    try:
        task_id = int(input(Fore.BLUE + "Which task number do you want to update? "))
        for task in tasks:
            if task['id'] == task_id:
                task['description'] = input(Fore.BLUE + "New task description: ").strip()
                deadline = input(Fore.BLUE + "New deadline (YYYY-MM-DD): ").strip()
                priority = input(Fore.BLUE + "New priority (High/Medium/Low): ").strip().capitalize()
                if priority not in ["High", "Medium", "Low"]:
                    priority = "Medium"
                datetime.strptime(deadline, "%Y-%m-%d")
                task['deadline'] = deadline
                task['priority'] = priority
                save_tasks(tasks)
                print(Fore.GREEN + "✅ Task updated!\n")
                return
        print(Fore.RED + "Hmm, couldn’t find that task.\n")
    except ValueError:
        print(Fore.RED + "Something went wrong. Please enter valid info.\n")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_id = int(input(Fore.BLUE + "Which task number do you want to delete? "))
        confirm = input(Fore.RED + "Are you sure? This can't be undone (y/n): ").lower()
        if confirm != 'y':
            print(Fore.YELLOW + "Whew! Nothing was deleted.\n")
            return

        new_tasks = [t for t in tasks if t['id'] != task_id]
        if len(new_tasks) != len(tasks):
            save_tasks(new_tasks)
            print(Fore.GREEN + "🗑 Task deleted!\n")
        else:
            print(Fore.RED + "Couldn’t find that task.\n")
    except ValueError:
        print(Fore.RED + "Please enter a valid task number.\n")

def mark_completed(tasks):
    display_tasks(tasks)
    try:
        task_id = int(input(Fore.BLUE + "Which task is done? Enter its number: "))
        for task in tasks:
            if task['id'] == task_id and task['status'] == "Pending":
                task['status'] = "Completed"
                save_tasks(tasks)
                print(Fore.GREEN + "✅ Task marked as done!\n")
                return
        print(Fore.RED + "That task’s already completed or not found.\n")
    except ValueError:
        print(Fore.RED + "Please enter a valid number.\n")

def main():
    username = getpass.getuser()
    print(Fore.LIGHTCYAN_EX + f"\n👋 Hey there, {username}! Ready to conquer your tasks?")

    while True:
        print(Fore.CYAN + "="*40)
        print(Fore.MAGENTA + Style.BRIGHT + "🌟 Task Manager Buddy")
        print(Fore.CYAN + "="*40)
        print(Fore.LIGHTBLUE_EX + "1. ➕ Add a New Task")
        print("2. 📋 See My Tasks")
        print("3. ✏️ Update a Task")
        print("4. ❌ Remove a Task")
        print("5. ✅ Mark Something Done")
        print("6. 🚪 Exit")

        choice = input(Fore.YELLOW + "\nWhat do you want to do? ").strip()
        tasks = load_tasks()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_completed(tasks)
        elif choice == "6":
            print(Fore.LIGHTMAGENTA_EX + "Catch you later! Keep up the great work! 👋")
            break
        else:
            print(Fore.RED + "Oops! Not a valid choice. Try again.\n")

if name == "main":
    main()
