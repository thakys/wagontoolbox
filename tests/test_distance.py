# tests/test_distance.py

from mlproject.distance import haversine

def test_result_of_distance():
    assert haversine(48.865070, 2.380009, 45.123456, 54.987654) == 5859.495864551256

def test_type_result():
    assert type(haversine(1, 1, 1, 1)) == float
