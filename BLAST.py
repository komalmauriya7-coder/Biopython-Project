import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from Bio.Blast import NCBIWWW
from Bio import SeqIO

record = SeqIO.read("sequence.fasta", "fasta")

result_handle = NCBIWWW.qblast(
    program= "blastp",
    database= "nr",
    sequence= record.seq
)

with open ("blast_result.xml", "w") as b:
    b.write(result_handle.read())

print ("Blast Performed Suessfully")