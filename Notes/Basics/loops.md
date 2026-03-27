📅  Day 3 — Loops & Conditional Statements
Java for Beginners  ·  Complete Notes  ·  DSA Foundation

🎯 What You'll Learn Today:  Conditions (if/else), for loops, while loops, combining both — the backbone of every DSA problem.

🧠  Section 1 — Conditional Statements

1.1  What is a Condition?
A condition lets your program make a decision. It checks whether something is TRUE or FALSE, and then runs different blocks of code based on that result.

☔ Real-Life Example:  If it rains → take umbrella.   Else → leave it at home.

1.2  The if-else Statement
Syntax structure — the building block of all decisions:

  if ( condition ) {
      // runs when condition is TRUE
  } else {
      // runs when condition is FALSE
  }

📌  Worked Example — Age Check
  int age = 18;

  if (age >= 18) {
      System.out.println("You are an adult");
  } else {
      System.out.println("You are a minor");
  }

  // Output: You are an adult

1.3  Three Types of Conditions

Type 1️⃣ — Simple if (one path)
Use when you only need to do something when a condition is true. If it's false, nothing happens.

  if (x > 10) {
      System.out.println("Greater than 10");
  }

Type 2️⃣ — if-else (two paths)
Use when there are exactly two possibilities — one for true, one for false.

  if (x % 2 == 0) {
      System.out.println("Even");
  } else {
      System.out.println("Odd");
  }

💡 Key Operator:  x % 2 gives the remainder when x is divided by 2.  If remainder == 0, x is even.

Type 3️⃣ — if-else if-else (multiple paths)
Use when there are 3 or more possibilities. Conditions are checked top to bottom — the first true one runs.

  if (marks >= 90) {
      System.out.println("Grade A");
  } else if (marks >= 70) {
      System.out.println("Grade B");
  } else if (marks >= 50) {
      System.out.println("Grade C");
  } else {
      System.out.println("Grade D — Study harder!");
  }

🔢  Section 2 — Operators Reference

2.1  Comparison Operators
These are used inside conditions to compare two values:

Operator	Meaning	Example	Result
==	Equal to	5 == 5	true
!=	Not equal to	5 != 3	true
>	Greater than	7 > 4	true
<	Less than	2 < 9	true
>=	Greater than or equal	5 >= 5	true
<=	Less than or equal	3 <= 3	true

2.2  Logical Operators
Combine multiple conditions together:

Operator	Meaning	Example	Result
&&	AND — both must be true	x > 0 && x < 10	true if x is 1–9
||	OR — at least one true	x < 0 || x > 100	true if x is out of range
!	NOT — flips true/false	!(x == 0)	true if x is NOT zero

⚠️ Critical Mistake:  Using = (assignment) instead of == (comparison) inside an if condition — this is the #1 beginner bug!

🔁  Section 3 — Loops

3.1  What is a Loop?
A loop repeats a block of code multiple times without you having to write it again and again. It's one of the most powerful tools in programming.

📢 Real-Life Example:  A teacher calling attendance calls each student's name one by one — that's a loop running for every student.

3.2  The for Loop
Use a for loop when you know exactly how many times to repeat something.

  //    [1] init    [2] condition   [3] update
  for ( int i = 0;    i < 5;          i++ ) {
      System.out.println(i);
  }

  // Output:  0  1  2  3  4

🧠  How Each Part Works:

Part	Code	What It Does
1 — Initialise	int i = 0	Creates the counter variable and sets it to 0
2 — Condition	i < 5	Checks if loop should continue (runs while true)
3 — Update	i++	Increases counter by 1 after each iteration

🔄 Execution Flow:  i=0 → print 0 → i++ → i=1 → print 1 → … → i=4 → print 4 → i=5 → condition false → STOP

3.3  The while Loop
Use a while loop when you don't know in advance how many times to repeat — it keeps going as long as the condition is true.

  int i = 0;

  while (i < 5) {
      System.out.println(i);
      i++;          // NEVER forget this! (causes infinite loop)
  }

  // Output:  0  1  2  3  4

3.4  for vs while — When to Use Which?

Scenario	Use
Number of repetitions is fixed (e.g., loop 10 times)	for loop
Repetitions depend on a changing condition	while loop
Reading user input until they type 'quit'	while loop
Printing 1 to 100	for loop

⚡  Section 4 — Combining Loops + Conditions

🏆 Why This Matters:  Almost every single DSA problem uses loops + conditions together. Master this and you have the core of programming logic.

4.1  Example 1 — Print Even Numbers (1 to 10)
  for (int i = 1; i <= 10; i++) {
      if (i % 2 == 0) {
          System.out.println(i);
      }
  }

  // Output:  2  4  6  8  10

Step-by-step logic:
•	Loop runs for i = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
•	At each step, condition checks: is i divisible by 2 (remainder = 0)?
•	If YES → print it.  If NO → skip and continue.

4.2  Example 2 — Multiplication Table of 5
  int n = 5;

  for (int i = 1; i <= 10; i++) {
      System.out.println(n + " x " + i + " = " + (n * i));
  }

  // Output:  5 x 1 = 5
  //          5 x 2 = 10
  //          ...up to 5 x 10 = 50

4.3  Example 3 — Count Down from 10 to 1
  for (int i = 10; i >= 1; i--) {   // i-- decreases by 1
      System.out.println(i);
  }

  // Output:  10  9  8  7  6  5  4  3  2  1

❗  Section 5 — Common Mistakes & How to Fix Them

❌ Mistake	Example	✅ Fix
= instead of ==	if (x = 5)	if (x == 5)
Forgetting i++ in while	while (i<5) { print(i); }	Add i++ inside the loop body
Wrong boundary in for	for (i=1; i<10; i++) misses 10	Use i<=10 to include 10
Off-by-one error	Loop runs 1 extra or 1 less time	Trace manually: check first & last value

♾️ Infinite Loop Warning:  If you forget to update your counter (i++), the condition never becomes false and your program freezes — always double-check your update step!

🏋️  Section 6 — Practice Problems
Try solving these yourself before checking the solution — this is how real coding skill is built!

Problem 1 — Easy
Print numbers from 1 to 20 but print 'FizzBuzz' if the number is divisible by both 3 and 5, 'Fizz' if divisible by 3, and 'Buzz' if divisible by 5.

Problem 2 — Easy
Write a program that takes a number n and prints the sum of all numbers from 1 to n using a for loop.

Problem 3 — Medium
Print all prime numbers from 1 to 50. (Hint: A prime number is only divisible by 1 and itself — use a nested loop.)

🎯  Section 7 — Key Takeaways

Concept	What It Does	When to Use
if / else if / else	Makes decisions in code	Checking conditions, multiple outcomes
for loop	Repeats with a counter	Fixed number of repetitions
while loop	Repeats while condition is true	Unknown number of repetitions
Loop + Condition	The core of DSA logic	Almost every algorithm problem

🚀 Big Picture:  Every DSA problem — searching, sorting, patterns — is built on loops + conditions. 
