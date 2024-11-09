> **Programming Principles Assignment**  
> *Kennesaw State University - MS Cybersecurity Program*

This was one of several assignments needed to pass the **Programming Principles** module. 

---

### 🎓 Assignment Description: Grading Program

The program should calculate the average of 8 test scores and display the corresponding letter grade.

#### Functions to Implement

1. **`calc_average`**  
   Prompts for 8 test scores and returns the average.

2. **`determine_grade`**  
   Accepts the average score and returns the corresponding letter grade based on this scale:

   | Score Range | Grade |
   |-------------|-------|
   | 90-100      | A     |
   | 80-89       | B     |
   | 70-79       | C     |
   | 60-69       | D     |
   | Below 60    | F     |

---

### 🐱 Code Explanation Summary

- **`Cat` Class**  
  Defines a virtual cat with a `name`, `energy` level, and `stomach capacity`.
  - `play`: Decreases energy with each action. Prints a message when the cat is tired.
  - `eat`: Decreases stomach capacity with each feeding. Prints a message when the cat is full.

- **`main` Function**  
  - Prompts the user to name the cat, then lets the user interact by choosing to **play** or **feed**.
  - The loop continues until the user exits by entering **'n'**.

- **`__name__` Check**  
  Ensures `main` runs only if the script is executed directly, not when imported.
