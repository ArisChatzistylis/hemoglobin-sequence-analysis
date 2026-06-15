from Bio import SeqIO

# Make a list this time to compare sequences
records = list(SeqIO.parse("data/raw_sequences.fasta","fasta"))

human = records[0]
mouse = records[1]

print(human.id)
print(human.seq[:20])
print(mouse.id)
print(mouse.seq[:20])

# pairwise sequence comparison

matches = 0

for a, b in zip(human.seq, mouse.seq):
    if a == b:
        matches += 1

# Calculating percent sequence identity

identity = (matches / len(human.seq)) *100
print(f"Percent identity: {identity}%")
