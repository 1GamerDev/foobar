import sys;
import copy;

def answer(n):
	up = 0;
	up0 = 0;
	up1 = 0;
	if n == 0:
		return 1;
	elif n == 1:
		return 0;
	n0 = copy.copy(n);
	n1 = copy.copy(n);
	while n0 != 1:
		if n0 % 2 != 0:
			if (n0 + 1) % 2 == 0:
				n0 += 1;
				up0 += 1;
			else:
				n0 -= 1;
				up0 += 1;
		n0 /= 2;
		up0 += 1;
	while n1 != 1:
		if n1 % 2 != 0:
			if (n1 - 1) % 2 == 0:
				n1 -= 1;
				up1 += 1;
			else:
				n1 += 1;
				up1 += 1;
		n1 /= 2;
		up1 += 1;
	if up0 > up1:
		up = up1;
	else:
		up = up0;
	return up;

def main(argc, argv):
	if argc == 2:
		i = 0;
		try:
			i = int(argv[1]);
		except:
			print("Non-integer encountered.");
			return 0;
		if i < 0:
			print("You may only pass a positive integer.");
			return 0;
		ans = answer(i);
		print(ans);
	else:
		print("No argument was passed.");

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
