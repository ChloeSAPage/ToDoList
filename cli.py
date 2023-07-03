import functions
import time

current_time = time.strftime("%b %d %Y %H:%S")
print(f"It is currently {current_time}")

while True :
    user_action = input("Add, Show, Edit, Complete or Exit ToDo's: ")
    user_action =  user_action.strip().lower()
    todo_list = functions.get_todos()

    if user_action.startswith ("add"):

        user_action_split = user_action.split(" ", 1) 
        todo = user_action_split[1]+ "\n"

        todo_list.append(todo)
    
        functions.write_todos(todo_list)
    
    elif user_action.startswith ("show"):
        functions.show_todo(todo_list)

    elif user_action.startswith ("edit"):
        #"show" case here as well for user knowledge
        functions.show_todo(todo_list)
        try:
            user_action_split = user_action.split(" ", 1) 
            
            number = int(user_action_split[1]) - 1 
            
            yesno = functions.yes_no("edit", number, todo_list)
            
            match yesno:
                case "yes":
                    new_todo = input("Enter new ToDo: ") + "\n"
                    
                    todo_list = functions.get_todos()

                    todo_list[number] = new_todo
                    
                    functions.write_todos(todo_list)

                case "no":
                        continue
        except (ValueError, IndexError):
            print("Please Enter the number of the ToDo you wish to edit")
            continue
            
    elif  user_action.startswith ("complete"):
        #"show" case for user knowledge
        functions.show_todo(todo_list)
        try:
            user_action_split = user_action.split(" ", 1) 

            number = int(user_action_split[1]) - 1
            todo_to_remove = todo_list[number].strip().capitalize()
            
            yesno = functions.yes_no("complete", number, todo_list)
            
            match yesno:
                case "yes":
                    todo_list = functions.get_todos()

                    todo_list.pop(number)

                    functions.write_todos(todo_list)

                    print(todo_to_remove, "was removed")
                case "no":
                    continue
        except ValueError:
            print("Please Enter the number of the ToDo you wish to complete")
            continue
        except IndexError:
             print("There is no ToDo with that number")
             continue

    elif user_action.startswith ("exit"):
        print("Goodbye")
        break
    else:
        print("Unknown Entry") 
        
        






