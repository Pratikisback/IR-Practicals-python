import difflib as dl
file = open("D:\\InformationRetrieval_practicals\\file1.txt","r")
a = file.read()
file = open("D:\\InformationRetrieval_practicals\\file2.txt","r")
b = file.read()

sim = dl.get_close_matches
s = 0
wa = a.split()
wb = b.split()

for i in wa:
    if sim(i,wb):
        s += 1

n = float(s)/float(len(wa))
print('%d%% similarity' % int(n*100,))