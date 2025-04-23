task = []

def add_task():
    print("welcome to to-do-list")
    print("Enter the number of tasks you want:")
    n = int(input())

    if n <= 0:
        taskss()

    for i in range(n):
        do = input(f"Enter your task {i+1} : ")
        task.append(do)
    print(task)

def remove_task():
    print("Enter the number of tasks you want Remove:")
    n = int(input())
    if 1 <= n <= len(task):
        del task[n-1]
    print(task)

def update_task():
    print("Enter the number of tasks you want to Update:")
    n = int(input())
    if 1 <= n <= len(task):
        del task[n-1]
        do = input(f"Enter your task {n} : ")
        task.insert(n-1,do)
    print(task)

def taskss():
    while True:
        print("1. View")
        print("2. Add task")
        print("3. Remove task")
        print("4. Update task")
        print("5. Exit")

        n  = int(input())
        if n == 1:
            if len(task) == 0:
                print("No tasks entered")
            else:
                print(task)
        elif n == 2:
            add_task()
        elif n == 3:
            remove_task()
        elif n == 4:
            update_task()
        elif n == 5:
            exit()



if __name__ == "__main__":
    taskss()
