from Bio.Seq import Seq
sequence = Seq("ATATTTTTAAAGGGGCGGCGATAT")
for index,letter in enumerate(sequence):
    print("%i %s"%(index , letter))
