from Bio import SeqIO
file = input("enter the file name:-") # asking user to enter the file name
data = open(file,"r")
for seq_record in SeqIO.parse(data,"fasta"): # parsing the file using SeqIO.parse module
    a = seq_record.id # getting the sequence id
    b = (str(seq_record.seq)) # getting the sequence in fasta file
    c = (len(seq_record)) # getting the length of the sequence
print("The id of the fasta sequence :- ",a)
print("The sequence in the fasta file :-",b)
print("The length of the sequence in fasta file :-",c,"Aminoacids")  

