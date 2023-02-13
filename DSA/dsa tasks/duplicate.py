def find_duplicates(arr):
    duplicates = []
    for i in arr:
        if arr.count(i) > 1:
            if i not in duplicates:
                duplicates.append(i)
    return duplicates

array = list(map(int, input("Enter Numbers: ").strip().split()))

duplicates = find_duplicates(array)
if duplicates:
    print("Duplicate elements in the list:", duplicates)
else:
    print("No duplicate elements in the list.")
