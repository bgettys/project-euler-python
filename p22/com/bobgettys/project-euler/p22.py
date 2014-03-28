'''
Created on Mar 27, 2014

@author: rgettys
'''

'''

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

'''

#it's CSV -_-

f = open('../../../resources/names.txt', 'r')

state = 0
names = []
c = f.read(1)
name = ''
while c != '':
    o = ord(c)
    if (o >= 65 and o <= 90) or (o >= 97 and o <= 122):
        name += c
    elif name != '':
        names.append(name)
        name = ''
    c = f.read(1)

i = 1
sum = 0
for name in sorted(names):
    for c in name:
        o = ord(c)
        if (o > 90):
            o -= 96
        else:
            o -= 64
        sum += o*i
    i += 1
print(sum)

if __name__ == '__main__':
    pass