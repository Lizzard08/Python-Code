import time
import sorts
import random
import matplotlib.pyplot as plt


# generate a list from 1 to n to be sorted
def generateUnsortedList(n, ordering_type = 'random'):

    # return a perfectly sorted list (i.e. nothing to be done)
    if ordering_type == 'already_sorted':
        return list(range(1, n+1, 1))

    # return a nearly sorted list by swap ~10% of elements in sorted list
    elif ordering_type == 'nearly_sorted':
        alist = list(range(1, n+1, 1))
        random.seed(n)
        for i in range(n):
            if random.uniform(0, 1) < 0.10:
                j = random.choice(range(n))
                sorts.swap_two_elements(alist, i, j)
        return alist

    # return a perfectly unsorted list (i.e. sorted backwards)
    elif ordering_type == 'sorted_in_reverse':
        return list(range(n, 0, -1))

    # otherwise (and by default), return a randomly generated list
    else:
        alist = list(range(1, n+1, 1))
        random.seed(n)
        random.shuffle(alist)
        return alist

# carry out a particular sorting algorithm on a particular type of unsorted list
def timeSortingAlgorithm(n, ordering_type, sorting_algorithm):
    alist = generateUnsortedList(n, ordering_type)
    start = time.time()
    sorting_algorithm(alist)
    end = time.time()
    return end - start

# storage for performance benchmark results and intermediate results
lap_bubble = 0
lap_select = 0
lap_insert = 0
t_bubble = list()
t_select = list()
t_insert = list()

# benchmarking parameters
values_of_n = [2**x for x in range(5, 11)]
#ordering_type = 'random'
#ordering_type = 'sorted_in_reverse'
#ordering_type = 'nearly_sorted'
ordering_type = 'already_sorted'

# run benchmarks for each size n and k times for less-noisy results
for n in values_of_n:
    if n < 256:
        print(generateUnsortedList(n, ordering_type))
    for k in range(10):
        lap_bubble += timeSortingAlgorithm(n+k, ordering_type, sorts.bubbleSort)
        lap_select += timeSortingAlgorithm(n+k, ordering_type, sorts.selectionSort)
        lap_insert += timeSortingAlgorithm(n+k, ordering_type, sorts.insertionSort)
    t_bubble.append(lap_bubble/10.0)
    t_select.append(lap_select/10.0)
    t_insert.append(lap_insert/10.0)


# plot results of benchmarking
plt.plot(values_of_n, t_bubble, color='red')
plt.plot(values_of_n, t_select, color='blue')
plt.plot(values_of_n, t_insert, color='green')
plt.legend(('Bubble', 'Selection', 'Insertion'), loc='upper left')
plt.title('Comparing Sorting Algorithms (ordering: ' + ordering_type + ')')
#plt.ylim((0, 0.0001))

plt.show()

