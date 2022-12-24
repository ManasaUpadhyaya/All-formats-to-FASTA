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
print(list_dict_fastq)




