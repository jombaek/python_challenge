def trans(line, res=""):
    for c in line:
        if c.isalpha():
            res += chr((ord(c) - ord('a') + 2) % 26 + ord('a'))
        else:
            res += c
    return res

line = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

table = str.maketrans(
    "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
)

res = line.translate(table)
print(res)

print("map".translate(table))