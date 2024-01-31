from Bio import SeqIO
file = input("enter the file name:-")
data = open(file,"r")
for sequ in SeqIO.parse(data,"genbank"):
    a = sequ.id
    b = (str(sequ.seq))
    c = (len(sequ))
print("The ID of the Genbank file is :-",a)
print("The sequence of the Genbank file is :-",b)
print("The length of the sequence is:-",c)
A = b.count("A")
T = b.count("T")
G = b.count("G")
C = b.count("C")
GC = (G+C)/c*100
print("The count of the A in the genbank sequence is :-",A)
print("The count of the T in the genbank sequence is :-",T)
print("The count of the G in the genbank sequence is :-",G)
print("The count of the C in the genbank sequence is :-",C)
print("The GC contnet of the sequence is :-",GC)
