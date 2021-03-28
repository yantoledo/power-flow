# pylint: disable=redefined-outer-name
from faker import Faker
import pytest
from src.models import Branch, Node
from src.models.powers import SPower, PPower, QPower, Load
from src.models.impedances import SelfImpedance, MutualImpedance, Impedance

faker = Faker()


@pytest.fixture
def appearance_power():
    """ Make Appearance Power Class Mock """
    # Appearence Power Instance
    s_a = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    s_b = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    s_c = complex(faker.random_number(digits=2), faker.random_number(digits=2))

    return SPower(s_a, s_b, s_c)


@pytest.fixture
def active_power():
    """ Make Active Power Class Mock """
    # Active Power Instance
    p_a = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    p_b = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    p_c = complex(faker.random_number(digits=2), faker.random_number(digits=2))

    return PPower(p_a, p_b, p_c)


@pytest.fixture
def reactive_power():
    """ Make Reactive Power Class Mock """
    # Reactive Power Instance
    q_a = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    q_b = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    q_c = complex(faker.random_number(digits=2), faker.random_number(digits=2))

    return QPower(q_a, q_b, q_c)


@pytest.fixture
def load(appearance_power, active_power, reactive_power):
    """ Make Load Class Mock """
    # Load Instance
    model = faker.random_number(digits=2)
    type_connection = faker.random_number(digits=2)
    return Load(appearance_power, active_power, reactive_power, model, type_connection)


@pytest.fixture
def node(load):
    """ Make Load Class Mock """
    # Node Instance
    node_id = faker.random_number(digits=2)
    node_energyzed = True
    has_gd = True
    has_na_switch = True

    return Node(node_id, load, node_energyzed, has_gd, has_na_switch)


@pytest.fixture
def self_impedance():
    """ Make Self Impedance Class Mock """
    # Self Impedance Instance
    z_aa = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    z_bb = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    z_cc = complex(faker.random_number(digits=2), faker.random_number(digits=2))

    return SelfImpedance(z_aa, z_bb, z_cc)


@pytest.fixture
def mutual_impedance():
    """ Make Mutual Impedance Class Mock """
    # Mutual Impedance Instance
    z_ab = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    z_bc = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    z_ca = complex(faker.random_number(digits=2), faker.random_number(digits=2))

    return MutualImpedance(z_ab, z_bc, z_ca)


@pytest.fixture
def impedance(self_impedance, mutual_impedance):
    """ Make Impedance Class Mock """
    # Impedance Instance
    return Impedance(self_impedance, mutual_impedance)


def test_branch_class_creation(impedance, node):
    """ Testing Branch Class Creation """

    # Branch Instance
    branch_id = faker.random_number(digits=2)
    length = faker.random_number(digits=2)
    switch_status = True
    switch_type = faker.random_number(digits=2)

    branch = Branch(
        branch_id, impedance, node, node, length, switch_status, switch_type
    )

    assert branch.branch_id == branch_id
    assert branch.switch_status
    assert branch.switch_type == switch_type
    assert branch.lenth == length
    assert branch.initial_node == node
    assert branch.final_node == node
    assert branch.impedance == impedance
