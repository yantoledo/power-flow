from typing import Type
from src.models.impedances import Impedance
from .node import Node


class Branch:
    """ Class to define the system branches"""

    def __init__(
        self,
        branch_id: int,
        impedance: Type[Impedance],
        initial_node: Type[Node],
        final_node: Type[Node],
        lenth: int,
        switch_status: bool,
        switch_type: int,
    ):
        self.branch_id = branch_id
        self.impedance = impedance
        self.initial_node = initial_node
        self.final_node = final_node
        self.lenth = lenth
        self.switch_status = switch_status
        self.switch_type = switch_type
