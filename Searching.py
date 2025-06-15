import os
os.system("cls")

print("Searching Algorithms")
searching = [
    "Linear Search",
    "Binary Search",
    "Interpolation Search",
]

def Linear_search():
    os.system("cls")
    numbers = input("Enter numbers (space separated): ")
    numbers = list(map(int, numbers.split()))
    target = int(input("Enter number to search for: "))
    found = False
    for idx, num in enumerate(numbers):
        print(f"Checking index {idx}: {num}")
        if num == target:
            print(f"Number {target} found at index {idx}.")
            found = True
            break
    if not found:
        print(f"Number {target} not found in the list.")

def Binary_search():
    os.system("cls")
    numbers = input("Enter sorted numbers (space separated): ")
    numbers = list(map(int, numbers.split()))
    target = int(input("Enter number to search for: "))
    
    left, right = 0, len(numbers) - 1
    found = False
    
    while left <= right:
        mid = (left + right) // 2
        print(f"Checking middle index {mid}: {numbers[mid]}")
        
        if numbers[mid] == target:
            print(f"Number {target} found at index {mid}.")
            found = True
            break
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    if not found:
        print(f"Number {target} not found in the list.")
        
def Interpolation_search():
    os.system("cls")
    numbers = input("Enter sorted numbers (space separated): ")
    numbers = list(map(int, numbers.split()))
    target = int(input("Enter number to search for: "))

    low = 0
    high = len(numbers) - 1
    found = False

    while low <= high and target >= numbers[low] and target <= numbers[high]:
        if low == high:
            if numbers[low] == target:
                print(f"Number {target} found at index {low}.")
                found = True
            break

        # Interpolation formula
        pos = low + ((high - low) // (numbers[high] - numbers[low]) * (target - numbers[low]))

        if numbers[pos] == target:
            print(f"Number {target} found at index {pos}.")
            found = True
            break
        elif numbers[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    if not found:
        print(f"Number {target} not found in the list.")
       
running = True 
while running:
    os.system("cls")
    print("Searching Algorithms")
    for i, algo in enumerate(searching, start=1):
        print(f"{i}. {algo}")

    choice = input("Choose an algorithm: ")

    match choice:
        case '1':
            Linear_search()
        case '2':
            Binary_search()
        case '3':
            Interpolation_search()
            

    decision = input("\nDo you want to continue? (y/n): ")
    if decision.lower() == 'n':
       running = False
       os.system("cls")
       print("Exiting the program.")