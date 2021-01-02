"""Health & Education solution model for Paper Cluster
   Excel filename: CORE_PopulationChange_29Jan2020 (version 1.5).xlsx
   Excel sheet name: Paper_cluster
"""
import pathlib
import numpy as np
import pandas as pd
import sys
__file__ = 'c:\\Users\\sunishchal.dev\\Documents\\solutions\\solution\\health_and_education\\clusters'
repo_path = str(pathlib.Path(__file__).parents[2])
sys.path.append(repo_path)
# sys.path.append('c:\\Users\\sunishchal.dev\\Documents\\solutions')

from model import advanced_controls as ac
from solution.health_and_education.clusters import cluster_model

DATADIR = pathlib.Path(__file__).parents[0].joinpath('data')
THISDIR = pathlib.Path(__file__).parents[0]

name = 'Health and Education - Paper Cluster'
solution_category = ac.SOLUTION_CATEGORY.REDUCTION 
period_start = 2020
period_end = 2050

# % impact of educational attainment on uptake of Family Planning:
assumptions = {
    'fixed_weighting_factor': None,
    'pct_impact': 0.50,
    'use_fixed_weight': 'N',
    'Direct Emissions': 1318973.961,
    'Indirect Emissions': 524550.5,
    'period_start': 2020,
    'period_end': 2050,
    'Grid': 'N',
    'Fuel': 'N',
    'Other Direct': 'Y',
    'Indirect': 'Y'
}

# TABLE 1: Current TAM Mix
current_tam_mix_list = [
        ['Energy Source', 'Weighting Factor', 'Include in SOL?', 'Include in CONV?'],
        ['Virgin Paper', 44.0, 'N', 'Y']]

