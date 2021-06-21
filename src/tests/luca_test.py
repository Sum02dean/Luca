import sys
import os
import pandas as pd
import numpy as np
import pytest
sys.path.append(os.path.abspath('../'))  # nopep8
from classes.luca import Luca  # nopep8


def test_method():
    L = Luca(target='Luca')
    # Grab data
    x = pd.read_csv('../../data/20210103_hundenamen.csv')
    dog_names = x.HUNDENAME.values

    # Check all scores evaluate to exactly 1
    r = L.compute_distance(dog_names)
    assert [x for x in L.test_scores] == [
        1 for x in range(0, len(L.test_scores))]
