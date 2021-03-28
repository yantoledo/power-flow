# pylint: disable=redefined-outer-name
from faker import Faker
import pytest
from src.models import Node
from src.models.powers import SPower, PPower, QPower, Load


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


def test_node_class_creation(load, appearance_power, active_power, reactive_power):
    """ Testing Node Creation Class """

    # Node Instance
    node_id = faker.random_number(digits=2)
    node_energyzed = True
    has_gd = True
    has_na_switch = True

    node = Node(node_id, load, node_energyzed, has_gd, has_na_switch)

    assert node.load.get_s_a() == appearance_power.s_a
    assert node.load.get_s_b() == appearance_power.s_b
    assert node.load.get_s_c() == appearance_power.s_c

    assert node.load.get_p_a() == active_power.p_a
    assert node.load.get_p_b() == active_power.p_b
    assert node.load.get_p_c() == active_power.p_c

    assert node.load.get_q_a() == reactive_power.q_a
    assert node.load.get_q_b() == reactive_power.q_b
    assert node.load.get_q_c() == reactive_power.q_c

    assert node.has_gd
    assert node.has_na_switch
    assert node.node_id == node_id
