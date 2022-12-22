import re
genebank_file = open("KU325498.gb.txt")
dict = {}
x = print(dict)
sequence = ''
value_seq = ''
a = 0
for line in genebank_file:
    line.strip()
    if a == 1:
        sequence+= line
    if (re.search(pattern="DEFINITION", string = line)) is not None:
        dict["Name"] = line.split("DEFINITION")[1].split(",")[0].strip()
    if (re.search(pattern="ACCESSION", string=line)) is not None:
        dict["Accession"] = line.split("ACCESSION")[1].strip()
    if (re.search(pattern="LOCUS", string=line)) is not None:
        dict["Length"] = line.split()[2].strip('\n')
    if (re.search(pattern="ORIGIN", string=line)) is not None:
        a += 1

    if (re.search(pattern="//", string=line)) is not None:
        #print(sequence)
        for i in sequence:
            if re.search(pattern="[atgc]", string = i) is not None:
                value_seq += i
        dict["Seq"] = value_seq






