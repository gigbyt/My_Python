A = []

def add_items():
    while True:
        item = input("Enter a value to add (or press Enter to finish): ").strip()
        if item == "":
            break
        A.append(item)
        print("Added:", item)

def show_list():
    print("\nCurrent list:")
    for i, v in enumerate(A, 1):
        print(f"{i}. {v}")
    print()

def remove_item():
    show_list()
    try:
        idx = int(input("Enter index to remove (0 to cancel): "))
    except ValueError:
        print("Invalid input.")
        return
    if idx == 0:
        return
    if 1 <= idx <= len(A):
        removed = A.pop(idx - 1)
        print("Removed:", removed)
    else:
        print("Index out of range.")

def main():
    print("Start adding items to the list.")
    add_items()

    while True:
        show_list()
        confirm = input("Confirm final list? (y/n): ").strip().lower()
        if confirm == "y":
            print("Final list confirmed:")
            show_list()
            break
        elif confirm == "n":
            action = input("Choose: (a)dd more, (r)emove item, (s)tart over, (q)uit without confirming: ").strip().lower()
            if action == "a":
                add_items()
            elif action == "r":
                remove_item()
            elif action == "s":
                A.clear()
                print("List cleared. Add items again.")
                add_items()
            elif action == "q":
                print("Exited without confirming. Current list:")
                show_list()
                break
            else:
                print("Unknown option.")
        else:
            print("Please answer 'y' or 'n'.")

if __name__ == "__main__":
    main()