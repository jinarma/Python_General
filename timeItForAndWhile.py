import timeit
import numpy

def while_loop(n=100_000):
	i, s = 0, 0
	while i < n:
		s += 1
		i += 1
	return s

def for_loop(n=100_000):
	s = 0
	for i in range(n):
		s += 1
	return s

def numpy_loop(n=100_000):
	return numpy.sum(numpy.arange(n))

if __name__ == '__main__':
	print('while_loop\t\t', timeit.timeit(while_loop, number=1))
	print('for_loop\t\t', timeit.timeit(for_loop, number=1))
	print('numpy_loop\t\t', timeit.timeit(numpy_loop, number=1))