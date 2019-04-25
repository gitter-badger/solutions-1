"""Tests for interpolation.py."""  # by Denton Gentry
# by Denton Gentry
import numpy as np  # by Denton Gentry
import pandas as pd  # by Denton Gentry
import pytest  # by Denton Gentry
from model import interpolation as itrp  # by Denton Gentry


# by Denton Gentry
# by Denton Gentry
def test_linear_trend():  # by Denton Gentry
    adoption_low_med_high = pd.DataFrame(adoption_low_med_high_list[1:],  # by Denton Gentry
                                         columns=adoption_low_med_high_list[0], dtype=np.float64).set_index(
        'Year')  # by Denton Gentry
    result = itrp.linear_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    expected = pd.DataFrame(linear_trend_list[1:], columns=linear_trend_list[0],  # by Denton Gentry
                            dtype=np.float64).set_index('Year')  # by Denton Gentry
    expected.index = expected.index.astype(int)  # by Denton Gentry
    pd.testing.assert_frame_equal(result, expected, check_exact=False)  # by Denton Gentry
    result = itrp.trend_algorithm(data=adoption_low_med_high.loc[:, 'Medium'], trend='linear')  # by Denton Gentry
    pd.testing.assert_frame_equal(result, expected, check_exact=False)  # by Denton Gentry
    # by Denton Gentry


def test_linear_trend_with_NaN_data():  # by Denton Gentry
    adoption_low_med_high = pd.DataFrame(tam_low_med_high_NaN_years_list[1:],  # by Denton Gentry
                                         columns=tam_low_med_high_NaN_years_list[0], dtype=np.float64).set_index(
        'Year')  # by Denton Gentry
    result = itrp.linear_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    expected = pd.DataFrame(linear_with_NaN_trend_list[1:], columns=linear_with_NaN_trend_list[0],  # by Denton Gentry
                            dtype=np.float64).set_index('Year')  # by Denton Gentry
    expected.index = expected.index.astype(int)  # by Denton Gentry
    pd.testing.assert_frame_equal(result, expected, check_exact=False)  # by Denton Gentry
    result = itrp.trend_algorithm(data=adoption_low_med_high.loc[:, 'Medium'], trend='linear')  # by Denton Gentry
    pd.testing.assert_frame_equal(result, expected, check_exact=False)  # by Denton Gentry
    # by Denton Gentry


def test_poly_degree2_trend():  # by Denton Gentry
    adoption_low_med_high = pd.DataFrame(adoption_low_med_high_list[1:],  # by Denton Gentry
                                         columns=adoption_low_med_high_list[0], dtype=np.float64).set_index(
        'Year')  # by Denton Gentry
    result = itrp.poly_degree2_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    expected = pd.DataFrame(poly_degree2_trend_list[1:], columns=poly_degree2_trend_list[0],  # by Denton Gentry
                            dtype=np.float64).set_index('Year')  # by Denton Gentry
    expected.index = expected.index.astype(int)  # by Denton Gentry
    pd.testing.assert_frame_equal(result, expected, check_exact=False)  # by Denton Gentry
    result = itrp.trend_algorithm(data=adoption_low_med_high.loc[:, 'Medium'], trend='degree2')  # by Denton Gentry
    pd.testing.assert_frame_equal(result, expected, check_exact=False)  # by Denton Gentry
    result = itrp.trend_algorithm(data=adoption_low_med_high.loc[:, 'Medium'], trend='2nd Poly')  # by Denton Gentry
    pd.testing.assert_frame_equal(result, expected, check_exact=False)  # by Denton Gentry
    # by Denton Gentry


def test_poly_degree3_trend():  # by Denton Gentry
    adoption_low_med_high = pd.DataFrame(adoption_low_med_high_list[1:],  # by Denton Gentry
                                         columns=adoption_low_med_high_list[0], dtype=np.float64).set_index(
        'Year')  # by Denton Gentry
    result = itrp.poly_degree3_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    expected = pd.DataFrame(poly_degree3_trend_list[1:], columns=poly_degree3_trend_list[0],  # by Denton Gentry
                            dtype=np.float64).set_index('Year')  # by Denton Gentry
    expected.index = expected.index.astype(int)  # by Denton Gentry
    pd.testing.assert_frame_equal(result, expected, check_exact=False)  # by Denton Gentry
    result = itrp.trend_algorithm(data=adoption_low_med_high.loc[:, 'Medium'], trend='degree3')  # by Denton Gentry
    pd.testing.assert_frame_equal(result, expected, check_exact=False)  # by Denton Gentry
    result = itrp.trend_algorithm(data=adoption_low_med_high.loc[:, 'Medium'], trend='3rd Poly')  # by Denton Gentry
    pd.testing.assert_frame_equal(result, expected, check_exact=False)  # by Denton Gentry
    # by Denton Gentry


def test_exponential_trend():  # by Denton Gentry
    adoption_low_med_high = pd.DataFrame(adoption_low_med_high_list[1:],  # by Denton Gentry
                                         columns=adoption_low_med_high_list[0], dtype=np.float64).set_index(
        'Year')  # by Denton Gentry
    result = itrp.exponential_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    expected = pd.DataFrame(exponential_trend_list[1:], columns=exponential_trend_list[0],  # by Denton Gentry
                            dtype=np.float64).set_index('Year')  # by Denton Gentry
    expected.index = expected.index.astype(int)  # by Denton Gentry
    pd.testing.assert_frame_equal(result, expected, check_exact=False)  # by Denton Gentry
    result = itrp.trend_algorithm(data=adoption_low_med_high.loc[:, 'Medium'], trend='exponential')  # by Denton Gentry
    pd.testing.assert_frame_equal(result, expected, check_exact=False)  # by Denton Gentry
    # by Denton Gentry


def test_invalid_trend():  # by Denton Gentry
    with pytest.raises(ValueError):  # by Denton Gentry
        _ = itrp.trend_algorithm(data=None, trend='invalid')  # by Denton Gentry
    # by Denton Gentry


def test_missing_data():  # by Denton Gentry
    adoption_low_med_high = pd.DataFrame(missing_data_low_med_high_list[1:],  # by Denton Gentry
                                         columns=missing_data_low_med_high_list[0], dtype=np.float64).set_index(
        'Year')  # by Denton Gentry
    # adoption_low_med_high.loc[[2012, 2013, ... 2020]] gets an error, not sure why  # by Denton Gentry
    adoption_low_med_high.loc[2012] = np.nan  # by Denton Gentry
    adoption_low_med_high.loc[2013] = np.nan  # by Denton Gentry
    adoption_low_med_high.loc[2014] = np.nan  # by Denton Gentry
    adoption_low_med_high.loc[2015] = np.nan  # by Denton Gentry
    adoption_low_med_high.loc[2016] = np.nan  # by Denton Gentry
    adoption_low_med_high.loc[2017] = np.nan  # by Denton Gentry
    adoption_low_med_high.loc[2018] = np.nan  # by Denton Gentry
    adoption_low_med_high.loc[2019] = np.nan  # by Denton Gentry
    adoption_low_med_high = adoption_low_med_high.sort_index()  # by Denton Gentry
    adoption_low_med_high.index = adoption_low_med_high.index.astype(int)  # by Denton Gentry
    result = itrp.linear_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    expected = pd.DataFrame(linear_missing_data_trend_list[1:],  # by Denton Gentry
                            columns=linear_missing_data_trend_list[0],  # by Denton Gentry
                            dtype=np.float64).set_index('Year')  # by Denton Gentry
    expected.index = expected.index.astype(int)  # by Denton Gentry
    pd.testing.assert_frame_equal(result, expected, check_exact=False)  # by Denton Gentry
    # by Denton Gentry
    result = itrp.poly_degree2_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    expected = pd.DataFrame(poly_degree2_missing_data_trend_list[1:],  # by Denton Gentry
                            columns=poly_degree2_missing_data_trend_list[0],  # by Denton Gentry
                            dtype=np.float64).set_index('Year')  # by Denton Gentry
    expected.index = expected.index.astype(int)  # by Denton Gentry
    pd.testing.assert_frame_equal(result, expected, check_exact=False)  # by Denton Gentry
    # by Denton Gentry
    result = itrp.poly_degree3_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    expected = pd.DataFrame(poly_degree3_missing_data_trend_list[1:],  # by Denton Gentry
                            columns=poly_degree3_missing_data_trend_list[0],  # by Denton Gentry
                            dtype=np.float64).set_index('Year')  # by Denton Gentry
    expected.index = expected.index.astype(int)  # by Denton Gentry
    pd.testing.assert_frame_equal(result, expected, check_exact=False)  # by Denton Gentry
    # by Denton Gentry
    result = itrp.exponential_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    expected = pd.DataFrame(exponential_missing_data_trend_list[1:],  # by Denton Gentry
                            columns=exponential_missing_data_trend_list[0],  # by Denton Gentry
                            dtype=np.float64).set_index('Year')  # by Denton Gentry
    expected.index = expected.index.astype(int)  # by Denton Gentry
    pd.testing.assert_frame_equal(result, expected, check_exact=False)  # by Denton Gentry
    # by Denton Gentry


def test_nan_data():  # by Denton Gentry
    adoption_low_med_high = pd.DataFrame(adoption_low_med_high_list[1:],  # by Denton Gentry
                                         columns=adoption_low_med_high_list[0], dtype=np.float64).set_index(
        'Year')  # by Denton Gentry
    adoption_low_med_high.loc[:, :] = np.nan  # by Denton Gentry
    result = itrp.linear_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    assert result.isna().all(axis=None, skipna=False)  # by Denton Gentry
    result = itrp.poly_degree2_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    assert result.isna().all(axis=None, skipna=False)  # by Denton Gentry
    result = itrp.poly_degree3_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    assert result.isna().all(axis=None, skipna=False)  # by Denton Gentry
    result = itrp.exponential_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    assert result.isna().all(axis=None, skipna=False)  # by Denton Gentry
    # by Denton Gentry


