import sys;

def answer(n):
	n = int(n);
	if n == 0:
		return 1;
	elif n == 1:
		return 0;
	elif n == 2:
		return 1;
	elif n == 3:
		return 2;
	elif n < 0:
		return n * -1 + 1; 
	up = 0;
	while n != 1:
		if n == 0:
			n += 1;
			up += 1;
		elif n == 3:
			n -= 1;
			up += 1;
		elif (n % 2) == 0:
			n /= 2;
			n = int(n);
			up += 1;
		elif ((n - 1) & (n - 2)) < ((n + 1) & n):
			n -= 1;
			up += 1;
		else:
			n += 1;
			up += 1;
	return up;

def main(argc, argv):
	if argc == 2:
		i = 0;
		try:
			i = int(argv[1]);
		except:
			print("Non-integer encountered.");
			return 0;
		ans = answer(argv[1]);
		print(ans);
	else:
		print("No argument was passed.");

if __name__ == "__main__":
	main(len(sys.argv), sys.argv)
