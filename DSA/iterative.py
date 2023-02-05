def count_freq(li, l):
    frequency = [0] * 100
    for i in range(l):
        frequency[li[i]] += 1
    for i in range(100):
        if frequency[i] > 1:
            print("Frequency of", i, "is ", frequency[i])

li = list(map(int,input("Enter nums:").split()))
l = len(li)
count_freq(li, l)