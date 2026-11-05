import random
import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)

def heap_sort(arr):
    import heapq
    h = arr[:]
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # merge
    res = []
    i=j=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i]); i+=1
        else:
            res.append(right[j]); j+=1
    res.extend(left[i:]); res.extend(right[j:])
    return res

def benchmark():
    sizes = [1000, 5000, 10000, 20000, 50000]
    results = {"Heap": [], "Quick": [], "Merge": []}
    
    for n in sizes:
        arr = [random.randint(0, 1000000) for _ in range(n)]
        
        for name, func in [("Heap", heap_sort), ("Quick", quick_sort), ("Merge", merge_sort)]:
            start = time.time()
            func(arr.copy())
            results[name].append(time.time() - start)
            print(f"{name} n={n} done")

    # Plot
    for name in results:
        plt.plot(sizes, results[name], marker='o', label=name)
    plt.xlabel("Array Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Heap vs Quick vs Merge Sort")
    plt.legend()
    plt.grid(True)
    plt.savefig("benchmark.png")
    print("Saved benchmark.png")
    plt.show()

if __name__ == "__main__":
    benchmark()