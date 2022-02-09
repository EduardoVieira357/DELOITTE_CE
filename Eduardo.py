import glob, re ; out1 = []; out2 = []; out3 = []; l = ""; cont = []
pat1 = re.compile('^ {8,11}[A-Z0-9_]{3,16} '); glue = 'XXX XXX XXX XXX\n'
pat2 = re.compile('.*APPEND*|.*INCLUDE.|.*___*.|.*ABAP*|.*SAP AG.')
pat3 = re.compile('.*Poèet polí*|.*Krátký popis.')
for file in glob.glob('./input/*.txt'):
    with open(file, 'r', encoding='ansi', errors='ignore') as fr:
            cont = fr.readlines()
            if len(cont) == 0: continue
            for i in range(len(cont)):
                if (re.match(pat1,cont[i])) and not (re.match(pat2,cont[i])):
                    out1.append(file.replace('.txt', '')+
                       cont[i].replace(" X ","   ").replace("\n",glue))
                if (re.match(pat2,cont[i])) or not (re.match(pat1,cont[i])):
                    out3.append(cont[i])
                if (re.match(pat3,cont[i])):
                    out2.append(file.replace('.txt', '')+'|'+cont[i])
            fr.close()
with open('./output_1','w', encoding='ansi', errors='ignore') as f1:
    for l in out1:
        f1.write(re.sub('X{3}.X{3}.X{3}.X{3}',"","|".join((l.split(None,4)))))
f1.close
with open('./output_2','w', encoding='ansi', errors='ignore') as f2:
    for l in out2:
        f2.write(l)
f2.close
with open('./output_3','w', encoding='ansi', errors='ignore') as f3:
    for l in out3:
        f3.write(l)
f3.close