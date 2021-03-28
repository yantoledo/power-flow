from faker import Faker
from src.models.powers import SPower, QPower, PPower, Load

faker = Faker()


def test_self_spower_class_creation():
    """ Testing Appearance Power Creation Class """
    s_a = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    s_b = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    s_c = complex(faker.random_number(digits=2), faker.random_number(digits=2))

    appearance_power = SPower(s_a, s_b, s_c)

    assert appearance_power.s_a == s_a
    assert appearance_power.s_b == s_b
    assert appearance_power.s_c == s_c


def test_reactive_power_class_creation():
    """ Testing Reactive Power Creation Class """
    q_a = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    q_b = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    q_c = complex(faker.random_number(digits=2), faker.random_number(digits=2))

    reactive_power = QPower(q_a, q_b, q_c)

    assert reactive_power.q_a == q_a
    assert reactive_power.q_b == q_b
    assert reactive_power.q_c == q_c


def test_impedance_class_creation():
    """ Testing Active Power Creation Class """

    p_a = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    p_b = complex(faker.random_number(digits=2), faker.random_number(digits=2))
    p_c = complex(faker.random_number(digits=2), faker.random_number(digits=2))

    active_power = PPower(p_a, p_b, p_c)

    assert active_power.p_a == p_a
    assert active_power.p_b == p_b
    assert active_power.p_c == p_c


def test_load_class_creation():
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

    assert load.get_s_a() == s_a
    assert load.get_s_b() == s_b
    assert load.get_s_c() == s_c

    assert load.get_p_a() == p_a
    assert load.get_p_b() == p_b
    assert load.get_p_c() == p_c

    assert load.get_q_a() == q_a
    assert load.get_q_b() == q_b
    assert load.get_q_c() == q_c

    assert load.model == model
    assert load.type_connection == type_connection
