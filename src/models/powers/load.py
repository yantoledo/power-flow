from typing import Type
from .s_power import SPower
from .p_power import PPower
from .q_power import QPower


class Load:
    """ Class to define the General Power Load of the System """

    def __init__(
        self,
        s_power: Type[SPower],
        p_power: Type[PPower],
        q_power: Type[QPower],
        model: int,
        type_connection: int,
    ):
        self.s_power = s_power
        self.p_power = p_power
        self.q_power = q_power
        self.model = model
        self.type_connection = type_connection

    def get_s_a(self) -> complex:
        " Method to return the Appearance Power from phase A "
        return self.s_power.s_a

    def get_s_b(self) -> complex:
        " Method to return the Appearance Power from phase B "
        return self.s_power.s_b

    def get_s_c(self) -> complex:
        " Method to return the Appearance Power from phase C "
        return self.s_power.s_c

    def get_p_a(self) -> float:
        " Method to return the Active Power from phase A "
        return self.p_power.p_a

    def get_p_b(self) -> float:
        " Method to return the Active Power from phase B "
        return self.p_power.p_b

    def get_p_c(self) -> float:
        " Method to return the Active Power from phase C "
        return self.p_power.p_c

    def get_q_a(self) -> float:
        " Method to return the Reactive Power from phase A "
        return self.q_power.q_a

    def get_q_b(self) -> float:
        " Method to return the Reactive Power from phase B "
        return self.q_power.q_b

    def get_q_c(self) -> float:
        " Method to return the Reactive Power from phase C "
        return self.q_power.q_c
