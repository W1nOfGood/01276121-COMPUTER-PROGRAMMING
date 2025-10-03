def process_commands():
    shopping_dict = {
        "egg": 1,
        "ham": 1,
        "water": 1,
        "soda": 1,
    }

    print("*** Shopping List 2 ***")
    commands = input("Enter some pairs of (operation, item): ").split(",")
    
    for command in commands:
        command_parts = command.strip().split(" ")
        
        if len(command_parts) != 2:
            print("Operation not supported!")
            return
        
        operation, item = command_parts
        item = item.lower()
        
        if operation == 'a':
            if item in shopping_dict:
                shopping_dict[item] += 1
            else:
                shopping_dict[item] = 1
                
        elif operation == 'r':
            if item in shopping_dict:
                shopping_dict[item] -= 1
                if shopping_dict[item] == 0:
                    shopping_dict.pop(item)
                    
        else:
            print("Operation not supported!")
            return
    
    print(f"Final shopping dict is {shopping_dict}")

process_commands()
