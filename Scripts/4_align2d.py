from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='3ipv', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='3ipvA', atom_files='3ipv.pdb')
aln.append(file='ccLP3.ali', align_codes='ccLP3')
aln.align2d()
aln.write(file='ccLP3-3ipvA.ali', alignment_format='PIR')
aln.write(file='ccLP3-3ipvA.pap', alignment_format='PAP', alignment_features='INDICES HELIX BETA')
