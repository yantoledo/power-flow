class MutualImpedance:
    """ Class to define the Mutual Impedance of a branch """

    def __init__(self, z_ab: complex, z_bc: complex, z_ca: complex):
        self.z_ab = z_ab
        self.z_bc = z_bc
        self.z_ca = z_ca
