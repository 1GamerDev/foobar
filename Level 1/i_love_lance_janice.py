import sys;
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
revalphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
revalphabet.reverse();
def answer(plaintext):
    str = "";
    for i in plaintext:
        tmpstr = "";
        passt = 0;
        if i.isupper():
            str += i;
            passt = 1;
        if i.upper() in alphabet and passt == 0:
            i = i.upper();
            if alphabet.index(i) < 13:
                tmpstr = revalphabet[alphabet.index(i)];
            else:
                tmpstr = alphabet[revalphabet.index(i)];
            str += tmpstr.lower();
        elif passt == 0:
            str += i;
    if str == "":
        return "";
    return str;
def main(argc, argv):
    if argc != 2:
        print("Failed");
        return;
    ans = answer(argv[1]);
    if ans == "":
        print("Failed");
    else:
        print(ans);
    return;
if __name__== "__main__":
  main(len(sys.argv), sys.argv)
