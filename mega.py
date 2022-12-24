import re
mega_file = open("KU325498.mega.txt")
dict_mega = {}
seq = ''
a = 0
for line in mega_file:
    if a == 1:
        line = line.strip()
        seq += line
    if re.search(pattern="TITLE", string = line) is not None:
        dict_mega["TITLE"] = line.split("TITLE")[1].split(":")[1].strip()
    if re.search(pattern="#", string=line) is not None and re.search(pattern="MEGA", string=line) is None:
        a = 1
        dict_mega["DESCRIPTOR"] = line.split("#")[1].strip()
dict_mega["Sequence"] = seq
fasta_desc = ">"
fasta_seq = ""
for key, value in dict_mega.items():
    if key != 'Sequence':
        fasta_desc+= dict_mega[key] + "|"

    else:
        fasta_seq += dict_mega[key].upper()

print(fasta_desc, fasta_seq)
fasta_genbank = open("fasta_mega.txt", "w")
fasta_genbank.write(fasta_desc) + fasta_genbank.write("\n") + fasta_genbank.write(fasta_seq)


