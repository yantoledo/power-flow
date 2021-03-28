class SelfImpedance:
    """ Class to define the Self Impedance of a branch """

    def __init__(self, z_aa: complex, z_bb: complex, z_cc: complex):
        self.z_aa = z_aa
        self.z_bb = z_bb
        self.z_cc = z_cc
