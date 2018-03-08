from modeller import *
import sys
import os

# input 
directory = sys.argv[1]

e = environ()
e.io.atom_files_directory = [directory]

pdbs = os.listdir(directory)

for pdb in pdbs:
	code = pdb
	m = model(e, file = code)

	m.make_chains(file=code, minimal_chain_length = 30, minimal_stdres= 30,
		chop_nonstd_termini=True, max_nonstdres=10,
		minimal_resolution=99.0, structure_types='structureN structureX')