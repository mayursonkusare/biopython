from Bio import SeqIO
from Bio.Seq import Seq
file = input("enter the file name:-")
data = open (file,"r")
for Seq_record in SeqIO.parse(data,"fasta"):
    a = str(Seq_record.seq)
print("The sequence is :-\n",a)
b = int(input("enter the starting postion from you want to slice the string:-"))
c = int(input("enter the ending positon from you want to slice the string:-"))
d = a[b:c]
print("The slice sequence is :-",d)
