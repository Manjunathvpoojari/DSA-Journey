# 📅 Day 4 - Patterns (Detailed)

## 🧠 Concept
Patterns use nested loops

## 🔑 Key Idea
- Outer loop = rows
- Inner loop = columns

## ⭐ Pattern 1
*
**
***
****

for(int i = 1; i <= 4; i++) {     // rows
    for(int j = 1; j <= i; j++) { // columns
        System.out.print("*");
    }
    System.out.println();
}

## 💡 Logic
stars = row number

## ⭐ Pattern 2
****
****
****
****

## 💡 Logic
fixed number of columns

for(int i = 1; i <= 4; i++) {
    for(int j = 1; j <= 4; j++) {
        System.out.print("*");
    }
    System.out.println();
}

## 🔢 Pattern 3
1
12
123
1234

for(int i = 1; i <= 4; i++) {
    for(int j = 1; j <= i; j++) {
        System.out.print(j);
    }
    System.out.println();
}

## 🎯 Takeaways
- Use nested loops
- Observe row-column relation
- Practice improves logic