import pathlib
from src.corpus import plotting


def test_get_ranks_and_frequencies():
    """Test ranks and frequencies counting"""
    test_file = pathlib.Path(__file__).parent / "test_ranks_and_frequencies.txt"
    expected = [(1, 3), (2, 2), (3, 2), (4, 1), (5, 1)]
    actual = plotting.get_ranks_and_frequencies(test_file)
    assert expected == actual, "Search in Document failed"
