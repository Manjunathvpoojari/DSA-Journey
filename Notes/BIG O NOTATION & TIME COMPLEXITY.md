===========================================================
🚀 BIG O NOTATION & TIME COMPLEXITY — INTERVIEW READY NOTES
===========================================================

1. WHAT IS BIG O?
-----------------
Big O notation is used to describe the efficiency of an algorithm. 
It measures how the RUNTIME or SPACE requirements grow as the 
INPUT SIZE (n) increases.

Key Rule: We always look at the "Worst Case Scenario."

-----------------------------------------------------------
2. THE BIG O HIERARCHY (Fastest to Slowest)
-----------------------------------------------------------

🟢 O(1) - Constant Time
-----------------------
Description: The time taken is independent of the input size.
How to spot: Basic math, accessing an array index, or variable assignment.
Example: 
    int val = arr[5]; 
    int sum = a + b;

🟡 O(log n) - Logarithmic Time
------------------------------
Description: The problem size is halved in every step. Extremely fast.
How to spot: Algorithms that "divide and conquer" or skip half the data.
Example: Binary Search.
Growth: To process 1,000,000 items, it only takes ~20 steps.

🟠 O(n) - Linear Time
---------------------
Description: Time grows directly with the number of elements.
How to spot: A single loop that visits every element once.
Example: 
    for(int i = 0; i < n; i++) { 
        System.out.println(arr[i]); 
    }

🔵 O(n log n) - Linearithmic Time
---------------------------------
Description: Performing a log n operation n times.
How to spot: Most efficient sorting algorithms.
Example: Merge Sort, Quick Sort, Heap Sort.
Note: This is the best time complexity possible for comparison-based sorting.

🔴 O(n^2) - Quadratic Time
--------------------------
Description: Time grows as the square of the input size.
How to spot: Nested loops (a loop inside a loop).
Example: 
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            // Logic
        }
    }
Warning: Avoid O(n^2) for inputs larger than 10,000.

-----------------------------------------------------------
3. PERFORMANCE COMPARISON (The "1ms per operation" Rule)
-----------------------------------------------------------

If 1 operation takes 1ms, here is how long the algorithm takes:

n (Elements) | O(log n) | O(n)      | O(n log n) | O(n^2)
-----------------------------------------------------------
10           | 3 ms     | 10 ms     | 30 ms      | 100 ms
100          | 7 ms     | 100 ms    | 700 ms     | 10 seconds
1,000        | 10 ms    | 1 second  | 10 seconds | 16.6 minutes
1,000,000    | 20 ms    | 16.6 mins | 5.5 hours  | 31.7 YEARS!!

-----------------------------------------------------------
4. INTERVIEW CHEAT SHEET: HOW TO CALCULATE
-----------------------------------------------------------

1. Drop Constants: O(2n) becomes O(n). O(500) becomes O(1).
2. Drop Non-Dominant Terms: O(n^2 + n) becomes O(n^2).
3. Different Inputs: If you have two different arrays, use two 
   variables. Example: O(a + b) or O(a * b).

-----------------------------------------------------------
5. SPACE COMPLEXITY (Quick Tip)
-----------------------------------------------------------
It's the same logic, but for MEMORY instead of time.
- If you create a new array of size n -> O(n) Space.
- If you only use a few variables -> O(1) Space.

===========================================================
🔥 MASTER TIP: 
If an interviewer asks for a "Better than O(n^2)" solution, 
they usually want O(n log n) or O(n).
===========================================================