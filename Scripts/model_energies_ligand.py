from modeller import *
from modeller.scripts import complete_pdb

log.verbose()    # request verbose output
env = environ()
env.libs.topology.read(file='$(LIB)/top_heav.lib') # read topology
env.libs.parameters.read(file='$(LIB)/par.lib') # read parameters

for i in range(1, 6):
    # read model file
    code = "TvLDH.B9999%04d" % i
    mdl = complete_pdb(env, code)
    s = selection(mdl)
    s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='TvLDH.profile',
                  normalize_profile=True, smoothing_window=15)