def test_empty_data():  # by Denton Gentry
    adoption_low_med_high = pd.DataFrame(columns=['Low', 'Medium', 'High'])  # by Denton Gentry
    result = itrp.linear_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    assert result.isna().all(axis=None, skipna=False)  # by Denton Gentry
    result = itrp.poly_degree2_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    assert result.isna().all(axis=None, skipna=False)  # by Denton Gentry
    result = itrp.poly_degree3_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    assert result.isna().all(axis=None, skipna=False)  # by Denton Gentry
    result = itrp.exponential_trend(adoption_low_med_high.loc[:, 'Medium'])  # by Denton Gentry
    assert result.isna().all(axis=None, skipna=False)  # by Denton Gentry
    # by Denton Gentry
    # by Denton Gentry


g_data_sources = {  # by Denton Gentry
    'Ambitious Cases': {  # by Denton Gentry
        'Ambitious 1': 'filename1',  # by Denton Gentry
        'Ambitious 2': 'filename2',  # by Denton Gentry
    },  # by Denton Gentry
    'Baseline Cases': {  # by Denton Gentry
        'Baseline 1': 'filename1',  # by Denton Gentry
    },  # by Denton Gentry
    'Conservative Cases': {  # by Denton Gentry
        'Conservative 1': 'filename1',  # by Denton Gentry
    },  # by Denton Gentry
    '100% REN': {  # by Denton Gentry
    },  # by Denton Gentry
}  # by Denton Gentry
g_all_data_sources = ['Ambitious 1', 'Ambitious 2', 'Baseline 1', 'Conservative 1']  # by Denton Gentry


# by Denton Gentry
def test_matching_data_sources():  # by Denton Gentry
    assert sorted(itrp.matching_data_sources(data_sources=g_data_sources,  # by Denton Gentry
                                             name='Ambitious Cases', groups_only=False)) == sorted(
        ['Ambitious 1', 'Ambitious 2'])  # by Denton Gentry
    assert itrp.matching_data_sources(data_sources=g_data_sources,  # by Denton Gentry
                                      name='Baseline Cases', groups_only=False) == ['Baseline 1']  # by Denton Gentry
    assert itrp.matching_data_sources(data_sources=g_data_sources,  # by Denton Gentry
                                      name='Conservative Cases', groups_only=False) == [
               'Conservative 1']  # by Denton Gentry
    sorted_all_sources = sorted(['Ambitious 1', 'Ambitious 2', 'Baseline 1', 'Conservative 1'])  # by Denton Gentry
    result = itrp.matching_data_sources(data_sources=g_data_sources,  # by Denton Gentry
                                        name='ALL SOURCES', groups_only=False)  # by Denton Gentry
    assert sorted(result) == sorted_all_sources  # by Denton Gentry
    assert itrp.matching_data_sources(data_sources=g_data_sources,  # by Denton Gentry
                                      name='100% REN', groups_only=False) == []  # by Denton Gentry
    assert itrp.matching_data_sources(data_sources=g_data_sources,  # by Denton Gentry
                                      name=None, groups_only=False) == None  # by Denton Gentry
    # by Denton Gentry


def test_matching_data_sources_no_such_group():  # by Denton Gentry
    assert itrp.matching_data_sources(data_sources=g_data_sources,  # by Denton Gentry
                                      name='no such group', groups_only=False) == None  # by Denton Gentry
    # by Denton Gentry


def test_groups_only():  # by Denton Gentry
    assert itrp.matching_data_sources(data_sources=g_data_sources, name='Ambitious 1',  # by Denton Gentry
                                      groups_only=False) == ['Ambitious 1']  # by Denton Gentry
    assert sorted(itrp.matching_data_sources(data_sources=g_data_sources, name='Ambitious 1',  # by Denton Gentry
                                             groups_only=True)) == sorted(g_all_data_sources)  # by Denton Gentry
    # by Denton Gentry


def test_all_and_empty_result():  # by Denton Gentry
    assert itrp.matching_data_sources(data_sources=g_data_sources, name='100% REN',  # by Denton Gentry
                                      groups_only=False) == []  # by Denton Gentry
    assert sorted(itrp.matching_data_sources(data_sources=g_data_sources, name='ALL SOURCES',  # by Denton Gentry
                                             groups_only=False)) == sorted(g_all_data_sources)  # by Denton Gentry
    # by Denton Gentry


def test_is_group_name():  # by Denton Gentry
    assert itrp.is_group_name(data_sources=g_data_sources, name='Ambitious Cases') == True  # by Denton Gentry
    assert itrp.is_group_name(data_sources=g_data_sources, name='ALL SOURCES') == True  # by Denton Gentry
    assert itrp.is_group_name(data_sources=g_data_sources, name='Ambitious 1') == False  # by Denton Gentry
    assert itrp.is_group_name(data_sources=g_data_sources, name=None) == False  # by Denton Gentry
    with pytest.raises(ValueError):  # by Denton Gentry
        _ = itrp.is_group_name(data_sources=g_data_sources, name='not a group name')  # by Denton Gentry
    # by Denton Gentry


def test_is_group_name_improvedstoves():  # by Denton Gentry
    # test a specific case from ImprovedCookStoves  # by Denton Gentry
    data_sources = {  # by Denton Gentry
        'Baseline Cases': {  # by Denton Gentry
            'Global alliance For Clean cookstoves - Interpolated': 'filename1',  # by Denton Gentry
            'International Energy Agency - Interpolated': 'filename2',  # by Denton Gentry
            'The World Bank': 'filename3',  # by Denton Gentry
        },  # by Denton Gentry
        'Conservative Cases': {  # by Denton Gentry
        },  # by Denton Gentry
        'Ambitious Cases': {  # by Denton Gentry
        },  # by Denton Gentry
        'Maximum Cases': {  # by Denton Gentry
        },  # by Denton Gentry
    }  # by Denton Gentry
    assert itrp.is_group_name(data_sources=data_sources, name='Baseline Cases') == True  # by Denton Gentry
    assert itrp.is_group_name(data_sources=data_sources, name='The World Bank') == False  # by Denton Gentry
    # by Denton Gentry
    # by Denton Gentry


# SolarPVUtil 'Adoption Data'!AB46:AD94  # by Denton Gentry
adoption_low_med_high_list = [['Year', 'Low', 'Medium', 'High'],  # by Denton Gentry
                              [2012, 58.200000, 58.200000, 58.200000], [2013, 81.060000, 81.060000, 81.060000],
                              # by Denton Gentry
                              [2014, 112.633033, 112.633033, 112.633033], [2015, 138.403698, 176.240921, 214.078144],
                              # by Denton Gentry
                              [2016, 221.118595, 272.031352, 322.944109], [2017, 312.381791, 383.309352, 454.236913],
                              # by Denton Gentry
                              [2018, 412.974691, 509.379474, 605.784256], [2019, 523.185314, 649.546273, 775.907231],
                              # by Denton Gentry
                              [2020, 500.486594, 654.000000, 807.513406], [2021, 771.946597, 969.388115, 1166.829634],
                              # by Denton Gentry
                              [2022, 909.853893, 1147.672267, 1385.490641],
                              [2023, 1056.253096, 1337.271311, 1618.289526],  # by Denton Gentry
                              [2024, 1210.700727, 1537.489801, 1864.278876],
                              [2025, 1265.160143, 1595.400000, 1925.639857],  # by Denton Gentry
                              [2026, 1541.862231, 1967.003336, 2392.144441],
                              [2027, 1717.612329, 2194.907488, 2672.202647],  # by Denton Gentry
                              [2028, 1899.495352, 2430.649302, 2961.803253],
                              [2029, 2086.990245, 2673.533332, 3260.076420],  # by Denton Gentry
                              [2030, 2361.039771, 3040.200000, 3719.360229],
                              [2031, 2476.785301, 3177.946255, 3879.107210],  # by Denton Gentry
                              [2032, 2678.020412, 3438.084256, 4198.148100],
                              [2033, 2882.766540, 3702.582689, 4522.398837],  # by Denton Gentry
                              [2034, 3090.469022, 3970.746106, 4851.023191],
                              [2035, 3294.571903, 4241.879064, 5189.186224],  # by Denton Gentry
                              [2036, 3512.441874, 4515.286114, 5518.130355],
                              [2037, 3725.553339, 4790.271812, 5854.990285],  # by Denton Gentry
                              [2038, 3939.272082, 5066.140711, 6193.009340],
                              [2039, 4152.965387, 5342.197365, 6531.429344],  # by Denton Gentry
                              [2040, 4394.843061, 5665.200000, 6935.556939],
                              [2041, 4577.714588, 5892.092154, 7206.469721],  # by Denton Gentry
                              [2042, 4787.420703, 6164.539397, 7541.658092],
                              [2043, 4994.406010, 6434.392611, 7874.379213],  # by Denton Gentry
                              [2044, 5197.943507, 6700.956350, 8203.969193],
                              [2045, 5402.182194, 6963.535167, 8524.888140],  # by Denton Gentry
                              [2046, 5591.599994, 7221.433617, 8851.267240],
                              [2047, 5780.112723, 7473.956253, 9167.799784],  # by Denton Gentry
                              [2048, 5961.967390, 7720.407630, 9478.847871],
                              [2049, 6136.269626, 7960.092301, 9783.914977],  # by Denton Gentry
                              [2050, 6284.441079, 8167.800000, 10051.158921],
                              [2051, 6457.338827, 8416.379743, 10375.420659],  # by Denton Gentry
                              [2052, 6604.579123, 8631.591621, 10658.604119],
                              [2053, 6739.190765, 8837.255009, 10935.319253],  # by Denton Gentry
                              [2054, 6861.330435, 9032.674462, 11204.018488],
                              [2055, 6969.910301, 9217.154532, 11464.398763],  # by Denton Gentry
                              [2056, 7063.805739, 9389.999774, 11716.193809],
                              [2057, 7141.873711, 9550.514742, 11959.155773],  # by Denton Gentry
                              [2058, 7202.930366, 9698.003990, 12193.077613],
                              [2059, 7245.770888, 9831.772071, 12417.773254],  # by Denton Gentry
                              [2060, 7269.169476, 9951.123540, 12633.077604]]  # by Denton Gentry
