from Levenshtein import distance
import numpy as np


class Luca:
    """simple class which filters dog names via a user provided Levenshtein score to a provided target query.
    """

    def __init__(self, target='Luca'):
        self.target = 'Luca'
        self.test_scores = None

    def compute_distance(self, name_list, score_to_select=1):
        """Computes the Levenshtein distance between target string and all other strings in a list.

        :param name_list: list of dog names
        :type name_list: list
        :param score_to_select: Levenshtein score to filter list on, defaults to 1
        :type score_to_select: int, optional
        :return: list of names filtered on a specific Levenshtein score
        :rtype: list
        """

        # Get Levenshtein distance and filter on score
        scores = np.array([distance(self.target, x) for x in name_list])
        idx = np.where(scores == score_to_select)
        selected_scores = scores[idx]

        # Save scores for later code tests
        self. test_scores = selected_scores
        selected_names = name_list[idx]

        # Convert list to set
        selected_names_set = set(selected_names)
        return selected_names_set
