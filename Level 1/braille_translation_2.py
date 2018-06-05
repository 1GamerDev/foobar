import sys;
def convert(c):
    return {
        'A' : "100000",
        'B' : "110000",
        'C' : "100100",
        'D' : "100110",
        'E' : "100010",
        'F' : "110100",
        'G' : "110110",
        'H' : "110010",
        'I' : "010100",
        'J' : "010110",
        'K' : "101000",
        'L' : "111000",
        'M' : "101100",
        'N' : "101110",
        'O' : "101010",
        'P' : "111100",
        'Q' : "111110",
        'R' : "111010",
        'S' : "011100",
        'T' : "011110",
        'U' : "101001",
        'V' : "111001",
        'W' : "010111",
        'X' : "101101",
        'Y' : "101111",
        'Z' : "101011",
        ' ' : "000000"
    }[c]
def answer(plaintext):
    str = "";
    ci = 0;
    for i in plaintext:
        ci+=1;
        if ci > 49:
            return "";
        tmps = "";
        try:
            tmps = convert(i.upper());
        except KeyError:
            print("Non-alphabetic character encountered (character {})".format(ci));
            pass;
        if i.isupper():
            str += "000001";
        str += tmps;
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
