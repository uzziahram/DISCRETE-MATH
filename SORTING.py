import os

def Bubble_sort():
    os.system("cls")
    numbers = input("Enter numbers to sort (space separated): ")
    numbers = list(map(int, numbers.split()))
    n = len(numbers)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True
                print("Current state:", numbers)
        if not swapped:
            break
    
    print("Sorted numbers:", numbers)  
    
def Selection_sort():
    os.system("cls")
    unsorted = input("Enter numbers to sort (space separated): ")
    unsorted = list(map(int, unsorted.split()))
    n = len(unsorted)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if unsorted[j] < unsorted[min_idx]:
                min_idx = j
        unsorted[i], unsorted[min_idx] = unsorted[min_idx], unsorted[i]
        print("Current state:", unsorted)
   
    print("Sorted numbers:", unsorted)
    
def Insertion_sort():
    os.system("cls")
    unsorted = input("Enter numbers to sort (space separated): ")
    unsorted = list(map(int, unsorted.split()))
    n = len(unsorted)
    for i in range(1, n):
        key = unsorted[i]
        j = i - 1
        while j >= 0 and key < unsorted[j]:
            unsorted[j + 1] = unsorted[j]
            j -= 1
        unsorted[j + 1] = key
        print("Current state:", unsorted)
    
    print("Sorted numbers:", unsorted)
    
def Merge_sort():
    os.system("cls")
    unsorted = input("Enter numbers to sort (space separated): ")
    unsorted = list(map(int, unsorted.split()))
    
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])
        merged = merge(left_half, right_half)
        print("Current state:", merged)
        return merged
    
    sorted_numbers = merge_sort(unsorted)
    print("Sorted numbers:", sorted_numbers)


def Quick_sort():
    os.system("cls")
    unsorted = input("Enter numbers to sort (space separated): ")
    unsorted = list(map(int, unsorted.split()))
    
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        sorted_arr = quick_sort(left) + middle + quick_sort(right)
        print("Current state:", sorted_arr)
        return sorted_arr
    
    sorted_numbers = quick_sort(unsorted)
    print("Sorted numbers:", sorted_numbers)
    
def Bucket_sort():
    os.system("cls")
    unsorted = input("Enter numbers to sort (space separated): ")
    unsorted = list(map(int, unsorted.split()))
    max_value = max(unsorted)
    bucket = [[] for _ in range(max_value // 10 + 1)]
    for idx, num in enumerate(unsorted):
        bucket[num // 10].append(num)
        # Print buckets after each insertion
        print(f"Iteration {idx+1}: ", end="")
        for b_idx, b in enumerate(bucket):
            print(f"Bucket {b_idx}: {b}  ", end="")
        print()
    for i in range(len(bucket)):
        bucket[i] = sorted(bucket[i])
    sorted_numbers = [num for sublist in bucket for num in sublist]
    print("Sorted numbers:", sorted_numbers)
    
def Shell_sort():
    os.system("cls")
    unsorted = input("Enter numbers to sort (space separated): ")
    unsorted = list(map(int, unsorted.split()))
    n = len(unsorted)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = unsorted[i]
            j = i
            while j >= gap and unsorted[j - gap] > temp:
                unsorted[j] = unsorted[j - gap]
                j -= gap
            unsorted[j] = temp
            print("Current state:", unsorted)
        gap //= 2
    
    print("Sorted numbers:", unsorted)
    
def Comb_sort():
    os.system("cls")
    unsorted = input("Enter numbers to sort (space separated): ")
    unsorted = list(map(int, unsorted.split()))
    n = len(unsorted)
    gap = n
    shrink = 1.3
    sorted = False
    
    while not sorted:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1
        sorted = True
        
        for i in range(n - gap):
            if unsorted[i] > unsorted[i + gap]:
                unsorted[i], unsorted[i + gap] = unsorted[i + gap], unsorted[i]
                sorted = False
                print("Current state:", unsorted)
    
    print("Sorted numbers:", unsorted)
    
def Radix_sort():
    os.system("cls")
    unsorted = input("Enter numbers to sort (space separated): ")
    unsorted = list(map(int, unsorted.split()))
    
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1
        
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        for i in range(n - 1, -1, -1):
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            print("Current state:", output)
        
        for i in range(n):
            arr[i] = output[i]
    
    max_num = max(unsorted)
    exp = 1
    while max_num // exp > 0:
        counting_sort(unsorted, exp)
        exp *= 10
    
    print("Sorted numbers:", unsorted)
    
def Tree_sort():
    os.system("cls")
    unsorted = input("Enter numbers to sort (space separated): ")
    nums = list(map(int, unsorted.split()))
    if not nums:
        print("No numbers entered.")
        return

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert(self, value):
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)

        def inorder(self, result):
            if self.left:
                self.left.inorder(result)
            result.append(self.value)
            if self.right:
                self.right.inorder(result)

    # Build the BST
    root = Node(nums[0])
    for num in nums[1:]:
        root.insert(num)

    # In-order traversal to get sorted numbers
    sorted_numbers = []
    root.inorder(sorted_numbers)
    print("Sorted numbers:", sorted_numbers)
    
sorting = [
            "Bubble Sort",
            "Selection Sort",
            "Insertion Sort",
            "Merge Sort",
            "Quick Sort",
            "Bucket Sort",
            "Shell Sort",
            "Comb Sort",
            "Radix Sort",
            "Tree Sort"
         ]
running = True
while(running):
    os.system("cls")
    print("Sorting Algorithms")
    i = 1
    for sorter in sorting:
        print(f"{i}.", sorter)
        i = i + 1

    sorter = input("Choose Sorting Algorithm: ")
    match sorter:
        case "1":
            Bubble_sort()
        case "2":
            Selection_sort()
        case "3":
            Insertion_sort()
        case "4":
            Merge_sort()
        case "5":
            Quick_sort()
        case "6":
            Bucket_sort()
        case "7":
            Shell_sort()
        case "8":
            Comb_sort()
        case "9":
            Radix_sort()
        case "10":
            Tree_sort()
        
    restart = input("\nStart again? [y/n]: ")
    if restart.lower() == "n":
        running = False
        running = False

