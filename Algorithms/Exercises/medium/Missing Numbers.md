You're given an unordered list of unique integers nums in the range [1, n], where n represents the length of nums + 2. This means that two numbers in this range are missing from the list.

Write a function that takes in this list and returns a new list with the two missing numbers, sorted numerically.
### Sample Input

```python
nums = [1, 4, 3]
```
### Sample Output

```python
[2, 5] # n is 5, meaning the completed list should be [1, 2, 3, 4, 5]
```

## Solução

### 2 for loops

- range of max -> get all the iterations
- number not in range of max -> missing

Time -> O(nˆ2)
Space -> O(1)

### 2 pointers and sort
[[Missing Numbers.excalidraw]]
- Sort
- Compare items of pointers

Time -> O(n log n)
Space -> O(n)

### Set
[[Set]]
- Convert the Input List to a Set

The conversion from a list to a set takes O(n) time, where nnn is the length of the input list.

- Generate the Complete Range of Numbers
- Check for Missing Numbers

Since checking membership in a set takes O(1) time, this step is efficient. Each lookup is constant time, and since there are n+2 numbers in the complete range, this entire check runs in O(n) time.

Time -> O(n)
Space -> O(n)

### **Comparison**
| **Algorithm**         | **Time Complexity**          | **Space Complexity** |
| --------------------- | ---------------------------- | -------------------- |
| **`missingNumbers1`** | O(n2)O(n^2)O(n2)             | O(1)O(1)O(1)         |
| **`missingNumbers`**  | O(nlog⁡n)O(n \log n)O(nlogn) | O(n)O(n)O(n)         |
| **`missingNumbers3`** | O(n)O(n)O(n)                 | O(n)O(n)O(n)         |

### **Which is better?**

1. **Time complexity**:
    
    - `missingNumbers3` is the best with O(n) time complexity.
    - `missingNumbers` is next with O(nlog⁡n).
    - `missingNumbers1` is the worst with O(nˆ2), making it inefficient for larger inputs.
2. **Space complexity**:
    
    - `missingNumbers1` has the best space complexity with O(1).
    - Both `missingNumbers` and `missingNumbers3` use O(n) space due to the creation of additional data structures (`complete_array` and `includedNums`).

### **Overall Best Algorithm**:

- **`missingNumbers3`** is the best in terms of both time and space tradeoffs. It has linear time complexity and moderate space usage.