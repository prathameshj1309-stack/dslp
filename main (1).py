# Python Program to Manage Borrowing Records in a Library

# Input number of books
n = int(input("Enter number of books: "))

books = []
borrow_counts = []

# Input book names and borrow counts
for i in range(n):
    book = input(f"\nEnter name of book {i+1}: ")
    count = int(input(f"Enter borrow count for '{book}': "))
    
    books.append(book)
    borrow_counts.append(count)

# 1. Calculate Average Borrow Count
average = sum(borrow_counts) / n
print("\nAverage number of books borrowed:", average)

# 2. Find Highest and Lowest Borrowed Books
max_count = max(borrow_counts)
min_count = min(borrow_counts)

max_index = borrow_counts.index(max_count)
min_index = borrow_counts.index(min_count)

print("\nMost Borrowed Book:")
print(books[max_index], "with", max_count, "borrowings")

print("\nLeast Borrowed Book:")
print(books[min_index], "with", min_count, "borrowings")

# 3. Count Members/Books with Zero Borrowings
zero_count = borrow_counts.count(0)

print("\nNumber of books not borrowed:", zero_count)

# 4. Find Mode (Most Frequently Occurring Borrow Count)
frequency = {}

for count in borrow_counts:
    if count in frequency:
        frequency[count] += 1
    else:
        frequency[count] = 1

mode = max(frequency, key=frequency.get)

print("\nMost Frequent Borrow Count (Mode):", mode)

# Time and Space Complexity
print("\n----- Complexity Analysis -----")

print("1. Average Calculation:")
print("   Time Complexity  : O(n)")
print("   Space Complexity : O(1)")

print("\n2. Highest and Lowest Borrowed Book:")
print("   Time Complexity  : O(n)")
print("   Space Complexity : O(1)")

print("\n3. Counting Zero Borrowings:")
print("   Time Complexity  : O(n)")
print("   Space Complexity : O(1)")

print("\n4. Finding Mode:")
print("   Time Complexity  : O(n)")
print("   Space Complexity : O(n)")