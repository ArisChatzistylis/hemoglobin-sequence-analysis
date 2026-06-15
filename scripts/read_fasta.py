from Bio import SeqIO


for record in SeqIO.parse("data/raw_sequences.fasta","fasta"):

    print("-" * 40)
    print(f"ID: {record.name}")
    print(f"Length: {len(record.seq)} amino acids")
    print(f"First 10 amino acids: {record.seq[:10]}")

    print(f"Number of alanines: {record.seq.count('A')}")
    print(f"Number of glycines: {record.seq.count('G')}")
    print(f"Number of valines: {record.seq.count('V')}")
    