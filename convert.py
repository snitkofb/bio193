# Ben Snitkoff
# November 10, 2023
# Bio 193 -- Dr. Benjamin Wolfe -- Tufts University


# Globals
inputfiles = ["277-up.txt", "258-down.txt", "258-up.txt", "261-down.txt", "261-up.txt", "280-down.txt", "280-up.txt", "mb-down.txt", "mb-up.txt"]

table = {
	'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
	'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
	'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',					
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
	'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
	'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
	'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
	'TAC':'Y', 'TAT':'Y', 'TAA':'', 'TAG':'',
	'TGC':'C', 'TGT':'C', 'TGA':'', 'TGG':'W',
}
 
# Main
 
def main():
	print("Entered Main")
	for file in inputfiles: 					# Iterate through input file list
		outputName = file[0:(len(file)-4)] + ".fasta" # Generate fasta file name
		o = open(outputName, "w") 				# Open fasta output file
		lineCounter = 1 						# Reset line count for fasta file. It starts at 1 because KOALA can't handle 0 indexed fasta files for no documented reason
		with open(file, "r") as f:				# Open the current file
			for line in f:						# For each line (all sequences)
				formatLine = '>' +  str(lineCounter) +  '\n'
				o.write(str(formatLine))		# print out the fasta forma`t
				o.write(translate(line) + "\n") # and the sequence 
				lineCounter += 1 				# Increment line counter
		o.close()								# close this file, restart loop
 
def translate(seq):
	 
	protein = ""	#reset protein variable
	length = len(seq) - len(seq)%3 # Set length variable to a multiple of 3
	for i in range(0, length, 3):	# For each codon
		protein+= table[seq[i:i + 3]] # add the next single letter protein to the list
	return protein


main()