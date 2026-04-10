============================================================
           ARRAYS & STRINGS - EXAM REVISION NOTES
============================================================

------------------------------------------------------------
: ARRAYS BASICS
------------------------------------------------------------
1. DEFINITION
   - A collection of elements of the same data type.
   - Stored in contiguous (adjacent) memory locations.
   - Index-based: Starts at 0, ends at (length - 1).

2. DECLARATION (Java)
   - 1D Array: int[] arr = new int[5];
   - 2D Array: int[][] matrix = new int[3][3];

3. OPERATIONS & TIME COMPLEXITY
   - Access: O(1) -> Fast because of direct indexing.
   - Search (Linear): O(n) -> Check every element.
   - Search (Binary): O(log n) -> Only for sorted arrays.
   - Insert/Delete: O(n) -> Requires shifting elements.

4. KEY PROPERTIES
   - Fixed Size: Cannot grow or shrink once declared.
   - Memory Efficient: No extra overhead per element.

5. COMMON PROBLEMS
   - Find Max/Min: Use a loop and a 'max' variable.
   - Reverse: Use Two-Pointer technique.
   - Kadane’s Algorithm: Used for Max Subarray Sum.

------------------------------------------------------------
: STRINGS & IMMUTABILITY
------------------------------------------------------------
1. DEFINITION
   - A sequence of characters. In Java, Strings are Objects.
   - String s = "Hello";

2. THE IMMUTABILITY RULE
   - Strings cannot be changed once created.
   - Any modification (like s + "!") creates a NEW object.
   - Why? Security, Thread-safety, and String Pool caching.

3. MUTABLE ALTERNATIVES
   - StringBuilder: Fast, used for single-threaded tasks.
   - StringBuffer: Thread-safe, used for multi-threaded tasks.

4. ESSENTIAL METHODS
   - length(): Returns number of characters.
   - charAt(i): Returns char at specific index.
   - substring(start, end): Extracts part of a string.
   - equals(): Compares content (Use this, NOT '==').
   - trim(): Removes leading/trailing spaces.

5. PERFORMANCE TIP
   - Accessing a char is O(1).
   - Concatenating in a loop using "+" is O(n^2). Use StringBuilder!

------------------------------------------------------------
: LOGIC PATTERNS (CRITICAL)
------------------------------------------------------------
1. TWO-POINTER TECHNIQUE
   - Use: Reversing, Palindromes, Pair Sum.
   - Logic: 
     int left = 0, right = arr.length - 1;
     while (left < right) {
         // swap or compare
         left++; right--;
     }

2. SLIDING WINDOW
   - Use: Maximum sum of 'k' consecutive elements.
   - Logic: Add next element, remove first element of window.

3. FREQUENCY COUNTING (HASHING)
   - Use: Anagrams, checking duplicates.
   - Logic:
     int[] freq = new int[26];
     for(char c : str.toCharArray()) {
         freq[c - 'a']++;
     }

4. ARRAY VS STRING COMPARISON
   - Array: Mutable, primitive/object, [] access.
   - String: Immutable, object, charAt() access.

============================================================
                   END OF NOTES
============================================================