# by Denton Gentry
# SolarPVUtil 'Adoption Data'!BW50:CA96  # by Denton Gentry
linear_trend_list = [['Year', 'x', 'constant', 'adoption'],  # by Denton Gentry
                     [2014, 0.000000, -445.045081, -445.045081], [2015, 232.618862, -445.045081, -212.426218],
                     # by Denton Gentry
                     [2016, 465.237725, -445.045081, 20.192644], [2017, 697.856587, -445.045081, 252.811506],
                     # by Denton Gentry
                     [2018, 930.475450, -445.045081, 485.430369], [2019, 1163.094312, -445.045081, 718.049231],
                     # by Denton Gentry
                     [2020, 1395.713174, -445.045081, 950.668094], [2021, 1628.332037, -445.045081, 1183.286956],
                     # by Denton Gentry
                     [2022, 1860.950899, -445.045081, 1415.905818], [2023, 2093.569761, -445.045081, 1648.524681],
                     # by Denton Gentry
                     [2024, 2326.188624, -445.045081, 1881.143543], [2025, 2558.807486, -445.045081, 2113.762406],
                     # by Denton Gentry
                     [2026, 2791.426349, -445.045081, 2346.381268], [2027, 3024.045211, -445.045081, 2579.000130],
                     # by Denton Gentry
                     [2028, 3256.664073, -445.045081, 2811.618993], [2029, 3489.282936, -445.045081, 3044.237855],
                     # by Denton Gentry
                     [2030, 3721.901798, -445.045081, 3276.856717], [2031, 3954.520660, -445.045081, 3509.475580],
                     # by Denton Gentry
                     [2032, 4187.139523, -445.045081, 3742.094442], [2033, 4419.758385, -445.045081, 3974.713305],
                     # by Denton Gentry
                     [2034, 4652.377248, -445.045081, 4207.332167], [2035, 4884.996110, -445.045081, 4439.951029],
                     # by Denton Gentry
                     [2036, 5117.614972, -445.045081, 4672.569892], [2037, 5350.233835, -445.045081, 4905.188754],
                     # by Denton Gentry
                     [2038, 5582.852697, -445.045081, 5137.807617], [2039, 5815.471560, -445.045081, 5370.426479],
                     # by Denton Gentry
                     [2040, 6048.090422, -445.045081, 5603.045341], [2041, 6280.709284, -445.045081, 5835.664204],
                     # by Denton Gentry
                     [2042, 6513.328147, -445.045081, 6068.283066], [2043, 6745.947009, -445.045081, 6300.901928],
                     # by Denton Gentry
                     [2044, 6978.565871, -445.045081, 6533.520791], [2045, 7211.184734, -445.045081, 6766.139653],
                     # by Denton Gentry
                     [2046, 7443.803596, -445.045081, 6998.758516], [2047, 7676.422459, -445.045081, 7231.377378],
                     # by Denton Gentry
                     [2048, 7909.041321, -445.045081, 7463.996240], [2049, 8141.660183, -445.045081, 7696.615103],
                     # by Denton Gentry
                     [2050, 8374.279046, -445.045081, 7929.233965], [2051, 8606.897908, -445.045081, 8161.852827],
                     # by Denton Gentry
                     [2052, 8839.516771, -445.045081, 8394.471690], [2053, 9072.135633, -445.045081, 8627.090552],
                     # by Denton Gentry
                     [2054, 9304.754495, -445.045081, 8859.709415], [2055, 9537.373358, -445.045081, 9092.328277],
                     # by Denton Gentry
                     [2056, 9769.992220, -445.045081, 9324.947139], [2057, 10002.611082, -445.045081, 9557.566002],
                     # by Denton Gentry
                     [2058, 10235.229945, -445.045081, 9790.184864], [2059, 10467.848807, -445.045081, 10022.803727],
                     # by Denton Gentry
                     [2060, 10700.467670, -445.045081, 10255.422589]]  # by Denton Gentry
# by Denton Gentry
# SolarPVUtil 'Adoption Data'!CF50:CI96  # by Denton Gentry
poly_degree2_trend_list = [['Year', 'x^2', 'x', 'constant', 'adoption'],  # by Denton Gentry
                           [2014, 0.000000, 0.000000, -216.892778, -216.892778],  # by Denton Gentry
                           [2015, 0.803353, 197.271322, -216.892778, -18.818102],  # by Denton Gentry
                           [2016, 3.213413, 394.542645, -216.892778, 180.863280],  # by Denton Gentry
                           [2017, 7.230179, 591.813967, -216.892778, 382.151368],  # by Denton Gentry
                           [2018, 12.853651, 789.085290, -216.892778, 585.046163],  # by Denton Gentry
                           [2019, 20.083829, 986.356612, -216.892778, 789.547664],  # by Denton Gentry
                           [2020, 28.920714, 1183.627935, -216.892778, 995.655872],  # by Denton Gentry
                           [2021, 39.364306, 1380.899257, -216.892778, 1203.370786],  # by Denton Gentry
                           [2022, 51.414603, 1578.170580, -216.892778, 1412.692406],  # by Denton Gentry
                           [2023, 65.071608, 1775.441902, -216.892778, 1623.620732],  # by Denton Gentry
                           [2024, 80.335318, 1972.713225, -216.892778, 1836.155765],  # by Denton Gentry
                           [2025, 97.205735, 2169.984547, -216.892778, 2050.297504],  # by Denton Gentry
                           [2026, 115.682858, 2367.255870, -216.892778, 2266.045950],  # by Denton Gentry
                           [2027, 135.766687, 2564.527192, -216.892778, 2483.401102],  # by Denton Gentry
                           [2028, 157.457223, 2761.798515, -216.892778, 2702.362960],  # by Denton Gentry
                           [2029, 180.754465, 2959.069837, -216.892778, 2922.931525],  # by Denton Gentry
                           [2030, 205.658414, 3156.341160, -216.892778, 3145.106796],  # by Denton Gentry
                           [2031, 232.169069, 3353.612482, -216.892778, 3368.888773],  # by Denton Gentry
                           [2032, 260.286430, 3550.883805, -216.892778, 3594.277457],  # by Denton Gentry
                           [2033, 290.010498, 3748.155127, -216.892778, 3821.272847],  # by Denton Gentry
                           [2034, 321.341272, 3945.426450, -216.892778, 4049.874944],  # by Denton Gentry
                           [2035, 354.278752, 4142.697772, -216.892778, 4280.083747],  # by Denton Gentry
                           [2036, 388.822939, 4339.969095, -216.892778, 4511.899256],  # by Denton Gentry
                           [2037, 424.973832, 4537.240417, -216.892778, 4745.321471],  # by Denton Gentry
                           [2038, 462.731431, 4734.511739, -216.892778, 4980.350393],  # by Denton Gentry
                           [2039, 502.095737, 4931.783062, -216.892778, 5216.986022],  # by Denton Gentry
                           [2040, 543.066749, 5129.054384, -216.892778, 5455.228356],  # by Denton Gentry
                           [2041, 585.644468, 5326.325707, -216.892778, 5695.077397],  # by Denton Gentry
                           [2042, 629.828893, 5523.597029, -216.892778, 5936.533145],  # by Denton Gentry
                           [2043, 675.620024, 5720.868352, -216.892778, 6179.595598],  # by Denton Gentry
                           [2044, 723.017862, 5918.139674, -216.892778, 6424.264758],  # by Denton Gentry
                           [2045, 772.022406, 6115.410997, -216.892778, 6670.540625],  # by Denton Gentry
                           [2046, 822.633656, 6312.682319, -216.892778, 6918.423198],  # by Denton Gentry
                           [2047, 874.851613, 6509.953642, -216.892778, 7167.912477],  # by Denton Gentry
                           [2048, 928.676276, 6707.224964, -216.892778, 7419.008462],  # by Denton Gentry
                           [2049, 984.107645, 6904.496287, -216.892778, 7671.711154],  # by Denton Gentry
                           [2050, 1041.145721, 7101.767609, -216.892778, 7926.020552],  # by Denton Gentry
                           [2051, 1099.790503, 7299.038932, -216.892778, 8181.936657],  # by Denton Gentry
                           [2052, 1160.041991, 7496.310254, -216.892778, 8439.459468],  # by Denton Gentry
                           [2053, 1221.900186, 7693.581577, -216.892778, 8698.588985],  # by Denton Gentry
                           [2054, 1285.365087, 7890.852899, -216.892778, 8959.325209],  # by Denton Gentry
                           [2055, 1350.436695, 8088.124222, -216.892778, 9221.668139],  # by Denton Gentry
                           [2056, 1417.115009, 8285.395544, -216.892778, 9485.617775],  # by Denton Gentry
                           [2057, 1485.400029, 8482.666867, -216.892778, 9751.174118],  # by Denton Gentry
                           [2058, 1555.291756, 8679.938189, -216.892778, 10018.337167],  # by Denton Gentry
                           [2059, 1626.790189, 8877.209511, -216.892778, 10287.106923],  # by Denton Gentry
                           [2060, 1699.895328, 9074.480834, -216.892778, 10557.483384]]  # by Denton Gentry
