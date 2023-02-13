# Примеры для алгоритмической сложности

## ... создание переменной, деление, умножение.."

```python
a = 10
b = 2
c = a / b
d = a * b
```

## O(1)

### Получение элемента из списка по индексу

```python
numbers = [1, 2, 3]
num = numbers[1]
```

### Получение значения из словаря по ключу

```python
data = {
    "foo": "bar",
    "spam": "eggs",
}
spam_value = data["spam"]
```

### Получение длины коллекции

```python
codes = {"iddqd", "hesoyam", "rosebud"}
total_len = len(codes)
```


## O(n)

### Сложение всех элементов
```python
def sum_all(numbers: list[int]) -> int:
    result = 0
    for num in numbers:
        result += num
    return result
```

6:20 
```python
def sum_all(numbers):
    result = 0
    for num in numbers:
        result += num
    return result
```

### Поиск элемента в коллекции (перебором)

```python
def has_value(a: list[int], target: int):
    # проверка: есть ли элемент в списке
    for num in a:
        if num == target:
            return True
    return False
```

6:20 
```python
def has_value(a, target):
    # есть ли элемент в списке
    for num in a:
        if num == target:
            return True
    return False
```


## O(log n)

Разделяй и властвуй (Divide and conquer) - картинка

### Бинарный поиск
тут картинка бинарного дерева. И подписать:
- бинарный поиск: "разделяй и властвуй"
- поиск минимального/максимального числа в бинарном дереве

O(1) + O(n^2) = O(n^2) 

## O(n log n)
подписать:
- сортировка слиянием (merge sort)
- "быстрая сортировка" (quick sort)
- сортировка кучей/множеством (heap sort)

## O(n^2)

### Проход по всем элементам в цикле и ещё раз для каждой итерации 

```python
def show_pairs(numbers):
    for number_i in numbers:
        for number_j in numbers:
            print(number_i, number_j)
```

### Сортировка пузырьком

```python
def bubble_sort(numbers):
  for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
      if numbers[j] > numbers[j + 1]:
        temp = numbers[j]
        numbers[j] = numbers[j+1]
        numbers[j+1] = temp
```

## O(n^3)

### Проход по всем элементам в цикле трижды 

```python
def combine_3(values: list):
    for i in values:
        for j in values:
            for k in values:
                print(i, j, k)
```

