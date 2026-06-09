tasks = []

try:
    with open("tasks.txt","r") as fs:
        tasks = [line.strip() for line in fs.readlines()]

except FileNotFoundError:
    tasks = []


def save_tasks_to_file():
    with open("tasks.txt", "w") as fs:
        for task in tasks:
            fs.write(task + "\n")
   
while True:
    print(" Press 1 for Add task\n Press 2 for View tasks\n Press 3 for Update task\n Press 4 for Delete task\n Press 5 for Mark Task as Done\n Press 6 for Exit")
  
    try:
      res = int(input("What do you want to do :"))
    except Exception as err:
      print("please enter valid number!")
      continue

    
    if res==1:
        try:
           task = int(input("Enter how many tasks you want to add :"))

           for i in range(task):
                task_name = input("Enter your task name : ")
                task_with_status = task_name + " | Pending"
                tasks.append(task_with_status)

           save_tasks_to_file()
           print("All tasks added successfully")

        except Exception as err:
            print(err)
    
    
    elif res==2:
            if not tasks :
                print("No Tasks available")
            else:
                print("Your tasks:")
                for i,task_name in enumerate(tasks):
                    print(f"{i+1}. {task_name}")


    elif res==3:
            if not tasks:
                print("No Tasks to update")
            else:
                try: 
                    print("Your current Tasks:")
                    for i,task_name in enumerate(tasks):
                      print(f"{i+1}. {task_name}")

                    
                    task2 = int(input("Enter which task number you want to change:"))
                   
                    if 1<=task2<=len(tasks):
                        
                        selected_task = tasks[task2-1]
                        
                        # old_name , status = selected_task.split(" | ")

                        parts = selected_task.split("|")

                        old_name = parts[0].strip()
                        
                        status = parts[1].strip()

                        new_task = input("Enter new task:")
                        
                        update_task = new_task +  " | " + status
                        
                        tasks[task2 - 1] = update_task
                        
                        save_tasks_to_file()
                        print("Task updated successfully")
                    else:
                        print("Invalid Task number")
                except Exception as err:
                    print(err)

                    
    elif res==4:
            if not tasks:
                print("No Tasks to delete")
            else:
                print("Your current Tasks:")
                for i,task in enumerate(tasks):
                    print(f"{i+1}. {task}")
                try:
                    nums = input("Enter which task you want to delete (comma separated):")
                    num_list = nums.split(",")
                    indices = []
                    for n in num_list:
                        indices.append(int(n.strip()))

                    indices = list(set(indices))
                    indices.sort(reverse=True)
                    for i in indices:
                      
                      if 1<=i<=len(tasks):
                        del tasks[i-1]
                      else:
                        print("invalid task")


                    save_tasks_to_file()
                    print("Tasks Deleted successfully")

                except Exception as err:
                    print("error occurred",err)
        
    
    elif res == 5:
        if not tasks :
            print("No Tasks available")
        else:
            print("Your tasks:")
            for i,task_name in enumerate(tasks):
                print(f"{i+1}. {task_name}")
            
            mark_task = int(input("Enter task number to mark as done :"))
           
            if 1 <= mark_task <= len(tasks):
                
                selected_task = tasks[mark_task -1]
                task_name , status = selected_task.split(" | ")
               
                if status == "Done":
                    print("Task already done")
                else:
                    status = "Done"
                    update_task = task_name + " | " + status
                    tasks[mark_task -1] = update_task
                    save_tasks_to_file()
                    print("Task Marked as Done successfully")
            else:
                print("Invalid Task number")        

    elif res==6:
            print("exit!!")
            break