# by Denton Gentry
# SolarPVUtil 'Adoption Data'!CN50:CR96  # by Denton Gentry
poly_degree3_trend_list = [['Year', 'x^3', 'x^2', 'x', 'constant', 'adoption'],  # by Denton Gentry
                           [2014, 0.000000, 0.000000, 0.000000, 111.343842, 111.343842],  # by Denton Gentry
                           [2015, -0.120128, 8.731774, 66.067972, 111.343842, 186.023460],  # by Denton Gentry
                           [2016, -0.961021, 34.927096, 132.135943, 111.343842, 277.445860],  # by Denton Gentry
                           [2017, -3.243445, 78.585966, 198.203915, 111.343842, 384.890277],  # by Denton Gentry
                           [2018, -7.688166, 139.708383, 264.271886, 111.343842, 507.635946],  # by Denton Gentry
                           [2019, -15.015948, 218.294349, 330.339858, 111.343842, 644.962100],  # by Denton Gentry
                           [2020, -25.947559, 314.343862, 396.407829, 111.343842, 796.147975],  # by Denton Gentry
                           [2021, -41.203762, 427.856923, 462.475801, 111.343842, 960.472804],  # by Denton Gentry
                           [2022, -61.505325, 558.833532, 528.543773, 111.343842, 1137.215822],  # by Denton Gentry
                           [2023, -87.573011, 707.273690, 594.611744, 111.343842, 1325.656265],  # by Denton Gentry
                           [2024, -120.127587, 873.177394, 660.679716, 111.343842, 1525.073365],  # by Denton Gentry
                           [2025, -159.889819, 1056.544647, 726.747687, 111.343842, 1734.746358],  # by Denton Gentry
                           [2026, -207.580471, 1257.375448, 792.815659, 111.343842, 1953.954478],  # by Denton Gentry
                           [2027, -263.920309, 1475.669797, 858.883630, 111.343842, 2181.976960],  # by Denton Gentry
                           [2028, -329.630100, 1711.427693, 924.951602, 111.343842, 2418.093038],  # by Denton Gentry
                           [2029, -405.430607, 1964.649138, 991.019574, 111.343842, 2661.581946],  # by Denton Gentry
                           [2030, -492.042598, 2235.334130, 1057.087545, 111.343842, 2911.722919],  # by Denton Gentry
                           [2031, -590.186837, 2523.482670, 1123.155517, 111.343842, 3167.795192],  # by Denton Gentry
                           [2032, -700.584089, 2829.094758, 1189.223488, 111.343842, 3429.077999],  # by Denton Gentry
                           [2033, -823.955122, 3152.170394, 1255.291460, 111.343842, 3694.850574],  # by Denton Gentry
                           [2034, -961.020699, 3492.709578, 1321.359431, 111.343842, 3964.392153],  # by Denton Gentry
                           [2035, -1112.501586, 3850.712310, 1387.427403, 111.343842, 4236.981968],  # by Denton Gentry
                           [2036, -1279.118550, 4226.178589, 1453.495375, 111.343842, 4511.899256],  # by Denton Gentry
                           [2037, -1461.592355, 4619.108417, 1519.563346, 111.343842, 4788.423250],  # by Denton Gentry
                           [2038, -1660.643768, 5029.501792, 1585.631318, 111.343842, 5065.833184],  # by Denton Gentry
                           [2039, -1876.993552, 5457.358715, 1651.699289, 111.343842, 5343.408295],  # by Denton Gentry
                           [2040, -2111.362475, 5902.679187, 1717.767261, 111.343842, 5620.427814],  # by Denton Gentry
                           [2041, -2364.471302, 6365.463206, 1783.835233, 111.343842, 5896.170978],  # by Denton Gentry
                           [2042, -2637.040798, 6845.710773, 1849.903204, 111.343842, 6169.917021],  # by Denton Gentry
                           [2043, -2929.791728, 7343.421888, 1915.971176, 111.343842, 6440.945177],  # by Denton Gentry
                           [2044, -3243.444858, 7858.596550, 1982.039147, 111.343842, 6708.534681],  # by Denton Gentry
                           [2045, -3578.720955, 8391.234761, 2048.107119, 111.343842, 6971.964767],  # by Denton Gentry
                           [2046, -3936.340782, 8941.336519, 2114.175090, 111.343842, 7230.514670],  # by Denton Gentry
                           [2047, -4317.025107, 9508.901826, 2180.243062, 111.343842, 7483.463623],  # by Denton Gentry
                           [2048, -4721.494693, 10093.930680, 2246.311034, 111.343842, 7730.090862],  # by Denton Gentry
                           [2049, -5150.470308, 10696.423082, 2312.379005, 111.343842, 7969.675622],  # by Denton Gentry
                           [2050, -5604.672715, 11316.379032, 2378.446977, 111.343842, 8201.497136],  # by Denton Gentry
                           [2051, -6084.822682, 11953.798530, 2444.514948, 111.343842, 8424.834639],  # by Denton Gentry
                           [2052, -6591.640973, 12608.681576, 2510.582920, 111.343842, 8638.967365],  # by Denton Gentry
                           [2053, -7125.848354, 13281.028170, 2576.650891, 111.343842, 8843.174549],  # by Denton Gentry
                           [2054, -7688.165590, 13970.838312, 2642.718863, 111.343842, 9036.735426],  # by Denton Gentry
                           [2055, -8279.313448, 14678.112001, 2708.786835, 111.343842, 9218.929230],  # by Denton Gentry
                           [2056, -8900.012692, 15402.849239, 2774.854806, 111.343842, 9389.035195],  # by Denton Gentry
                           [2057, -9550.984087, 16145.050024, 2840.922778, 111.343842, 9546.332556],  # by Denton Gentry
                           [2058, -10232.948401, 16904.714357, 2906.990749, 111.343842, 9690.100548],
                           # by Denton Gentry
                           [2059, -10946.626397, 17681.842238, 2973.058721, 111.343842, 9819.618404],
                           # by Denton Gentry
                           [2060, -11692.738842, 18476.433667, 3039.126692, 111.343842,
                            9934.165359]]  # by Denton Gentry
# by Denton Gentry
# SolarPVUtil 'Adoption Data'!CW50:CY96  # by Denton Gentry
exponential_trend_list = [['Year', 'coeff', 'e^x', 'adoption'],  # by Denton Gentry
                          [2014, 401.463348, 1.000000, 401.463348], [2015, 401.463348, 1.090876, 437.946633],
                          # by Denton Gentry
                          [2016, 401.463348, 1.190010, 477.745364], [2017, 401.463348, 1.298153, 521.160835],
                          # by Denton Gentry
                          [2018, 401.463348, 1.416124, 568.521719], [2019, 401.463348, 1.544815, 620.186560],
                          # by Denton Gentry
                          [2020, 401.463348, 1.685201, 676.546481], [2021, 401.463348, 1.838345, 738.028154],
                          # by Denton Gentry
                          [2022, 401.463348, 2.005406, 805.097019], [2023, 401.463348, 2.187649, 878.260819],
                          # by Denton Gentry
                          [2024, 401.463348, 2.386453, 958.073433], [2025, 401.463348, 2.603324, 1045.139080],
                          # by Denton Gentry
                          [2026, 401.463348, 2.839903, 1140.116883], [2027, 401.463348, 3.097981, 1243.725865],
                          # by Denton Gentry
                          [2028, 401.463348, 3.379512, 1356.750392], [2029, 401.463348, 3.686628, 1480.046108],
                          # by Denton Gentry
                          [2030, 401.463348, 4.021653, 1614.546416], [2031, 401.463348, 4.387124, 1761.269540],
                          # by Denton Gentry
                          [2032, 401.463348, 4.785807, 1921.326239], [2033, 401.463348, 5.220721, 2095.928212],
                          # by Denton Gentry
                          [2034, 401.463348, 5.695158, 2286.397270], [2035, 401.463348, 6.212710, 2494.175348],
                          # by Denton Gentry
                          [2036, 401.463348, 6.777295, 2720.835416], [2037, 401.463348, 7.393186, 2968.093388],
                          # by Denton Gentry
                          [2038, 401.463348, 8.065048, 3237.821116], [2039, 401.463348, 8.797965, 3532.060554],
                          # by Denton Gentry
                          [2040, 401.463348, 9.597487, 3853.039223], [2041, 401.463348, 10.469666, 4203.187071],
                          # by Denton Gentry
                          [2042, 401.463348, 11.421105, 4585.154869], [2043, 401.463348, 12.459006, 5001.834279],
                          # by Denton Gentry
                          [2044, 401.463348, 13.591228, 5456.379745], [2045, 401.463348, 14.826341, 5952.232374],
                          # by Denton Gentry
                          [2046, 401.463348, 16.173696, 6493.145984], [2047, 401.463348, 17.643492, 7083.215528],
                          # by Denton Gentry
                          [2048, 401.463348, 19.246858, 7726.908086], [2049, 401.463348, 20.995931, 8429.096691],
                          # by Denton Gentry
                          [2050, 401.463348, 22.903952, 9195.097216], [2051, 401.463348, 24.985366, 10030.708618],
                          # by Denton Gentry
                          [2052, 401.463348, 27.255930, 10942.256836], [2053, 401.463348, 29.732833, 11936.642686],
                          # by Denton Gentry
                          [2054, 401.463348, 32.434827, 13021.394101], [2055, 401.463348, 35.382366, 14204.723120],
                          # by Denton Gentry
                          [2056, 401.463348, 38.597765, 15495.588057], [2057, 401.463348, 42.105366, 16903.761320],
                          # by Denton Gentry
                          [2058, 401.463348, 45.931723, 18439.903391], [2059, 401.463348, 50.105803, 20115.643532],
                          # by Denton Gentry
                          [2060, 401.463348, 54.659206, 21943.667824]]  # by Denton Gentry
