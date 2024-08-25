# Install PyInputPlus with:
#       pip install PyInputPlus
import pyinputplus as pyip
import sqlite3 as sql


def printplus(name: str, status: int, true_status: int):
    if status == true_status:
        print(f"Task: {name} -> [\u2713]")
    else:
        print(f"Task: {name} -> [\u2717]")


def printline():
    print('--------------------------------------')


class TodoList:
    def __init__(self):
        self.db = sql.connect('todolist.db')
        self.cursor = self.db.cursor()
        self.cursor.execute('''create table if not exists tasks (
                        task_title TEXT,
                        status BOOLEAN
                            )''')

    def add_task(self, task_title):
        self.cursor.execute(
            '''INSERT INTO tasks (task_title, status) VALUES (?, ?)''',
            (task_title, False))
        self.db.commit()

    def remove_task(self, task_title):
        self.cursor.execute(
            '''DELETE FROM tasks WHERE task_title = ?''',
            (task_title,))
        self.db.commit()

    def task_complete(self, task_title=None):
        self.cursor.execute(
            '''UPDATE tasks SET status = ? WHERE task_title = ?''',
            (True, task_title))
        self.db.commit()

    def unfinished_tasks(self):
        tasks = self.cursor.execute(
            '''SELECT * from tasks''').fetchall()
        count = 0
        tasks_list = []
        if len(tasks) != 0:
            print("\nUnfinished tasks: ")
            for task in tasks:
                if task[1] == 0:
                    print(f"Task: {task[0]}")
                    count += 1
                    tasks_list.append(task[0])
            if count == 0:
                print("All of your task is finished!")
        else:
            print("To-Do list is empty!")
        return count, tasks_list

    def show_tasks(self):
        tasks = self.cursor.execute(
            '''SELECT * from tasks''').fetchall()
        tasks_list = []
        if len(tasks) != 0:
            print("Tasks: ")
            for task in tasks:
                tasks_list.append(task[0])
                printplus(task[0], task[1], 1)
        else:
            print("To-Do list is empty!")
        return len(tasks), tasks_list


todo = TodoList()


while True:
    operation = pyip.inputMenu(
        ['add task', 'remove task', 'complete task', 'show todolist', 'quit'],
        numbered=True,
        prompt='Please select operation\n'
    )
    printline()
    print(f'Your operation is "{operation}"')

    match operation:
        case 'add task':
            task_title = input("Plaese input task title or cancel operation: ")
            if task_title != 'cancel':
                todo.add_task(task_title)
            printline()

        case 'remove task':
            number_of_tasks, tasks = todo.show_tasks()
            tasks.append('cancel')
            if number_of_tasks > 0:
                task_title = pyip.inputMenu(tasks,
                                            numbered=True,
                                            prompt='Please select task:\n'
                                            )
                if task_title != 'cancel':
                    todo.remove_task(task_title)
            printline()

        case 'complete task':
            number_of_unfinished_tasks, unfinished_tasks = todo.unfinished_tasks()
            unfinished_tasks.append('cancel')
            if number_of_unfinished_tasks > 0:
                task_title = pyip.inputMenu(unfinished_tasks,
                                            numbered=True,
                                            prompt='Please select task:\n'
                                            )
                if task_title != 'cancel':
                    todo.task_complete(task_title)
            printline()

        case 'show todolist':
            todo.show_tasks()
            printline()

        case 'quit':
            print('Thanks!')
            break
