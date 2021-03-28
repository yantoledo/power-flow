from faker import Faker
from src.models import Node
from src.models.powers import SPower, PPower, QPower, Load


faker = Faker()


def test_node_class_creation():
    """ Testing Load Creation Class """

    # Appearence Power Instance
    s_a = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    s_b = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    s_c = complex(faker.random_number(digits=2), faker.random_number(digits=2))

    appearance_power = SPower(s_a, s_b, s_c)

    # Active Power Instance
    p_a = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    p_b = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    p_c = complex(faker.random_number(digits=2), faker.random_number(digits=2))

    active_power = PPower(p_a, p_b, p_c)

    # Reactive Power Instance
    q_a = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    q_b = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    q_c = complex(faker.random_number(digits=2), faker.random_number(digits=2))

    reactive_power = QPower(q_a, q_b, q_c)

    model = faker.random_number(digits=2)
    type_connection = faker.random_number(digits=2)

    # Load Instance
    load = Load(appearance_power, active_power, reactive_power, model, type_connection)

    # Node Instance
    node_id = faker.random_number(digits=2)
    node_energyzed = True
    has_gd = True
    has_na_switch = True

    node = Node(node_id, load, node_energyzed, has_gd, has_na_switch)

    assert node.load.get_s_a() == s_a
    assert node.load.get_s_b() == s_b
    assert node.load.get_s_c() == s_c

    assert node.load.get_p_a() == p_a
    assert node.load.get_p_b() == p_b
    assert node.load.get_p_c() == p_c

    assert node.load.get_q_a() == q_a
    assert node.load.get_q_b() == q_b
    assert node.load.get_q_c() == q_c

    assert node.has_gd
    assert node.has_na_switch
    assert node.node_id == node_id
