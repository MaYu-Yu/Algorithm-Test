def hanoi(n, a, b, c):
	if n == 1:
		print(a, '-->', c, end = ' ')
	else:
		hanoi(n - 1, a, c, b)
		hanoi(1    , a, b, c)
		hanoi(n - 1, b, a, c)
def hanoi_tail_recursion(n, a, b, c):
	while( n > 0 ):
		hanoi_tail_recursion(n - 1, a, c, b)
		print(a, '-->', c, end = ' ')
		n-=1
		a, b = b, a
if __name__ == '__main__':
	hanoi(5, 'A', 'B', 'C')
	print()
	hanoi_tail_recursion(5, 'A', 'B', 'C')