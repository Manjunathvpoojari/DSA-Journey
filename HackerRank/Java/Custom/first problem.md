------------------------------
## Problem Description: Integer Array Boundary Filtering and Averaging
Objective:
Write the main method within a class named Solution. The method should process a set of user inputs to calculate and display the integer average of specific elements within an array based on two boundary limits.
Detailed Requirements:

   1. Input Collection:
   * Read five (5) integer values from the standard input and store them in an integer array.
      * Read two (2) additional integer values representing the boundaries: limit1 and limit2.
   2. Logic:
   * Identify all elements within the array that are strictly greater than limit1 AND less than limit2.
      * Calculate the average of these identified integer values.
   3. Output:
   * Print the calculated average to the console.
      * Data Type Constraint: The returned average value must be of the int data type (integer division should be used).
   
Example Scenario:

* Input Values: 1, 2, 3, 4, 5
* Limits: limit1 = 2, limit2 = 6
* Filtering: The values greater than 2 and less than 6 are 3, 4, and 5.
* Calculation: $(3 + 4 + 5) / 3 = 12 / 3 = 4$.
* Output: 4

------------------------------
Approach:-

   1. Strict I/O Adherence: Follow the exact input/output format. Never include extra "Enter value" prompts; the automated judge only wants the final result.
   2. Data Type Precision: Use the specific types requested (e.g., performing integer division for an int average) to ensure your output matches the expected "Sample Output" character-for-character.
   3. Edge Case Safety: Always include logic to handle "zero" or "null" scenarios—such as checking if count > 0 before dividing—to prevent the program from crashing during hidden test cases.
   4. Minimalist Logic: Write clean, readable code (like using your Enhanced For-Loop) that focuses strictly on the problem's requirements without adding unnecessary features.

