# Heap vs Quick vs Merge

Benchmark the three sorts and explain the gaps (cache behaviour).

**Tools:** Python, matplotlib

**Run:** python sorting_benchmark.py

**Explanation:**
- QuickSort is fastest on average because it's cache-friendly, data stays in CPU cache, and partitions are in-place.
- MergeSort is stable but needs extra memory, causes more cache misses when copying between arrays.
- HeapSort has worst cache behaviour, random memory jumps in heap structure cause many cache misses, so it's slower even with O(n log n).

**Result graph:** benchmark.png