# by Denton Gentry
# ConcentratedSolar 'Adoption Data'!AB359:AD407  # by Denton Gentry
missing_data_low_med_high_list = [['Year', 'Low', 'Medium', 'High'],  # by Denton Gentry
                                  [2020, 0.00000169155508, 0.00000298340912, 0.00000427526317],  # by Denton Gentry
                                  [2021, 0.04478128413592, 0.07237104518385, 0.09996080623177],  # by Denton Gentry
                                  [2022, 0.10445700376197, 0.16878121873562, 0.23310543370926],  # by Denton Gentry
                                  [2023, 0.18118321080951, 0.29270090016902, 0.40421858952852],  # by Denton Gentry
                                  [2024, 0.27712367668104, 0.44760941678890, 0.61809515689677],  # by Denton Gentry
                                  [2025, 0.39445042261298, 0.63699641610086, 0.87954240958875],  # by Denton Gentry
                                  [2026, 0.53534359725980, 0.86436170915917, 1.19337982105854],  # by Denton Gentry
                                  [2027, 0.70199297968147, 1.13321714923445, 1.56444131878743],  # by Denton Gentry
                                  [2028, 0.89660129727754, 1.44709078142245, 1.99758026556736],  # by Denton Gentry
                                  [2029, 1.12138631248639, 1.80952944794462, 2.49767258340286],  # by Denton Gentry
                                  [2030, 1.37858039599474, 2.22409824530547, 3.06961609461620],  # by Denton Gentry
                                  [2031, 0.33841270925760, 1.17313136200367, 2.00785001474974],  # by Denton Gentry
                                  [2032, 1.36273689119353, 2.20673000642922, 3.05072312166491],  # by Denton Gentry
                                  [2033, 2.47507414376396, 3.56588822753215, 4.65670231130034],  # by Denton Gentry
                                  [2034, 3.64134920658068, 5.28571858429884, 6.93008796201700],  # by Denton Gentry
                                  [2035, 4.92719750230605, 7.40145811156219, 9.87571872081834],  # by Denton Gentry
                                  [2036, 6.38799620796120, 9.94847925423016, 13.50896230049910],  # by Denton Gentry
                                  [2037, 8.05837311905545, 12.96230699164860, 17.86624086424180],  # by Denton Gentry
                                  [2038, 9.96321045437242, 16.47862888677920, 22.99404731918600],  # by Denton Gentry
                                  [2039, 12.12327229936380, 20.53331387075860, 28.94335544215340],  # by Denton Gentry
                                  [2040, 12.57980291148420, 20.33628055766400, 28.09275820384370],  # by Denton Gentry
                                  [2041, 17.28389372718560, 30.40210359239220, 43.52031345759870],  # by Denton Gentry
                                  [2042, 20.32009533739120, 36.28874635294460, 52.25739736849810],  # by Denton Gentry
                                  [2043, 23.68355022995990, 42.85897611595470, 62.03440200194960],  # by Denton Gentry
                                  [2044, 27.39167468789690, 50.14970561311570, 72.90773653833450],  # by Denton Gentry
                                  [2045, 31.46185760793090, 58.19803276206140, 84.93420791619180],  # by Denton Gentry
                                  [2046, 35.91144956880740, 67.04114767385400, 98.17084577890060],  # by Denton Gentry
                                  [2047, 40.75773336050860, 76.71622840114180, 112.67472344177500],  # by Denton Gentry
                                  [2048, 46.01794139880320, 87.26043864692610, 128.50293589504900],  # by Denton Gentry
                                  [2049, 51.70920049342400, 98.71079867268270, 145.71239685194100],  # by Denton Gentry
                                  [2050, 58.37067713785460, 112.41832485101300, 166.46597256417100],  # by Denton Gentry
                                  [2051, 64.45323459303790, 124.47795720062600, 184.50267980821500],  # by Denton Gentry
                                  [2052, 71.54025559304320, 138.86894085152300, 206.19762611000200],  # by Denton Gentry
                                  [2053, 79.12594767781710, 154.31273531142500, 229.49952294503200],  # by Denton Gentry
                                  [2054, 87.22603599604820, 170.84371950946000, 254.46140302287100],  # by Denton Gentry
                                  [2055, 95.85608079249150, 188.49591930391900, 281.13575781534700],  # by Denton Gentry
                                  [2056, 105.03174070461000, 207.30352595713600, 309.57531120966200],
                                  # by Denton Gentry
                                  [2057, 114.76906113340800, 227.30147529533500, 339.83388945726300],
                                  # by Denton Gentry
                                  [2058, 125.08431321316100, 248.52514343704700, 371.96597366093200],
                                  # by Denton Gentry
                                  [2059, 135.99419355232700, 271.01075279436700, 406.02731203640700],
                                  # by Denton Gentry
                                  [2060, 147.51532024899800, 294.79437700559200,
                                   442.07343376218600]]  # by Denton Gentry
# by Denton Gentry
# ConcentratedSolar 'Adoption Data'!BY363:CA409  # by Denton Gentry
linear_missing_data_trend_list = [  # by Denton Gentry
    ['Year', 'x', 'constant', 'adoption'],  # by Denton Gentry
    [2014, 0.00000000000000, -99.27676466589640, -99.27676466589640],  # by Denton Gentry
    [2015, 6.44025806361785, -99.27676466589640, -92.83650660227850],  # by Denton Gentry
    [2016, 12.88051612723570, -99.27676466589640, -86.39624853866070],  # by Denton Gentry
    [2017, 19.32077419085350, -99.27676466589640, -79.95599047504280],  # by Denton Gentry
    [2018, 25.76103225447140, -99.27676466589640, -73.51573241142500],  # by Denton Gentry
    [2019, 32.20129031808920, -99.27676466589640, -67.07547434780710],  # by Denton Gentry
    [2020, 38.64154838170710, -99.27676466589640, -60.63521628418930],  # by Denton Gentry
    [2021, 45.08180644532490, -99.27676466589640, -54.19495822057140],  # by Denton Gentry
    [2022, 51.52206450894280, -99.27676466589640, -47.75470015695360],  # by Denton Gentry
    [2023, 57.96232257256060, -99.27676466589640, -41.31444209333570],  # by Denton Gentry
    [2024, 64.40258063617850, -99.27676466589640, -34.87418402971790],  # by Denton Gentry
    [2025, 70.84283869979630, -99.27676466589640, -28.43392596610000],  # by Denton Gentry
    [2026, 77.28309676341420, -99.27676466589640, -21.99366790248220],  # by Denton Gentry
    [2027, 83.72335482703200, -99.27676466589640, -15.55340983886430],  # by Denton Gentry
    [2028, 90.16361289064990, -99.27676466589640, -9.11315177524648],  # by Denton Gentry
    [2029, 96.60387095426770, -99.27676466589640, -2.67289371162863],  # by Denton Gentry
    [2030, 103.04412901788600, -99.27676466589640, 3.76736435198922],  # by Denton Gentry
    [2031, 109.48438708150300, -99.27676466589640, 10.20762241560710],  # by Denton Gentry
    [2032, 115.92464514512100, -99.27676466589640, 16.64788047922490],  # by Denton Gentry
    [2033, 122.36490320873900, -99.27676466589640, 23.08813854284280],  # by Denton Gentry
    [2034, 128.80516127235700, -99.27676466589640, 29.52839660646060],  # by Denton Gentry
    [2035, 135.24541933597500, -99.27676466589640, 35.96865467007850],  # by Denton Gentry
    [2036, 141.68567739959300, -99.27676466589640, 42.40891273369630],  # by Denton Gentry
    [2037, 148.12593546321100, -99.27676466589640, 48.84917079731420],  # by Denton Gentry
    [2038, 154.56619352682800, -99.27676466589640, 55.28942886093200],  # by Denton Gentry
    [2039, 161.00645159044600, -99.27676466589640, 61.72968692454990],  # by Denton Gentry
    [2040, 167.44670965406400, -99.27676466589640, 68.16994498816770],  # by Denton Gentry
    [2041, 173.88696771768200, -99.27676466589640, 74.61020305178550],  # by Denton Gentry
    [2042, 180.32722578130000, -99.27676466589640, 81.05046111540340],  # by Denton Gentry
    [2043, 186.76748384491800, -99.27676466589640, 87.49071917902120],  # by Denton Gentry
    [2044, 193.20774190853500, -99.27676466589640, 93.93097724263910],  # by Denton Gentry
    [2045, 199.64799997215300, -99.27676466589640, 100.37123530625700],  # by Denton Gentry
    [2046, 206.08825803577100, -99.27676466589640, 106.81149336987500],  # by Denton Gentry
    [2047, 212.52851609938900, -99.27676466589640, 113.25175143349300],  # by Denton Gentry
    [2048, 218.96877416300700, -99.27676466589640, 119.69200949711000],  # by Denton Gentry
    [2049, 225.40903222662500, -99.27676466589640, 126.13226756072800],  # by Denton Gentry
    [2050, 231.84929029024300, -99.27676466589640, 132.57252562434600],  # by Denton Gentry
    [2051, 238.28954835386000, -99.27676466589640, 139.01278368796400],  # by Denton Gentry
    [2052, 244.72980641747800, -99.27676466589640, 145.45304175158200],  # by Denton Gentry
    [2053, 251.17006448109600, -99.27676466589640, 151.89329981520000],  # by Denton Gentry
    [2054, 257.61032254471400, -99.27676466589640, 158.33355787881800],  # by Denton Gentry
    [2055, 264.05058060833200, -99.27676466589640, 164.77381594243500],  # by Denton Gentry
    [2056, 270.49083867195000, -99.27676466589640, 171.21407400605300],  # by Denton Gentry
    [2057, 276.93109673556700, -99.27676466589640, 177.65433206967100],  # by Denton Gentry
    [2058, 283.37135479918500, -99.27676466589640, 184.09459013328900],  # by Denton Gentry
    [2059, 289.81161286280300, -99.27676466589640, 190.53484819690700],  # by Denton Gentry
    [2060, 296.25187092642100, -99.27676466589640, 196.97510626052500]]  # by Denton Gentry
