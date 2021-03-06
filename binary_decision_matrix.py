# -*- coding: utf-8 -*-

from decision_matrix import DecisionMatrix
from loop_index.loop_index import LoopIndex

class BinaryDecisionMatrix(DecisionMatrix):
    """
    This subclass of DecisionMatrix is designed for situations whose all
    parameters are boolean. Each axis is simulated with a condition and has a
    length of 2. If a condition is true, coordinates 0 and 1 of the corresponding
    axis are false and true respectively. If a condition is false, 0 is true,
    and 1 is false.
    """

    def __init__(self, conditions):
        """
        The BinaryDecisionMatrix constructor.

        Args:
            conditions (tuplist): callable objects returning a boolean value.
                Each simulates an axis of length 2.
        """
        self._conditions = tuple(conditions)
        self._axis_count = len(self._conditions)
        self._check_presence_of_axes()
        self._matrix = dict()
        self.set_default_action(None)

    def _coordinate_is_true(self, axis, coordinate):
        if self._conditions[axis]():
            return coordinate == 1
        else:
            return coordinate == 0

    def _get_axis_length(self, axis):
        return 2

    def print_axis_values(self):
        """
        This method is a tool for debugging. It displays the boolean value of
        all conditions of all axes in the console. False and True are represented
        with 0 and 1 respectively.
        """
        axis_index = LoopIndex(self._axis_count)
        while axis_index.iterate():
            i = axis_index.get_value()
            if self._conditions[i]():
                axis = "[0, 1]"
            else:
                axis = "[1, 0]"
            print("Axis " + str(i) + ": " + axis)
