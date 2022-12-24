import re
fastq = open("example.fastq")
list_dict_fastq = []
for line in fastq:
    if line.startswith("@") :
        dict_fastq = {}
        dict_fastq["Descriptor"] = line.split("@")[1].strip()
    if re.search(pattern="[?]", string=line) is None and re.search(pattern="[+/]", string=line) is None:
        dict_fastq["Sequence"] = line.strip()
        list_dict_fastq.append(dict_fastq)

fasta_fastq = open("fasta_fastq.txt", "w")
for list_items in list_dict_fastq:
    fasta_desc = ""
    fasta_seq = ""
    for key, value in list_items.items():
        if key != 'Sequence':
            fasta_desc += ">" + list_items[key]

        else:
            fasta_seq += list_items[key].upper()
            fasta_fastq.write(fasta_desc) + fasta_fastq.write("\n") + fasta_fastq.write(fasta_seq) + fasta_fastq.write("\n")




