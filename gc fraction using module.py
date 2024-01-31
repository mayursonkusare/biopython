from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
file = input("enter the file name:-")
b = str(input("which type of the file format it is:-"))
data = open(file,"r")
for Seq_record in SeqIO.parse(data,b):
    a = str(Seq_record.seq)
print("The sequence is :-",a)
print("The gc content of the sequence is :-",gc_fraction(a)*100)
