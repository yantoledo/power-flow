from .start import sum_two_numbers


def test_sum_two_numbers():
    """ testing soma function """

    result = sum_two_numbers(2, 4)

    assert result == 6