# by Denton Gentry
# ConcentratedSolar 'Adoption Data'!CF363:CI409  # by Denton Gentry
poly_degree2_missing_data_trend_list = [  # by Denton Gentry
    ['Year', 'x^2', 'x', 'constant', 'adoption'],  # by Denton Gentry
    [2014, 0.00000000000000, 0.00000000000000, 65.40722493576480, 65.40722493576480],  # by Denton Gentry
    [2015, 0.30724624925683, -9.53654689773733, 65.40722493576480, 56.17792428728430],  # by Denton Gentry
    [2016, 1.22898499702732, -19.07309379547470, 65.40722493576480, 47.56311613731740],  # by Denton Gentry
    [2017, 2.76521624331147, -28.60964069321200, 65.40722493576480, 39.56280048586430],  # by Denton Gentry
    [2018, 4.91593998810929, -38.14618759094930, 65.40722493576480, 32.17697733292470],  # by Denton Gentry
    [2019, 7.68115623142076, -47.68273448868670, 65.40722493576480, 25.40564667849890],  # by Denton Gentry
    [2020, 11.06086497324590, -57.21928138642400, 65.40722493576480, 19.24880852258670],  # by Denton Gentry
    [2021, 15.05506621358470, -66.75582828416130, 65.40722493576480, 13.70646286518820],  # by Denton Gentry
    [2022, 19.66375995243710, -76.29237518189870, 65.40722493576480, 8.77860970630327],  # by Denton Gentry
    [2023, 24.88694618980330, -85.82892207963600, 65.40722493576480, 4.46524904593204],  # by Denton Gentry
    [2024, 30.72462492568300, -95.36546897737330, 65.40722493576480, 0.76638088407449],  # by Denton Gentry
    [2025, 37.17679616007650, -104.90201587511100, 65.40722493576480, -2.31799477926941],  # by Denton Gentry
    [2026, 44.24345989298360, -114.43856277284800, 65.40722493576480, -4.78787794409965],  # by Denton Gentry
    [2027, 51.92461612440430, -123.97510967058500, 65.40722493576480, -6.64326861041621],  # by Denton Gentry
    [2028, 60.22026485433880, -133.51165656832300, 65.40722493576480, -7.88416677821911],  # by Denton Gentry
    [2029, 69.13040608278680, -143.04820346606000, 65.40722493576480, -8.51057244750837],  # by Denton Gentry
    [2030, 78.65503980974860, -152.58475036379700, 65.40722493576480, -8.52248561828397],  # by Denton Gentry
    [2031, 88.79416603522400, -162.12129726153500, 65.40722493576480, -7.91990629054590],  # by Denton Gentry
    [2032, 99.54778475921300, -171.65784415927200, 65.40722493576480, -6.70283446429418],  # by Denton Gentry
    [2033, 110.91589598171600, -181.19439105700900, 65.40722493576480, -4.87127013952876],  # by Denton Gentry
    [2034, 122.89849970273200, -190.73093795474700, 65.40722493576480, -2.42521331624972],  # by Denton Gentry
    [2035, 135.49559592226200, -200.26748485248400, 65.40722493576480, 0.63533600554300],  # by Denton Gentry
    [2036, 148.70718464030600, -209.80403175022100, 65.40722493576480, 4.31037782584934],  # by Denton Gentry
    [2037, 162.53326585686300, -219.34057864795900, 65.40722493576480, 8.59991214466939],  # by Denton Gentry
    [2038, 176.97383957193400, -228.87712554569600, 65.40722493576480, 13.50393896200310],  # by Denton Gentry
    [2039, 192.02890578551900, -238.41367244343300, 65.40722493576480, 19.02245827785050],  # by Denton Gentry
    [2040, 207.69846449761700, -247.95021934117100, 65.40722493576480, 25.15547009221150],  # by Denton Gentry
    [2041, 223.98251570822900, -257.48676623890800, 65.40722493576480, 31.90297440508610],  # by Denton Gentry
    [2042, 240.88105941735500, -267.02331313664500, 65.40722493576480, 39.26497121647450],  # by Denton Gentry
    [2043, 258.39409562499400, -276.55986003438300, 65.40722493576480, 47.24146052637650],  # by Denton Gentry
    [2044, 276.52162433114700, -286.09640693212000, 65.40722493576480, 55.83244233479210],  # by Denton Gentry
    [2045, 295.26364553581400, -295.63295382985700, 65.40722493576480, 65.03791664172140],  # by Denton Gentry
    [2046, 314.62015923899400, -305.16950072759500, 65.40722493576480, 74.85788344716440],  # by Denton Gentry
    [2047, 334.59116544068800, -314.70604762533200, 65.40722493576480, 85.29234275112110],  # by Denton Gentry
    [2048, 355.17666414089600, -324.24259452306900, 65.40722493576480, 96.34129455359140],  # by Denton Gentry
    [2049, 376.37665533961700, -333.77914142080700, 65.40722493576480, 108.00473885457500],  # by Denton Gentry
    [2050, 398.19113903685200, -343.31568831854400, 65.40722493576480, 120.28267565407300],  # by Denton Gentry
    [2051, 420.62011523260100, -352.85223521628100, 65.40722493576480, 133.17510495208400],  # by Denton Gentry
    [2052, 443.66358392686300, -362.38878211401900, 65.40722493576480, 146.68202674860900],  # by Denton Gentry
    [2053, 467.32154511963900, -371.92532901175600, 65.40722493576480, 160.80344104364800],  # by Denton Gentry
    [2054, 491.59399881092900, -381.46187590949300, 65.40722493576480, 175.53934783720000],  # by Denton Gentry
    [2055, 516.48094500073200, -390.99842280723100, 65.40722493576480, 190.88974712926600],  # by Denton Gentry
    [2056, 541.98238368904900, -400.53496970496800, 65.40722493576480, 206.85463891984600],  # by Denton Gentry
    [2057, 568.09831487587900, -410.07151660270500, 65.40722493576480, 223.43402320893900],  # by Denton Gentry
    [2058, 594.82873856122400, -419.60806350044300, 65.40722493576480, 240.62789999654600],  # by Denton Gentry
    [2059, 622.17365474508200, -429.14461039818000, 65.40722493576480, 258.43626928266600],  # by Denton Gentry
    [2060, 650.13306342745300, -438.68115729591700, 65.40722493576480, 276.85913106730000]]  # by Denton Gentry
