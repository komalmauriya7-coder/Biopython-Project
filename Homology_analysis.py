from Bio.Blast import NCBIXML

with open("blast_result.xml") as b:
    blast_record = NCBIXML.read(b)

print(len(blast_record.alignments))

first_alignment = blast_record.alignments[0]
print(first_alignment.title)
print(first_alignment.length)

fifth_alignment = blast_record.alignments[4]
print(fifth_alignment.title)
print(fifth_alignment.length)

last_alignment = blast_record.alignments[-1]
print(last_alignment.title)
print(last_alignment.length)

first_hsp = first_alignment.hsps[0]
print(first_hsp.score)
print(first_hsp.expect)

print("Query sequences")
print(first_hsp.query)

print("Matched seq")
print(first_hsp.sbjct)

print("Alignment seq")
print(first_hsp.match)

print("Score:", first_hsp.score)
print("E-value:", first_hsp.expect)