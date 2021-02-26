# we have raw data stored in sequences variable

sequences = "tatgctttcc#tataggtctg#ctattcaatg"
dna_list = sequences.split('#') #we split sequences to create a list using # delimeter
print(dna_list)

for dna in dna_list:
  rna = dna.replace("t", "u")     #we convert DNA to RNA by replacing the letter t for Thymine with u for Uracil
  print(f"DNA: {dna} -> RNA: {rna}")
