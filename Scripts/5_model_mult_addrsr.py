# Addition of restratints to default ones
from modeller import *
from modeller.automodel import *

log.verbose()
env = environ()

# directories for input atom files
env.io.atom_files_directory = ['.','../atom_files']


class MyModel(automodel):
	"""docstring for MyModel"""
	def special_restraints(self, aln):
		rsr = self.restraints
		at = self.atoms


		# Residues to be alpha helix
		rsr.add(secondary_structure.alpha(
			self.residue_range('10:','12:')))
		rsr.add(secondary_structure.alpha(
			self.residue_range('18:','49:')))


a = MyModel(env, alnfile = 'ccLP2-mult.ali',            # alignment filename
	knowns = ('5eyxA','5u38A','4wv8A','4xtmA','4u2aA'),  # templates
	sequence = 'ccLP2',                                 # code of the target
	assess_methods=(assess.DOPE,assess.GA341))                                      

a.starting_model = 1                           # index of the first model
a.ending_model = 5                             # index of the last model
                                               # No. of models
a.make()                                       # Compertive modeling
		