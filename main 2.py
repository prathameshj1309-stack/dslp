# Real-Time Undo/Redo System using Stack in Python

# Stacks for undo and redo operations
undo_stack = []
redo_stack = []

# Current document state
document = ""

# Function to make a change
def make_change(new_text):
    global document
    
    # Save current state to undo stack
    undo_stack.append(document)
    
    # Clear redo stack because new action is performed
    redo_stack.clear()
    
    # Apply new change
    document += new_text
    
    print("\nChange Applied Successfully!")
    display_document()

# Function to undo last change
def undo():
    global document
    
    if len(undo_stack) == 0:
        print("\nNothing to Undo!")
    else:
        # Save current state to redo stack
        redo_stack.append(document)
        
        # Restore previous state
        document = undo_stack.pop()
        
        print("\nUndo Performed!")
        display_document()

# Function to redo last undone change
def redo():
    global document
    
    if len(redo_stack) == 0:
        print("\nNothing to Redo!")
    else:
        # Save current state to undo stack
        undo_stack.append(document)
        
        # Restore redone state
        document = redo_stack.pop()
        
        print("\nRedo Performed!")
        display_document()

# Function to display document
def display_document():
    print("Current Document State:")
    print(document)

# Menu-driven program
while True:
    print("\n----- TEXT EDITOR MENU -----")
    print("1. Make Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        text = input("Enter text to add: ")
        make_change(text)
        
    elif choice == 2:
        undo()
        
    elif choice == 3:
        redo()
        
    elif choice == 4:
        display_document()
        
    elif choice == 5:
        print("\nExiting Program...")
        break
        
    else:
        print("\nInvalid Choice! Please try again.")

# Complexity Analysis
print("\n----- Complexity Analysis -----")

print("1. Make Change:")
print("   Time Complexity  : O(1)")
print("   Space Complexity : O(n)")

print("\n2. Undo Operation:")
print("   Time Complexity  : O(1)")
print("   Space Complexity : O(n)")

print("\n3. Redo Operation:")
print("   Time Complexity  : O(1)")
print("   Space Complexity : O(n)")

print("\n4. Display Document:")
print("   Time Complexity  : O(1)")
print("   Space Complexity : O(1)")