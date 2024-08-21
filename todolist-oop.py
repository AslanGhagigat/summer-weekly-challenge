# Install PyInputPlus with:
#       pip install PyInputPlus
import pyinputplus as pyip


class TodoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_title):
        self.tasks.update({task_title: False})

    def task_complete(self, task_title):
        if task_title in self.tasks:
            self.tasks[task_title] = True
        else:
            print("Task Does't exist!")

    def remove_task(self, task_title):
        self.tasks.pop(task_title)

    def unfinished_tasks(self):
        print("\nUnfinished tasks: ")
        for task in self.tasks:
            if task:
                print(f"Task: {task}")

    def show_tasks(self):
        print("Tasks: ")
        for task in self.tasks:
            print(
                f"Task: {task} -> [{(u'\u2713') if self.tasks[task] else (u'\u2717')}]")


todo = TodoList()

while True:
    user_input = pyip.inputMenu(
        ['add task', 'remove task', 'complete task', 'show todolist', 'quit'],
        numbered=True,
        prompt='Please select operation\n'
    )
    print('--------------------------------------')
    print(f'Your operation is "{user_input}"')

    match user_input:
        case 'add task':
            task_title = input("Plaese input task title: ")
            todo.add_task(task_title)
            print('--------------------------------------')
        case 'remove task':
            task_title = input("Plaese input task title: ")
            todo.remove_task(task_title)
            print('--------------------------------------')
        case 'complete task':
            todo.unfinished_tasks()
            print('--------------------------------------')
            task_title = input("Plaese input task title: ")
            todo.task_complete(task_title)
            print('--------------------------------------')
        case 'show todolist':
            todo.show_tasks()
            print('--------------------------------------')
        case 'quit':
            print('Thanks!')
            break
