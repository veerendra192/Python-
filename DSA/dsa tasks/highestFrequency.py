def high_freq(arr):
    frequency = {}
    for i in arr:
        frequency[i] = frequency.get(i, 0) + 1
    return max(frequency, key=frequency.get)


array = list(map(int, input("Enter the numbers ").strip().split()))

highest_frequency_element = high_freq(array)
print("Element highest frequency:", highest_frequency_element)
