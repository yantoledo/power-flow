from typing import Type
from src.models.powers import Load


class Node:
    """ Class to define the system bus """

    def __init__(
        self,
        node_id: int,
        load: Type[Load],
        node_energyzed: bool,
        has_gd: bool,
        has_na_switch: bool,
    ):
        self.node_id = node_id
        self.load = load
        self.node_energyzed = node_energyzed
        self.has_gd = has_gd
        self.has_na_switch = has_na_switch
