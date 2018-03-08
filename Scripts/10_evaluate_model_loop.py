from modeller import *
from modeller.scripts import complete_pdb

log.verbose()    # request verbose output
env = environ()
env.libs.topology.read(file='$(LIB)/top_heav.lib') # read topology
env.libs.parameters.read(file='$(LIB)/par.lib') # read parameters

# directories for input atom files
env.io.atom_files_directory = './:../atom_files'

# read model file
mdl = complete_pdb(env, 'ccLLP.BL00090001.pdb')

s = selection(mdl)
s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='loop.profile',
              normalize_profile=True, smoothing_window=15)
