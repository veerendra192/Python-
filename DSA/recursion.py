def dup_element(li, l, frequency, i):
    if i == l:
        return
    frequency[li[i]] += 1
    dup_element(li, l, frequency, i+1)

def count_freq(li, l):
    frequency = [0] * 100
    dup_element(li, l, frequency, 0)
    for i in range(100):
        if frequency[i] > 1:
            print("frequency of", i, "is ", frequency[i])

li = list(map(int,input("Enter Numbers: ").split()))
l = len(li)
count_freq(li, l)