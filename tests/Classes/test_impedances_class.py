from faker import Faker
from src.models.impedances import SelfImpedance, MutualImpedance, Impedance

faker = Faker()


def test_self_impedance_class_creation():
    """ Testing Self Impedance Creation Class """
    z_aa = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    z_bb = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    z_cc = complex(faker.random_number(digits=2), faker.random_number(digits=2))

    self_impedance = SelfImpedance(z_aa, z_bb, z_cc)

    assert self_impedance.z_aa == z_aa
    assert self_impedance.z_bb == z_bb
    assert self_impedance.z_cc == z_cc


def test_mutual_impedance_class_creation():
    """ Testing Mutual Impedance Creation Class """
    z_ab = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    z_bc = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    z_ca = complex(faker.random_number(digits=2), faker.random_number(digits=2))

    mutual_impedance = MutualImpedance(z_ab, z_bc, z_ca)

    assert mutual_impedance.z_ab == z_ab
    assert mutual_impedance.z_bc == z_bc
    assert mutual_impedance.z_ca == z_ca


def test_impedance_class_creation():
    """ Testing Impedance Creation Class """

    # Self Impedance Instance
    z_aa = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    z_bb = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    z_cc = complex(faker.random_number(digits=2), faker.random_number(digits=2))

    self_impedance = SelfImpedance(z_aa, z_bb, z_cc)

    # Mutual Impedance Instance
    z_ab = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    z_bc = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    z_ca = complex(faker.random_number(digits=2), faker.random_number(digits=2))

    mutual_impedance = MutualImpedance(z_ab, z_bc, z_ca)

    # Impedance Instance
    impedance = Impedance(self_impedance, mutual_impedance)

    assert impedance.get_z_aa() == z_aa
    assert impedance.get_z_bb() == z_bb
    assert impedance.get_z_cc() == z_cc
    assert impedance.get_z_ab() == z_ab
    assert impedance.get_z_bc() == z_bc
    assert impedance.get_z_ca() == z_ca
