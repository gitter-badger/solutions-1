import pathlib
import pytest
from model import customadoption
import pandas as pd

datadir = pathlib.Path(__file__).parents[0].joinpath('data')
path1 = str(datadir.joinpath('ca_scenario_1_trr.csv'))
path2 = str(datadir.joinpath('ca_scenario_2_trr.csv'))


def test_scenarios():
    data_sources = [
        {'name': 'scenario 1', 'filename': path1, 'include': True},
        {'name': 'scenario 2', 'filename': path2, 'include': True},
    ]
    ca = customadoption.CustomAdoption(data_sources=data_sources, soln_adoption_custom_name='')
    assert len(ca.scenarios) == 2


def test_bad_CSV_file():
    path1 = str(datadir.joinpath('ca_scenario_no_world_trr.csv'))
    data_sources = [
        {'name': 'scenario no world', 'filename': path1, 'include': True},
    ]
    with pytest.raises(AssertionError):  # test validation
        ca = customadoption.CustomAdoption(data_sources=data_sources, soln_adoption_custom_name='')


def test_avg_high_low_one_scenario():
    data_sources = [
        {'name': 'scenario 1', 'filename': path1, 'include': True},
    ]
    ca = customadoption.CustomAdoption(data_sources=data_sources, soln_adoption_custom_name='')
    scen_1 = pd.read_csv(path1, index_col=0)
    avgs, _, lows = ca._avg_high_low()
    pd.testing.assert_frame_equal(avgs, scen_1, check_exact=False, check_dtype=False)
    pd.testing.assert_frame_equal(lows, scen_1, check_exact=False, check_dtype=False)


def test_avg_high_low_multiple_scenarios():
    data_sources = [
        {'name': 'scenario 1', 'filename': path1, 'include': True},
        {'name': 'scenario 2', 'filename': path2, 'include': True},
    ]
    ca = customadoption.CustomAdoption(data_sources=data_sources, soln_adoption_custom_name='')
    avg_scen = pd.read_csv(datadir.joinpath('ca_avg_trr.csv'), index_col=0)
    low_scen = pd.read_csv(datadir.joinpath('ca_low_trr.csv'), index_col=0)
    avgs, _, lows = ca._avg_high_low()
    pd.testing.assert_frame_equal(avgs, avg_scen, check_exact=False, check_dtype=False)
    pd.testing.assert_frame_equal(lows, low_scen, check_exact=False, check_dtype=False)


def test_adoption_data_per_region():
    data_sources = [
        {'name': 'scenario 1', 'filename': path1, 'include': True},
        {'name': 'scenario 2', 'filename': path2, 'include': True},
    ]
    ca = customadoption.CustomAdoption(
        data_sources=data_sources, soln_adoption_custom_name='Average of All Custom PDS Scenarios')
    expected = pd.read_csv(datadir.joinpath('ca_avg_trr.csv'), index_col=0)
    expected.name = 'adoption_data_per_region'
    result = ca.adoption_data_per_region()
    pd.testing.assert_frame_equal(result, expected, check_exact=False)

    ca = customadoption.CustomAdoption(
        data_sources=data_sources, soln_adoption_custom_name='Low of All Custom PDS Scenarios')
    expected = pd.read_csv(datadir.joinpath('ca_low_trr.csv'), index_col=0)
    expected.name = 'adoption_data_per_region'
    result = ca.adoption_data_per_region()
    pd.testing.assert_frame_equal(result, expected, check_exact=False)

    ca = customadoption.CustomAdoption(
        data_sources=data_sources, soln_adoption_custom_name='scenario 2')
    expected = pd.read_csv(path2, index_col=0)
    expected.name = 'adoption_data_per_region'
    expected.index = expected.index.astype(int)
    result = ca.adoption_data_per_region()
    pd.testing.assert_frame_equal(result, expected, check_exact=False)