# by Denton Gentry
# ConcentratedSolar 'Adoption Data'!CN363:CR409  # by Denton Gentry
poly_degree3_missing_data_trend_list = [  # by Denton Gentry
    ['Year', 'x^3', 'x^2', 'x', 'constant', 'adoption'],  # by Denton Gentry
    [2014, 0, 0, 0, -3.395412507, -3.395412507],  # by Denton Gentry
    [2015, 0.006238226, -0.179335345, 1.543789357, -3.395412507, -2.024720269],  # by Denton Gentry
    [2016, 0.049905805, -0.71734138, 3.087578715, -3.395412507, -0.975269368],  # by Denton Gentry
    [2017, 0.16843209, -1.614018106, 4.631368072, -3.395412507, -0.20963045],  # by Denton Gentry
    [2018, 0.399246436, -2.869365522, 6.17515743, -3.395412507, 0.309625838],  # by Denton Gentry
    [2019, 0.779778196, -4.483383628, 7.718946787, -3.395412507, 0.619928849],  # by Denton Gentry
    [2020, 1.347456723, -6.456072424, 9.262736144, -3.395412507, 0.758707937],  # by Denton Gentry
    [2021, 2.13971137, -8.78743191, 10.8065255, -3.395412507, 0.763392455],  # by Denton Gentry
    [2022, 3.193971491, -11.47746209, 12.35031486, -3.395412507, 0.671411757],  # by Denton Gentry
    [2023, 4.54766644, -14.52616295, 13.89410422, -3.395412507, 0.520195196],  # by Denton Gentry
    [2024, 6.238225569, -17.93353451, 15.43789357, -3.395412507, 0.347172126],  # by Denton Gentry
    [2025, 8.303078232, -21.69957676, 16.98168293, -3.395412507, 0.189771899],  # by Denton Gentry
    [2026, 10.77965378, -25.82428969, 18.52547229, -3.395412507, 0.08542387],  # by Denton Gentry
    [2027, 13.70538157, -30.30767332, 20.06926165, -3.395412507, 0.071557392],  # by Denton Gentry
    [2028, 17.11769096, -35.14972764, 21.613051, -3.395412507, 0.185601817],  # by Denton Gentry
    [2029, 21.05401129, -40.35045265, 23.15684036, -3.395412507, 0.464986501],  # by Denton Gentry
    [2030, 25.55177193, -45.90984835, 24.70062972, -3.395412507, 0.947140795],  # by Denton Gentry
    [2031, 30.64840222, -51.82791473, 26.24441908, -3.395412507, 1.669494054],  # by Denton Gentry
    [2032, 36.38133152, -58.10465181, 27.78820843, -3.395412507, 2.66947563],  # by Denton Gentry
    [2033, 42.78798918, -64.74005958, 29.33199779, -3.395412507, 3.984514878],  # by Denton Gentry
    [2034, 49.90580455, -71.73413804, 30.87578715, -3.395412507, 5.65204115],  # by Denton Gentry
    [2035, 57.77220699, -79.08688719, 32.41957651, -3.395412507, 7.7094838],  # by Denton Gentry
    [2036, 66.42462586, -86.79830703, 33.96336586, -3.395412507, 10.19427218],  # by Denton Gentry
    [2037, 75.90049049, -94.86839756, 35.50715522, -3.395412507, 13.14383565],  # by Denton Gentry
    [2038, 86.23723026, -103.2971588, 37.05094458, -3.395412507, 16.59560355],  # by Denton Gentry
    [2039, 97.47227451, -112.0845907, 38.59473393, -3.395412507, 20.58700525],  # by Denton Gentry
    [2040, 109.6430526, -121.2306933, 40.13852329, -3.395412507, 25.15547009],  # by Denton Gentry
    [2041, 122.7869939, -130.7354666, 41.68231265, -3.395412507, 30.33842743],  # by Denton Gentry
    [2042, 136.9415277, -140.5989106, 43.22610201, -3.395412507, 36.17330662],  # by Denton Gentry
    [2043, 152.1440834, -150.8210252, 44.76989136, -3.395412507, 42.69753702],  # by Denton Gentry
    [2044, 168.4320904, -161.4018106, 46.31368072, -3.395412507, 49.94854798],  # by Denton Gentry
    [2045, 185.8429779, -172.3412666, 47.85747008, -3.395412507, 57.96376885],  # by Denton Gentry
    [2046, 204.4141754, -183.6393934, 49.40125944, -3.395412507, 66.78062898],  # by Denton Gentry
    [2047, 224.1831123, -195.2961908, 50.94504879, -3.395412507, 76.43655773],  # by Denton Gentry
    [2048, 245.1872178, -207.3116589, 52.48883815, -3.395412507, 86.96898446],  # by Denton Gentry
    [2049, 267.4639213, -219.6857978, 54.03262751, -3.395412507, 98.41533851],  # by Denton Gentry
    [2050, 291.0506521, -232.4186073, 55.57641687, -3.395412507, 110.8130492],  # by Denton Gentry
    [2051, 315.9848397, -245.5100874, 57.12020622, -3.395412507, 124.199546],  # by Denton Gentry
    [2052, 342.3039134, -258.9602383, 58.66399558, -3.395412507, 138.6122582],  # by Denton Gentry
    [2053, 370.0453025, -272.7690599, 60.20778494, -3.395412507, 154.088615],  # by Denton Gentry
    [2054, 399.2464364, -286.9365522, 61.7515743, -3.395412507, 170.666046],  # by Denton Gentry
    [2055, 429.9447444, -301.4627151, 63.29536365, -3.395412507, 188.3819805],  # by Denton Gentry
    [2056, 462.1776559, -316.3475488, 64.83915301, -3.395412507, 207.2738477],  # by Denton Gentry
    [2057, 495.9826003, -331.5910531, 66.38294237, -3.395412507, 227.3790771],  # by Denton Gentry
    [2058, 531.3970068, -347.1932281, 67.92673173, -3.395412507, 248.7350979],  # by Denton Gentry
    [2059, 568.4583049, -363.1540738, 69.47052108, -3.395412507, 271.3793397],  # by Denton Gentry
    [2060, 607.203924, -379.4735902, 71.01431044, -3.395412507, 295.3492317]]  # by Denton Gentry
# by Denton Gentry
# ConcentratedSolar 'Adoption Data'!CN363:CR409  # by Denton Gentry
exponential_missing_data_trend_list = [  # by Denton Gentry
    ['Year', 'coeff', 'e^x', 'adoption'],  # by Denton Gentry
    [2014, 0.02177042693422, 1.00000000000000, 0.02177042693422],  # by Denton Gentry
    [2015, 0.02177042693422, 1.26720492422913, 0.02758759221361],  # by Denton Gentry
    [2016, 0.02177042693422, 1.60580831999055, 0.03495913270071],  # by Denton Gentry
    [2017, 0.02177042693422, 2.03488821046013, 0.04430038510512],  # by Denton Gentry
    [2018, 0.02177042693422, 2.57862036055087, 0.05613766615046],  # by Denton Gentry
    [2019, 0.02177042693422, 3.26764041860755, 0.07113792698059],  # by Denton Gentry
    [2020, 0.02177042693422, 4.14077002906961, 0.09014633136926],  # by Denton Gentry
    [2021, 0.02177042693422, 5.24720417093740, 0.11423387501232],  # by Denton Gentry
    [2022, 0.02177042693422, 6.64928296384749, 0.14475772892938],  # by Denton Gentry
    [2023, 0.02177042693422, 8.42600411438038, 0.18343770691954],  # by Denton Gentry
    [2024, 0.02177042693422, 10.67747390531770, 0.23245316549774],  # by Denton Gentry
    [2025, 0.02177042693422, 13.53054751114660, 0.29456579597138],  # by Denton Gentry
    [2026, 0.02177042693422, 17.14597643364110, 0.37327522716441],  # by Denton Gentry
    [2027, 0.02177042693422, 21.72746576742660, 0.47301620595548],  # by Denton Gentry
    [2028, 0.02177042693422, 27.53315161150280, 0.59940846542697],  # by Denton Gentry
    [2029, 0.02177042693422, 34.89014530164350, 0.75957335901368],  # by Denton Gentry
    [2030, 0.02177042693422, 44.21296393331240, 0.96253510085539],  # by Denton Gentry
    [2031, 0.02177042693422, 56.02688561105830, 1.21972921954733],  # by Denton Gentry
    [2032, 0.02177042693422, 70.99754533555510, 1.54564687323653],  # by Denton Gentry
    [2033, 0.02177042693422, 89.96843905739610, 1.95865132888469],  # by Denton Gentry
    [2034, 0.02177042693422, 114.00844899874100, 2.48201260881060],  # by Denton Gentry
    [2035, 0.02177042693422, 144.47206797492900, 3.14521859988357],  # by Denton Gentry
    [2036, 0.02177042693422, 183.07571595139600, 3.98563649754951],  # by Denton Gentry
    [2037, 0.02177042693422, 231.99444876038200, 5.05061819588207],  # by Denton Gentry
    [2038, 0.02177042693422, 293.98450786297800, 6.40016824822299],  # by Denton Gentry
    [2039, 0.02177042693422, 372.53861601104200, 8.11032472004307],  # by Denton Gentry
    [2040, 0.02177042693422, 472.08276867469600, 10.27744342233580],  # by Denton Gentry
    [2041, 0.02177042693422, 598.22560910829500, 13.02362691327020],  # by Denton Gentry
    [2042, 0.02177042693422, 758.07443766200000, 16.50360415581900],  # by Denton Gentry
    [2043, 0.02177042693422, 960.63566033751400, 20.91344845378210],  # by Denton Gentry
    [2044, 0.02177042693422, 1217.32223916980000, 26.50162486324470],  # by Denton Gentry
    [2045, 0.02177042693422, 1542.59673584959000, 33.58298952677670],  # by Denton Gentry
    [2046, 0.02177042693422, 1954.78617976838000, 42.55652969866670],  # by Denton Gentry
    [2047, 0.02177042693422, 2477.11467281754000, 53.92784399225350],  # by Denton Gentry
    [2048, 0.02177042693422, 3139.01191127461000, 68.33762946004390],  # by Denton Gentry
    [2049, 0.02177042693422, 3977.77135118107000, 86.59778056191310],  # by Denton Gentry
    [2050, 0.02177042693422, 5040.65144367420000, 109.73713395537000],  # by Denton Gentry
    [2051, 0.02177042693422, 6387.53833074661000, 139.05943651903600],  # by Denton Gentry
    [2052, 0.02177042693422, 8094.32002642440000, 176.21680271745000],  # by Denton Gentry
    [2053, 0.02177042693422, 10257.16219577140000, 223.30280013546500],  # by Denton Gentry
    [2054, 0.02177042693422, 12997.92644309840000, 282.97040792581400],  # by Denton Gentry
    [2055, 0.02177042693422, 16471.03639346230000, 358.58149433471600],  # by Denton Gentry
    [2056, 0.02177042693422, 20872.17842495260000, 454.39623535839200],  # by Denton Gentry
    [2057, 0.02177042693422, 26449.32727948890000, 575.81314699733100],  # by Denton Gentry
    [2058, 0.02177042693422, 33516.71777111610000, 729.67325531088900],  # by Denton Gentry
    [2059, 0.02177042693422, 42472.54980355620000, 924.64554220825600],  # by Denton Gentry
    [2060, 0.02177042693422, 53821.42425563330000, 1171.71538425281000]]  # by Denton Gentry
