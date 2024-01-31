from Bio.Seq import Seq
a = Seq("ATGCATGAA")
print(a)
print("The complementary of above sequence")
com = a.complement()
print(com)
rev_com = a.reverse_complement()
print(rev_com)
