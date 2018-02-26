S="kqep"
T="pekeq"
# S="hucw"
# T="utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"
ls = list(S)
dict = {}
for i in T:
    if i in ls:
        if i not in dict:
            index = ls.index(i)
            ls = ls[:index]+T.count(i)*[i]+ls[index+1:]
            dict[i] = i
    else:
        ls.append(i)
print  "".join(ls)
