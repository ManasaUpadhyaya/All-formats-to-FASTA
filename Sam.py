sam_file = open("sample.sam")
fasta_file = open("fasta.txt", "w")
for line in sam_file:
    if line.startswith("@") == 0:
        dict_sam = {}
        dict_sam["descriptor"] = ">" + line.split()[0].strip()
        dict_sam["sequence"] = line.split()[9].strip()
        for key, value in dict_sam.items():
            fasta_file.write(key)
            fasta_file.write(value)
            fasta_file.write("\n")




