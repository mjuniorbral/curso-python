# ESCRITO PELO CHATGPT NO DIA 14/08/2024 NO CHAT DE NOME PYTHON:

Em Python, há muitas funções e métodos embutidos que são do tipo `builtin_function_or_method`. Aqui está uma lista das funções embutidas disponíveis na maioria das versões padrão do Python 3.9 (a versão mais recente disponível até minha última atualização). 

Essas funções são implementadas em C e fazem parte da biblioteca padrão do Python:

### Funções embutidas (`builtin_function_or_method`):

1. `abs()`
2. `all()`
3. `any()`
4. `ascii()`
5. `bin()`
6. `bool()`
7. `breakpoint()`
8. `bytearray()`
9. `bytes()`
10. `callable()`
11. `chr()`
12. `classmethod()`
13. `compile()`
14. `complex()`
15. `delattr()`
16. `dict()`
17. `dir()`
18. `divmod()`
19. `enumerate()`
20. `eval()`
21. `exec()`
22. `filter()`
23. `float()`
24. `format()`
25. `frozenset()`
26. `getattr()`
27. `globals()`
28. `hasattr()`
29. `hash()`
30. `help()`
31. `hex()`
32. `id()`
33. `input()`
34. `int()`
35. `isinstance()`
36. `issubclass()`
37. `iter()`
38. `len()`
39. `list()`
40. `locals()`
41. `map()`
42. `max()`
43. `memoryview()`
44. `min()`
45. `next()`
46. `object()`
47. `oct()`
48. `open()`
49. `ord()`
50. `pow()`
51. `print()`
52. `property()`
53. `range()`
54. `repr()`
55. `reversed()`
56. `round()`
57. `set()`
58. `setattr()`
59. `slice()`
60. `sorted()`
61. `staticmethod()`
62. `str()`
63. `sum()`
64. `super()`
65. `tuple()`
66. `type()`
67. `vars()`
68. `zip()`
69. `__import__()`

### Métodos embutidos (`builtin_function_or_method`):
Esses métodos são integrados às classes padrão do Python. Por exemplo, métodos associados a tipos padrão como `str`, `list`, `dict`, etc.

- `dict.items()`
- `dict.keys()`
- `dict.values()`
- `str.lower()`
- `str.upper()`
- `str.join()`
- `list.append()`
- `list.extend()`
- `list.pop()`
- `set.add()`
- `set.remove()`

### Como listar dinamicamente
Você pode listar todas as funções embutidas no seu ambiente Python dinamicamente com o seguinte código:

```python
import builtins

# Lista todas as funções embutidas no Python
builtin_functions = [name for name, obj in vars(builtins).items() if isinstance(obj, type(len))]
print(builtin_functions)
```

### Considerações
Essa lista é baseada na versão padrão do Python 3.x, e ela pode variar dependendo das modificações feitas no ambiente de Python ou de atualizações posteriores.

Se precisar de mais detalhes ou ajuda com alguma dessas funções, estarei aqui para ajudar!
