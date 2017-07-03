human_characteristics = {
    "Black": "CCAGCAATCGC",
    "Brown_hair": "GCCAGTGCCG",
    "Blonde": "TTAGCTATCGC",
    "Square": "GCCACGG",
    "Round": "ACCACAA",
    "Oval": "AGGCCTCA",
    "Blue": "TTGTGGTGGC",
    "Green": "GGGAGGTGGC",
    "Brown": "AAGTAGTGAC",
    "Female": "TGAAGGACCTTC",
    "Male": "TGCAGGAACTTC",
    "White": "AAAACCTCA",
    "Black_race": "CGACTACAG",
    "Asian": "CGCGGGCCG"
}

suspect1_Eva = {
    "Gender": "Female",
    "Race": "White",
    "Hair color": "Blonde",
    "Eye color": "Blue",
    "Face shape": "Oval"}

suspect2_Larisa = {
    "Gender": "Female",
    "Race": "White",
    "Hair color": "Brown_hair",
    "Eye color": "Brown",
    "Face shape": "Oval"}

suspect3_Matej = {
    "Gender": "Male",
    "Race": "White",
    "Hair color": "Black",
    "Eye color": "Blue",
    "Face shape": "Oval"}

suspect4_Miha = {
    "Gender": "Male",
    "Race": "White",
    "Hair color": "Brown_hair",
    "Eye color": "Green",
    "Face shape": "Square"}


suspect1_Eva.values()
print suspect1_Eva.values()
eva_match = {item: human_characteristics[item] for item in suspect1_Eva.values() if item in human_characteristics}
print eva_match
suspect2_Larisa.values()
larisa_match = {item: human_characteristics[item] for item in suspect2_Larisa.values() if item in human_characteristics}
larisa_match.values()
suspect3_Matej.values()
matej_match = {item: human_characteristics[item] for item in suspect3_Matej.values() if item in human_characteristics}
matej_match.values()
suspect4_Miha.values()
miha_match = {item: human_characteristics[item] for item in suspect4_Miha.values() if item in human_characteristics}
miha_match.values()

x = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

if all(word in x for word in eva_match.values()):
    print True
else:
    print False

if all(word in x for word in larisa_match.values()):
    print True
else:
    print False

if all(word in x for word in matej_match.values()):
    print True
else:
    print False

if all(word in x for word in miha_match.values()):
    print True
else:
    print False