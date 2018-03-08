from modeller import *
from modeller.automodel import *

env = environ()
a = automodel(env, alnfile='ccLP3-mult.ali',
              knowns=('1ukgA','3ipvA','3zyrA'), sequence='ccLP3',
              assess_methods=(assess.DOPE,
                              #soap_protein_od.Scorer(),
                              assess.GA341))
a.starting_model = 1
a.ending_model = 5
a.make()
