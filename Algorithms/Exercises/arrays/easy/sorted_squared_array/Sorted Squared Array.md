Não é otimizável criar um array vazio e inserir elementos. Gasta mais memória. O melhor caso é criar um array com as posições que você já sabe que teria:

```python
sorted_squared_array = [0] * len(array)
```

**Insert Operation:** Each insert(0, value) operation takes  O(n) , since inserting at the beginning shifts all elements right:

```python
sorted_squared_array.insert(0, num_left ** 2) # Não fazer
```
