import sys;

def answer(xs):
	if len(xs) == 1:
		return xs[0];
	arr = [];
	a = [];
	fa = [];
	for i in xs:
		if i != 0:
			arr.append(i);
	negative = 0;
	for i in arr:
		if i < 0:
			negative += 1;
	if negative % 2 != 0:
		hitnegative = 0;
		h = float("inf")*-1;
		for i in arr:
			if i > h and i < 0:
				h = i;
		for i in arr:
			if i != h:
				fa.append(i);
			else:
				if hitnegative == 1:
					fa.append(i);
				hitnegative = 1;
	else:
		for i in arr:
			fa.append(i); 
	num = 0;
	numset = 0;
	for i in fa:
		if numset == 0:
			num = i;
			numset = 1;
		else:
			num = num * i;
	return num;

def main(argc, argv):
	if (argc > 1):
		del argv[0];
		up = 0;
		for i in argv:
			try:
				argv[up] = int(i);
			except:
				print("Non-integer encountered.");
				return 0;
			up += 1;
		ans = answer(argv);
		print(ans);
	else:
		print("No arguments were passed.");

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
