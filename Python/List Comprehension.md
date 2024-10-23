List comprehension in Python is a concise way to create lists. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list, range, or another collection) in just a single line of code.

### Basic syntax:

```python
[expression for item in iterable if condition]
```

- **expression**: The operation or transformation applied to each item in the iterable.
- **item**: The element from the iterable (e.g., a list, range, or other collection).
- **iterable**: The collection being iterated over.
- **if condition** _(optional)_: A condition to filter which items are included in the resulting list.

## Example:

```python
[x * 2 for x in range(5)]
```

- Result: `[0, 2, 4, 6, 8]`
- Here, each number in `range(5)` is doubled.