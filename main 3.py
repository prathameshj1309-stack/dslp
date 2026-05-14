# Python Program for Linear Search and Binary Search
# in an E-commerce Customer Account System

# Function for Linear Search
def linear_search(accounts, key):
    for i in range(len(accounts)):
        if accounts[i] == key:
            return i
    return -1

# Function for Binary Search
def binary_search(accounts, key):
    low = 0
    high = len(accounts) - 1

    while low <= high:
        mid = (low + high) // 2

        if accounts[mid] == key:
            return mid

        elif accounts[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# Input customer account IDs
n = int(input("Enter number of customer account IDs: "))

accounts = []

for i in range(n):
    acc_id = int(input(f"Enter Account ID {i+1}: "))
    accounts.append(acc_id)

# Sort list for Binary Search
accounts.sort()

print("\nSorted Customer Account IDs:")
print(accounts)

# Input account ID to search
key = int(input("\nEnter Customer Account ID to search: "))

# Linear Search
result1 = linear_search(accounts, key)

if result1 != -1:
    print("\nLinear Search:")
    print("Customer Account ID found at position", result1 + 1)
else:
    print("\nLinear Search:")
    print("Customer Account ID not found")

# Binary Search
result2 = binary_search(accounts, key)

if result2 != -1:
    print("\nBinary Search:")
    print("Customer Account ID found at position", result2 + 1)
else:
    print("\nBinary Search:")
    print("Customer Account ID not found")


# Complexity Analysis
print("\n----- Complexity Analysis -----")

print("\n1. Linear Search:")
print("   Best Case Time Complexity    : O(1)")
print("   Worst Case Time Complexity   : O(n)")
print("   Space Complexity             : O(1)")

print("\n2. Binary Search:")
print("   Best Case Time Complexity    : O(1)")
print("   Worst Case Time Complexity   : O(log n)")
print("   Space Complexity             : O(1)")