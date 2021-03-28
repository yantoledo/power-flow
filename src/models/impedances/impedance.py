from typing import Type
from .self import SelfImpedance
from .mutual import MutualImpedance


class Impedance:
    """ Class to define the General Impedance of a Branch """

    def __init__(
        self,
        self_impedance: Type[SelfImpedance],
        mutual_impedance: Type[MutualImpedance],
    ):
        self.self_impedance = self_impedance
        self.mutual_impedance = mutual_impedance

    def get_z_aa(self) -> complex:
        " Method to return the Self Impedance from phase A "
        return self.self_impedance.z_aa

    def get_z_bb(self) -> complex:
        " Method to return the Self Impedance from phase B "
        return self.self_impedance.z_bb

    def get_z_cc(self) -> complex:
        " Method to return the Self Impedance from phase C "
        return self.self_impedance.z_cc

    def get_z_ab(self) -> complex:
        " Method to return the Mutual Impedance from phases AB "
        return self.mutual_impedance.z_ab

    def get_z_bc(self) -> complex:
        " Method to return the Mutual Impedance from phases BC "
        return self.mutual_impedance.z_bc

    def get_z_ca(self) -> float:
        " Method to return the Mutual Impedance from phase CA "
        return self.mutual_impedance.z_ca
