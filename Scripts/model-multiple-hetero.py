from modeller import *
from modeller.automodel import *

class MyModel(automodel):
    def special_restraints(self, aln):
        rsr = self.restraints
        for ids in (('NH1:161:A', 'O1A:336:B'),
                    ('NH2:161:A', 'O1B:336:B'),
                    ('NE2:186:A', 'O2:336:B')):
            atoms = [self.atoms[i] for i in ids]
            rsr.add(forms.upper_bound(group=physical.upper_distance,
                                      feature=features.distance(*atoms),
                                      mean=3.5, stdev=0.1))

env = environ()
env.io.hetatm = True
a = MyModel(env, alnfile='TvLDH-1emd_bs.ali',
              knowns=('TvLDH_model','1emd'), sequence='TvLDH')
a.starting_model = 1
a.ending_model = 5
a.make()
