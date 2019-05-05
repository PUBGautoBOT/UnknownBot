fh = open('kk.txt','r')
op = open('opkk.txt','w')

l = fh.readlines()



c = 1

##for i in l:
##    str = ''
##    for j in i:
##        print(j)
##        if '\t' in j:
##            c += 1
##        if c%2 == 0:
##            print('\\t')
##            j = '\n'
##        str += j
##        #print(str)
##    op.write(str)

for i in l:
    i = i.replace('\n','')
    t = i.split('\t')
    s = ''
    for w in range(0,len(t)):
        #print(t[w] + " - " + str(w))
        s += ' '+t[w]
        if w%2 != 0:
            op.write(s.strip()+'\n')
            s = ''
            #print('\n')




















op.close()
