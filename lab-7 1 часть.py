import numpy as np
import random
import time

list_1 = [random.randint(1, 100) for i in range(1000000)]
list_2 = [random.randint(1, 100) for i in range(1000000)]

massiv_1 = np.array(list_1)
massiv_2 = np.array(list_2)

start_time = time.perf_counter()
result_list = [list_1[i] * list_2[i] for i in range(len(list_1))]
end_time = time.perf_counter()
list_time = end_time - start_time
print(f"Время перемножения списков: {list_time}")

start_time = time.perf_counter()
result_array = np.multiply(massiv_1, massiv_2)
end_time = time.perf_counter()
massiv_time = end_time - start_time
print(f"Время перемножения массивов: {massiv_time}")

