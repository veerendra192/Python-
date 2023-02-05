def check_element(li, l, freq, x):
    for i in range(l):
        if li[i] == x:
            freq[x] += 1

def count_freq(li, l):
    freq = [0] * 100
    for i in range(100):
        check_element(li, l, freq, i)
    for i in range(100):
        if freq[i] > 1:
            print("Frequency of", i, "is ", freq[i])

li = list(map(int,input("Enter Numbers: ").split()))
l = len(li)
count_freq(li, l)