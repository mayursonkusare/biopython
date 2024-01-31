"""from Bio import SeqIO
from Bio.Seq import Seq
a = int(input("how many time you want to run the code:-"))
d = [sequence]
seq =""
for i in range(a):
    b = input("enter the file name:-")
    data = open(file,"r")
    sequence = Seq(data)
    print("The sequence:-",sequence)
    for seq in d:
        cont += seq
        print("The concatinated sequence :-",seq)"""
from Bio import SeqIO
from Bio.Seq import Seq

a = int(input("How many times do you want to run the code: "))
d = []  # Initialize an empty list to store sequences

for i in range(a):
    b = input("Enter the file name: ")
    with open(b, "r") as data:  # Use `with` for proper file handling
        sequence = SeqIO.read(data, "fasta")  # Read sequence using SeqIO
        d.append(sequence.seq)  # Append the sequence to the list
        print("The sequence:", sequence.seq)  # Print the current sequence

cont = ""
for seq in d:
    cont += seq
    print("The concatenated sequence:", cont)  # Print the concatenated sequence
