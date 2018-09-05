from echopype import unpack_ek60

from os import path

def data_file(filename):
    return path.abspath(path.join(path.dirname(__file__),'..','data',filename))

# OOI CE04OSPS EK60
# def test_ooi_ek60_unpack():
#     first_ping_metadata, data_times, power_data_dict, angle_data_dict, motion_data_dict, config_header, config_transducer = \
#         unpack_ek60.load_ek60_raw(data_file('OOI-D20170821-T000000.raw'))

# OceanStarr 2 channel EK60
# first_ping_metadata, data_times, power_data_dict, frequencies, bin_size, config_header, config_transducer = \
#     unpack_ek60.load_ek60_raw('data_zplsc/OceanStarr_2017-D20170725-T004612.raw')

# Dyson 5 channel EK60
# first_ping_metadata, data_times, power_data_dict, angle_data_dict, motion_data_dict, config_header, config_transducer = \
#     unpack_ek60.load_ek60_raw('data_zplsc/DY1801_EK60-D20180211-T164025.raw')

# EK80
# first_ping_metadata, data_times, power_data_dict, frequencies, bin_size, config_header, config_transducer = \
#     unpack_ek60.load_ek60_raw('data_zplsc/D20180206-T000625.raw')


def test_dyson_5channel_ek60_unpack():
    first_ping_metadata, data_times, power_data_dict, angle_data_dict, motion_data_dict, config_header, config_transducer = \
        unpack_ek60.load_ek60_raw(data_file('DY1801_EK60-D20180211-T164025.raw'))
