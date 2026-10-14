approved_models =("MacBook Pro", "Dell XPS", "ThinkPad", "Airpod Pro")
device_inventory =[]

while True:
    print("\nIT Inventory Menu")
    print("1: Add")
    print("2: Remove")
    print("3: View")
    print("4: Exit")
    
    user_choice = input("Choose an option: ")
    
    if user_choice == "1":
        print(approved_models)
        device = input("Enter device name: ")

        if device in approved_models:
            device_inventory.append(device)
            print("Device added.")
        else:
            print("Error: Device model not approved for company use.")

    
    elif user_choice == "2":
        device = input("Enter device to remove: ")

        if device in device_inventory:
            device_inventory.remove(device)
            print("Device removed.")
        else:
            print("Device not found.")

    elif user_choice == "3":
        print(device_inventory)

    elif user_choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Choose 1, 2, 3, or 4.")
