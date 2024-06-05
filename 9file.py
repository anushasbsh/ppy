fname = "sample.txt"
WC = {}
with open(fname , 'r')as fh:
    for line in fh:
        wl = line.replace(',','').replace('\'','').replace('-','').replace('.','').lower().split()
        for w in wl:
            if w not in WC:
                WC[w] = 1
            else:
                WC[w] = WC[w]+1

for (w,o) in WC.items():
    print(w,o)