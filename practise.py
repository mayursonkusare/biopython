from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction,seq3,seq1,molecular_weight,six_frame_translations
a = input("enter the file name:-")
file = open(a,'r')
print(file)
for a in SeqIO.parse(file,"genbank"):
  b = a.id
  c = (str(a.seq))
  d = len(c)
  e = (gc_fraction(c)*100)
  f= seq3(c)
  g = six_frame_translations(c)
print("The id of the sequence is :-",b)
print("The sequence in file is:-",c)
print("The length of the sequence is :-",d)
print("The gc percentage of the sequence is :-",e)
print(f)
print("%0.2f"%molecular_weight(c,"protein"))


