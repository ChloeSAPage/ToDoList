while True :
    user_action = input("Add, Show, Edit, Complete or Exit ToDo's: ")
    user_action =  user_action.strip().lower()
    
    match user_action:
        case "add":
            todo = input("Enter a ToDo: ") +"\n"

            with open("ToDoList.txt", "r") as file:
                todo_list = file.readlines()

            todo_list.append(todo)
       
            with open("ToDoList.txt", "w") as file:
                file.writelines(todo_list)
        
        case "show":
            with open("ToDoList.txt", "r") as file:
               todo_list = file.readlines()
               print("Here is the List of ToDos:")
            
            #numbering each ToDo, removing the break line and print
            for index, item in enumerate(todo_list):
                item =  item.strip("\n")
                print(f"{(index)+1}. {item.capitalize()}")
        case "edit":
            #"show" case here as well for user knowledge
            with open("ToDoList.txt", "r") as file:
               todo_list = file.readlines()

            print("Here is the List of ToDos:")
            for index, item in enumerate(todo_list):
                        item =  item.strip("\n")
                        print(f"{(index)+1}. {item.capitalize()}")
            
            number = int(input("Number of To Do you wish to edit: ")) - 1
            print(f"Do you wish to edit {todo_list[number].strip()}?")
            yes_no = input()
            yes_no = yes_no.strip().lower()
            
            match yes_no:
                case "yes":
                    new_todo = input("Enter new ToDo: ") + "\n"
                    
                    with open("ToDoList.txt", "r") as file:
                         todo_list = file.readlines()

                    todo_list[number] = new_todo
                    
                    with open("ToDoList.txt", "w") as file:
                        file.writelines(todo_list)

                case "no":
                    continue
        case "complete":
           #"show" case for user knowledge
            with open("ToDoList.txt", "r") as file:
               todo_list = file.readlines()
               print("Here is the List of ToDos:")
           
            for index, item in enumerate(todo_list):
                item =  item.strip("\n")
                print(f"{(index)+1}. {item.capitalize()}")
            
            number = int(input("Number of To Do you wish to complete: ")) - 1
           
            print(f"Do you wish to complete {todo_list[number].strip().capitalize()}?")
            todo_to_remove = todo_list[number].strip().capitalize()
            yes_no = input()
            yes_no = yes_no.strip().lower()
            match yes_no:
                case "yes":
                    with open("ToDoList.txt", "r") as file:
                        todo_list = file.readlines()
                    
                    todo_list.pop(number)

                    with open("ToDoList.txt", "w") as file:
                        file.writelines(todo_list)
                    print(todo_to_remove, "was removed")
                case "no":
                    continue
        case "exit":
            print("Goodbye")
            break
        case _:
            print("Unknown Entry") 
        
        