# Table 2: REF2, Paper Demand TAM (TWh Therms)										
# WaterHeating_cluster!B28:K75
# TODO: Replace this with solarpvutil.Scenario.ref_tam_per_region once we resolve the data mismatch
ref2_tam_list = [
        ['World', 'OECD90', 'Eastern Europe', 'Asia (Sans Japan)', 'Middle East and Africa', 'Latin America', 'China', 'India', 'EU', 'USA'],
        [432.403664, 242.716674, 22.577752, 138.887882, 9.755026, 23.089264, 110.778571, 10.247000, 92.507389, 75.239768],
        [440.592298, 248.917271, 23.960729, 144.985455, 10.190211, 23.707307, 113.197545, 10.734412, 93.239345, 74.086896],
        [448.865022, 255.307923, 24.931198, 151.805693, 10.585601, 24.327959, 121.559636, 11.495328, 93.696571, 73.532245],
        [457.497906, 261.824829, 25.872882, 158.655475, 10.988170, 24.961113, 129.962601, 12.265347, 94.135585, 72.990815],
        [466.488656, 268.471125, 26.787807, 165.541254, 11.398145, 25.607156, 138.410661, 13.050637, 94.557354, 72.462605],
        [475.834975, 275.249948, 27.677999, 172.469483, 11.815755, 26.266473, 146.908035, 13.857367, 94.962847, 71.947615],
        [485.534570, 282.164433, 28.545484, 179.446614, 12.241225, 26.939451, 155.458945, 14.691704, 95.353031, 71.445845],
        [495.585143, 289.217715, 29.392287, 186.479101, 12.674784, 27.626475, 164.067609, 15.559816, 95.728875, 70.957296],
        [505.984400, 296.412932, 30.220434, 193.573396, 13.116658, 28.327932, 172.738248, 16.467872, 96.091346, 70.481967],
        [516.730046, 303.753218, 31.031952, 200.735951, 13.567074, 29.044208, 181.475083, 17.422039, 96.441413, 70.019858],
        [527.819784, 311.241709, 31.828865, 207.973221, 14.026259, 29.775688, 190.282334, 18.428485, 96.780043, 69.570969],
        [539.251320, 318.881542, 32.613200, 215.291657, 14.494440, 30.522758, 199.164220, 19.493379, 97.108205, 69.135301],
        [551.022357, 326.675853, 33.386983, 222.697712, 14.971846, 31.285806, 208.124962, 20.622889, 97.426867, 68.712852],
        [563.130602, 334.627776, 34.152240, 230.197839, 15.458702, 32.065216, 217.168781, 21.823181, 97.736997, 68.303625],
        [575.573757, 342.740449, 34.910995, 237.798491, 15.955235, 32.861374, 226.299896, 23.100425, 98.039562, 67.907617],
        [588.349528, 351.017006, 35.665276, 245.506121, 16.461674, 33.674668, 235.522527, 24.460789, 98.335531, 67.524829],
        [601.455620, 359.460585, 36.417108, 253.327182, 16.978245, 34.505482, 244.840896, 25.910440, 98.625871, 67.155262],
        [614.889736, 368.074320, 37.168516, 261.268125, 17.505175, 35.354203, 254.259221, 27.455546, 98.911552, 66.798915],
        [628.649582, 376.861347, 37.921528, 269.335405, 18.042691, 36.221216, 263.781724, 29.102276, 99.193540, 66.455789],
        [642.732861, 385.824803, 38.678168, 277.535474, 18.591020, 37.106909, 273.412624, 30.856798, 99.472805, 66.125882],
        [657.137279, 394.967824, 39.440462, 285.874784, 19.150390, 38.011666, 283.156142, 32.725278, 99.750313, 65.809196],
        [671.860541, 404.293544, 40.210436, 294.359788, 19.721028, 38.935875, 293.016498, 34.713887, 100.027033, 65.505730],
        [686.900350, 413.805101, 40.990116, 302.996940, 20.303160, 39.879920, 302.997911, 36.828790, 100.303933, 65.215484],
        [702.254412, 423.505629, 41.781528, 311.792692, 20.897014, 40.844188, 313.104603, 39.076158, 100.581981, 64.938459],
        [717.920430, 433.398266, 42.586698, 320.753497, 21.502817, 41.829065, 323.340794, 41.462156, 100.862146, 64.674653],
        [733.896110, 443.486146, 43.407652, 329.885808, 22.120796, 42.834937, 333.710703, 43.992955, 101.145394, 64.424068],
        [750.179155, 453.772405, 44.246414, 339.196077, 22.751178, 43.862189, 344.218550, 46.674720, 101.432694, 64.186704],
        [766.767272, 464.260180, 45.105012, 348.690757, 23.394190, 44.911209, 354.868557, 49.513622, 101.725015, 63.962559],
        [783.658163, 474.952607, 45.985471, 358.376301, 24.050060, 45.982382, 365.664943, 52.515827, 102.023323, 63.751635],
        [800.849534, 485.852820, 46.889817, 368.259162, 24.719014, 47.076094, 376.611929, 55.687503, 102.328588, 63.553931],
        [818.339090, 496.963956, 47.820076, 378.345792, 25.401280, 48.192731, 387.713734, 59.034819, 102.641777, 63.369447],
        [836.124534, 508.289152, 48.778273, 388.642645, 26.097085, 49.332679, 398.974579, 62.563943, 102.963859, 63.198183],
        [854.203572, 519.831542, 49.766434, 399.156173, 26.806655, 50.496325, 410.398684, 66.281042, 103.295800, 63.040140],
        [872.573908, 531.594263, 50.786586, 409.892829, 27.530218, 51.684053, 421.990269, 70.192284, 103.638570, 62.895317],
        [891.233246, 543.580450, 51.840754, 420.859066, 28.268001, 52.896251, 433.753555, 74.303839, 103.993136, 62.763714],
        [910.179292, 555.793240, 52.930963, 432.061337, 29.020232, 54.133303, 445.692762, 78.621873, 104.360467, 62.645332],
        [929.409749, 568.235768, 54.059240, 443.506093, 29.787136, 55.395597, 457.812109, 83.152554, 104.741530, 62.540169],
        [948.922322, 580.911171, 55.227611, 455.199789, 30.568942, 56.683518, 470.115817, 87.902051, 105.137294, 62.448227],
        [968.714717, 593.822583, 56.438102, 467.148877, 31.365877, 57.997453, 482.608107, 92.876532, 105.548726, 62.369505],
        [988.784637, 606.973141, 57.692737, 479.359810, 32.178167, 59.337787, 495.293198, 98.082164, 105.976794, 62.304004],
        [1009.129787, 620.365981, 58.993544, 491.839040, 33.006040, 60.704906, 508.175310, 103.525116, 106.422467, 62.251722],
        [1029.747871, 634.004239, 60.342547, 504.593021, 33.849722, 62.099196, 521.258665, 109.211556, 106.886713, 62.212661],
        [1050.636595, 647.891050, 61.741774, 517.628205, 34.709442, 63.521044, 534.547481, 115.147651, 107.370499, 62.186820],
        [1071.793662, 662.029551, 63.193248, 530.951044, 35.585426, 64.970835, 548.045980, 121.339570, 107.874794, 62.174200],
        [1093.216778, 676.422877, 64.698998, 544.567993, 36.477900, 66.448955, 561.758381, 127.793481, 108.400566, 62.174799],
        [1114.903646, 691.074164, 66.261047, 558.485503, 37.387093, 67.955791, 575.688905, 134.515551, 108.948782, 62.188619],
        [1136.851972, 705.986548, 67.881423, 572.710027, 38.313232, 69.491729, 589.841772, 141.511950, 109.520411, 62.215659]]


class Cluster:

    def __init__(self):
        self.name = name

    def run_cluster(self):
        scenario = cluster_model.Scenario(name, assumptions)
        scenario.load_pop_data(DATADIR)
        scenario.load_tam_mix(current_tam_mix_list)
        scenario.load_ref2_tam(ref2_tam_list)
        scenario.calc_ref1_tam()
        scenario.calc_ref2_demand()
        scenario.calc_ref1_demand()
        scenario.calc_change_demand()
        scenario.calc_addl_units_highed()
        scenario.calc_addl_units_lowed()
        scenario.calc_emis_diff_highed_paper()
        scenario.calc_emis_diff_lowed_paper()
        scenario.calc_emis_alloc_lldc()
        scenario.calc_addl_units_mdc()
        scenario.calc_emis_diff_mdc_paper()
        scenario.calc_emis_alloc_mdc()
        scenario.calc_total_emis()
        scenario.print_total_emis()
        return scenario
        
if __name__ == "__main__":
    cluster = Cluster()
    cluster.run_cluster()