# by Denton Gentry
# Water Efficiency 'TAM Data'!V544:Y592  # by Denton Gentry
tam_low_med_high_NaN_years_list = [['Year', 'Low', 'Medium', 'High'],  # by Denton Gentry
                                   [2012, np.nan, np.nan, np.nan],  # by Denton Gentry
                                   [2013, np.nan, np.nan, np.nan],  # by Denton Gentry
                                   [2014, np.nan, 0.0000, np.nan],  # by Denton Gentry
                                   [2015, np.nan, 0.0000, np.nan],  # by Denton Gentry
                                   [2016, np.nan, 0.0000, np.nan],  # by Denton Gentry
                                   [2017, np.nan, 0.0000, np.nan],  # by Denton Gentry
                                   [2018, np.nan, 0.0000, np.nan],  # by Denton Gentry
                                   [2019, np.nan, 0.0000, np.nan],  # by Denton Gentry
                                   [2020, np.nan, 0.0000, np.nan],  # by Denton Gentry
                                   [2021, np.nan, 0.0000, np.nan],  # by Denton Gentry
                                   [2022, 527.005506578651, 527.005506578651, 527.005506578651],  # by Denton Gentry
                                   [2023, 2206.146176138490, 2206.146176138490, 2206.146176138490],  # by Denton Gentry
                                   [2024, 3860.878664535700, 3860.878664535700, 3860.878664535700],  # by Denton Gentry
                                   [2025, 5494.272691053110, 5494.272691053110, 5494.272691053110],  # by Denton Gentry
                                   [2026, 7109.369248402820, 7109.369248402820, 7109.369248402820],  # by Denton Gentry
                                   [2027, 8709.586220284300, 8709.586220284300, 8709.586220284300],  # by Denton Gentry
                                   [2028, 10298.514118037400, 10298.514118037400, 10298.514118037400],
                                   # by Denton Gentry
                                   [2029, 11879.474582086000, 11879.474582086000, 11879.474582086000],
                                   # by Denton Gentry
                                   [2030, 13379.959345877900, 13379.959345877900, 13379.959345877900],
                                   # by Denton Gentry
                                   [2031, 15026.450316684300, 15026.450316684300, 15026.450316684300],
                                   # by Denton Gentry
                                   [2032, 16595.143221848300, 16595.143221848300, 16595.143221848300],
                                   # by Denton Gentry
                                   [2033, 18162.014767014800, 18162.014767014800, 18162.014767014800],
                                   # by Denton Gentry
                                   [2034, 19727.971156309500, 19727.971156309500, 19727.971156309500],
                                   # by Denton Gentry
                                   [2035, 21294.014417168400, 21294.014417168400, 21294.014417168400],
                                   # by Denton Gentry
                                   [2036, 22861.361849738500, 22861.361849738500, 22861.361849738500],
                                   # by Denton Gentry
                                   [2037, 24431.127313168400, 24431.127313168400, 24431.127313168400],
                                   # by Denton Gentry
                                   [2038, 26004.226783509800, 26004.226783509800, 26004.226783509800],
                                   # by Denton Gentry
                                   [2039, 27581.630576118700, 27581.630576118700, 27581.630576118700],
                                   # by Denton Gentry
                                   [2040, 29239.641793475600, 29239.641793475600, 29239.641793475600],
                                   # by Denton Gentry
                                   [2041, 30753.920850767900, 30753.920850767900, 30753.920850767900],
                                   # by Denton Gentry
                                   [2042, 32351.217690602400, 32351.217690602400, 32351.217690602400],
                                   # by Denton Gentry
                                   [2043, 33957.462513951600, 33957.462513951600, 33957.462513951600],
                                   # by Denton Gentry
                                   [2044, 35573.713191003300, 35573.713191003300, 35573.713191003300],
                                   # by Denton Gentry
                                   [2045, 37200.959924663400, 37200.959924663400, 37200.959924663400],
                                   # by Denton Gentry
                                   [2046, 38840.134042465900, 38840.134042465900, 38840.134042465900],
                                   # by Denton Gentry
                                   [2047, 40492.098630960000, 40492.098630960000, 40492.098630960000],
                                   # by Denton Gentry
                                   [2048, 42157.613380147800, 42157.613380147800, 42157.613380147800],
                                   # by Denton Gentry
                                   [2049, 43837.328930809300, 43837.328930809300, 43837.328930809300],
                                   # by Denton Gentry
                                   [2050, 45491.865604233100, 45491.865604233100, 45491.865604233100],
                                   # by Denton Gentry
                                   [2051, 47241.616398066800, 47241.616398066800, 47241.616398066800],
                                   # by Denton Gentry
                                   [2052, 48967.233516912400, 48967.233516912400, 48967.233516912400],
                                   # by Denton Gentry
                                   [2053, 50708.982693585700, 50708.982693585700, 50708.982693585700],
                                   # by Denton Gentry
                                   [2054, 52467.060565405600, 52467.060565405600, 52467.060565405600],
                                   # by Denton Gentry
                                   [2055, 54241.635211057100, 54241.635211057100, 54241.635211057100],
                                   # by Denton Gentry
                                   [2056, 56032.940257134400, 56032.940257134400, 56032.940257134400],
                                   # by Denton Gentry
                                   [2057, 57841.257211548100, 57841.257211548100, 57841.257211548100],
                                   # by Denton Gentry
                                   [2058, 59666.823542820500, 59666.823542820500, 59666.823542820500],
                                   # by Denton Gentry
                                   [2059, 61509.891884951900, 61509.891884951900, 61509.891884951900],
                                   # by Denton Gentry
                                   [2060, 63379.458443301200, 63379.458443301200,
                                    63379.458443301200]]  # by Denton Gentry
# by Denton Gentry
# Water Efficiency 'TAM Data'!BT544:BV592  # by Denton Gentry
linear_with_NaN_trend_list = [['Year', 'x', 'constant', 'adoption'],  # by Denton Gentry
                              [2014, 0.000000000000, -8488.781557825990, -8488.781557825990],  # by Denton Gentry
                              [2015, 1494.981254810580, -8488.781557825990, -6993.800303015400],  # by Denton Gentry
                              [2016, 2989.962509621170, -8488.781557825990, -5498.819048204820],  # by Denton Gentry
                              [2017, 4484.943764431750, -8488.781557825990, -4003.837793394240],  # by Denton Gentry
                              [2018, 5979.925019242330, -8488.781557825990, -2508.856538583650],  # by Denton Gentry
                              [2019, 7474.906274052920, -8488.781557825990, -1013.875283773070],  # by Denton Gentry
                              [2020, 8969.887528863500, -8488.781557825990, 481.105971037512],  # by Denton Gentry
                              [2021, 10464.868783674100, -8488.781557825990, 1976.087225848090],  # by Denton Gentry
                              [2022, 11959.850038484700, -8488.781557825990, 3471.068480658680],  # by Denton Gentry
                              [2023, 13454.831293295200, -8488.781557825990, 4966.049735469260],  # by Denton Gentry
                              [2024, 14949.812548105800, -8488.781557825990, 6461.030990279840],  # by Denton Gentry
                              [2025, 16444.793802916400, -8488.781557825990, 7956.012245090430],  # by Denton Gentry
                              [2026, 17939.775057727000, -8488.781557825990, 9450.993499901010],  # by Denton Gentry
                              [2027, 19434.756312537600, -8488.781557825990, 10945.974754711600],  # by Denton Gentry
                              [2028, 20929.737567348200, -8488.781557825990, 12440.956009522200],  # by Denton Gentry
                              [2029, 22424.718822158700, -8488.781557825990, 13935.937264332800],  # by Denton Gentry
                              [2030, 23919.700076969300, -8488.781557825990, 15430.918519143300],  # by Denton Gentry
                              [2031, 25414.681331779900, -8488.781557825990, 16925.899773953900],  # by Denton Gentry
                              [2032, 26909.662586590500, -8488.781557825990, 18420.881028764500],  # by Denton Gentry
                              [2033, 28404.643841401100, -8488.781557825990, 19915.862283575100],  # by Denton Gentry
                              [2034, 29899.625096211700, -8488.781557825990, 21410.843538385700],  # by Denton Gentry
                              [2035, 31394.606351022200, -8488.781557825990, 22905.824793196300],  # by Denton Gentry
                              [2036, 32889.587605832800, -8488.781557825990, 24400.806048006800],  # by Denton Gentry
                              [2037, 34384.568860643400, -8488.781557825990, 25895.787302817400],  # by Denton Gentry
                              [2038, 35879.550115454000, -8488.781557825990, 27390.768557628000],  # by Denton Gentry
                              [2039, 37374.531370264600, -8488.781557825990, 28885.749812438600],  # by Denton Gentry
                              [2040, 38869.512625075200, -8488.781557825990, 30380.731067249200],  # by Denton Gentry
                              [2041, 40364.493879885700, -8488.781557825990, 31875.712322059800],  # by Denton Gentry
                              [2042, 41859.475134696300, -8488.781557825990, 33370.693576870300],  # by Denton Gentry
                              [2043, 43354.456389506900, -8488.781557825990, 34865.674831680900],  # by Denton Gentry
                              [2044, 44849.437644317500, -8488.781557825990, 36360.656086491500],  # by Denton Gentry
                              [2045, 46344.418899128100, -8488.781557825990, 37855.637341302100],  # by Denton Gentry
                              [2046, 47839.400153938700, -8488.781557825990, 39350.618596112700],  # by Denton Gentry
                              [2047, 49334.381408749200, -8488.781557825990, 40845.599850923300],  # by Denton Gentry
                              [2048, 50829.362663559800, -8488.781557825990, 42340.581105733800],  # by Denton Gentry
                              [2049, 52324.343918370400, -8488.781557825990, 43835.562360544400],  # by Denton Gentry
                              [2050, 53819.325173181000, -8488.781557825990, 45330.543615355000],  # by Denton Gentry
                              [2051, 55314.306427991600, -8488.781557825990, 46825.524870165600],  # by Denton Gentry
                              [2052, 56809.287682802200, -8488.781557825990, 48320.506124976200],  # by Denton Gentry
                              [2053, 58304.268937612700, -8488.781557825990, 49815.487379786700],  # by Denton Gentry
                              [2054, 59799.250192423300, -8488.781557825990, 51310.468634597300],  # by Denton Gentry
                              [2055, 61294.231447233900, -8488.781557825990, 52805.449889407900],  # by Denton Gentry
                              [2056, 62789.212702044500, -8488.781557825990, 54300.431144218500],  # by Denton Gentry
                              [2057, 64284.193956855100, -8488.781557825990, 55795.412399029100],  # by Denton Gentry
                              [2058, 65779.175211665700, -8488.781557825990, 57290.393653839700],  # by Denton Gentry
                              [2059, 67274.156466476200, -8488.781557825990, 58785.374908650300],  # by Denton Gentry
                              [2060, 68769.137721286800, -8488.781557825990, 60280.356163460800]]  # by Denton Gentry
