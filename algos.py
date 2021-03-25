#!/usr/bin/python3

def comapareArrays(a,b):
    if len(a) != len(b): return False
    i=0;
    while (i < len(a)):
        if(a[i] != b[i]): return False
        i+=1
    return True

def selectionSort(ar):
    m = len(ar)
    last = 0
    while last < m:
        minn = last
        for i in range(last, len(ar)):
            if ar[i] < ar[minn]:
                minn = i
        b = ar[last]
        a = ar[minn]
        ar[last] = a
        ar[minn] = b
        last += 1
    return ar

def insertionSort(ar):
    k = ar[0]
    for i in range(1, len(ar)):
        j = i
        t = ar[i]
        k = t
        while (ar[j-1] > k):
            ar[j]=ar[j-1]
            j-= 1
        ar[j] = t
    return ar

"""
    Ich bin definitiv zu blöd um Quicksort zu implementieren
    --> RAUSCHEN IM KOPF! fuck off
"""
def quickSort(daten, links, rechts):
    i = links
    j = rechts
    pivot = daten[j]
    if i > j: return daten
    if daten[i] > pivot:
        di = daten[i]
        daten[i] = pivot
        daten[j] = di
    daten = quickSort(daten, links+1, rechts)
    daten = quickSort(daten, links, rechts-1)
    return daten

def runTests():
    expected = [0,10,30,40,200,227,600,4000]
    ar = [227, 0,10,200,4000,30,40,600]
    a = selectionSort(ar)
    assert comapareArrays(a, expected), "[-] The output is different than expected for selectionSort"
    print("[+] selectionSort Test passed")

    expected = [10,30,40,200,400,4000]
    ar1 = [10,400,40,30,4000,200]
    b = insertionSort(ar1)
    assert comapareArrays(b, expected), "[-] The output is different than expected for insertSort"
    print("[+] insertSort Test passed")

    expected = [10,30,40,200,400,4000]
    ar1 = [10,400,40,30,4000,200]
    b = quickSort(ar1, 0,len(ar1)-1)
    assert comapareArrays(b, expected), "[-] The output is different than expected for quickSort"
    print("[+] quickSort Test passed")
    
if __name__ == "__main__":
    runTests()
