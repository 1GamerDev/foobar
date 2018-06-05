import sys;
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
revalphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
revalphabet.reverse();
def convert(c):
    return {
        '1' : 'A',
        '2' : 'B',
        '3' : 'C',
        '4' : 'D',
        '5' : 'E',
        '6' : 'F',
        '7' : 'G',
        '8' : 'H',
        '9' : 'I',
        '10' : 'J',
        '11' : 'K',
        '12' : 'L',
        '13' : 'M',
        '14' : 'N',
        '15' : 'O',
        '16' : 'P',
        '17' : 'Q',
        '18' : 'R',
        '19' : 'S',
        '20' : 'T',
        '21' : 'U',
        '22' : 'V',
        '23' : 'W',
        '24': 'X',
        '25': 'Y',
        '26': 'Z'
    }[c]
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
