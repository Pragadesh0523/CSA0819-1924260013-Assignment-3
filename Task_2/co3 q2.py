import copy
import sys
import timeit
rows, cols = 3, 4
bad = [[0] * cols] * rows
good = [[0 for j in range(cols)] for i in range(rows)]
bad[0][1] = 7
good[0][1] = 7
print("bad:", bad)
print("good:", good)
print("bad[0] is bad[1]:", bad[0] is bad[1])
print("good[0] is good[1]:", good[0] is good[1])
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}
print(stops[(13.0418, 80.2341)])
original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)
original[0][0] = 99
print("Original:", original)
print("Shallow:", shallow)
print("Deep:", deep)
values = list(range(1000000))
tuple_values = tuple(values)
print("List memory:", sys.getsizeof(values))
print("Tuple memory:", sys.getsizeof(tuple_values))
list_time = timeit.timeit(
    "list(range(10000))",
    number=1000
)
tuple_time = timeit.timeit(
    "tuple(range(10000))",
    number=1000
)
print("List creation time:", list_time)
print("Tuple creation time:", tuple_time)
list_index = timeit.timeit(
    "values[5000]",
    globals={"values": values},
    number=1000000
)
tuple_index = timeit.timeit(
    "values[5000]",
    globals={"values": tuple_values},
    number=1000000
)
print("List indexing time:", list_index)
print("Tuple indexing time:", tuple_index)
nested = ([1, 2, 3], [4, 5, 6])
nested[0][1] = 100
print("Tuple containing lists:", nested)
