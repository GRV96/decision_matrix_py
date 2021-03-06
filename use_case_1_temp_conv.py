# -*- coding: utf-8 -*-

from decision_matrix import DecisionMatrix

def convert_c_to_f(temperature):
    print("Converting °C to °F")
    return temperature * 9 / 5 + 32

def convert_c_to_k(temperature):
    print("Converting °C to K")
    return temperature + 273.15

def convert_f_to_c(temperature):
    print("Converting °F to °C")
    return (temperature - 32) * 5 / 9

def convert_f_to_k(temperature):
    print("Converting °F to K")
    return (temperature + 459.67) * 5 / 9

def convert_k_to_c(temperature):
    print("Converting K to °C")
    return temperature - 273.15

def convert_k_to_f(temperature):
    print("Converting K to °F")
    return temperature * 9 / 5 - 459.67

def do_not_convert(temperature):
    print("Not converting")
    return temperature

def perform_conversion(conv_fnc):
    print(conv_fnc(input_temp))

input_temp = 23

DEG_C = "C"
DEG_F = "F"
KELVIN = "K"

input_scale = "f"
output_scale = "c"

input_scale_axis = [
    lambda: input_scale.upper() == DEG_C,
    lambda: input_scale.upper() == DEG_F,
    lambda: input_scale.upper() == KELVIN]
output_scale_axis = [
    lambda: output_scale.upper() == DEG_C,
    lambda: output_scale.upper() == DEG_F,
    lambda: output_scale.upper() == KELVIN]

dm = DecisionMatrix(input_scale_axis, output_scale_axis)
dm.set_all_actions({(0, 0): lambda: perform_conversion(do_not_convert),
                    (0, 1): lambda: perform_conversion(convert_c_to_f),
                    (0, 2): lambda: perform_conversion(convert_c_to_k),
                    (1, 0): lambda: perform_conversion(convert_f_to_c),
                    (1, 1): lambda: perform_conversion(do_not_convert),
                    (1, 2): lambda: perform_conversion(convert_f_to_k),
                    (2, 0): lambda: perform_conversion(convert_k_to_c),
                    (2, 1): lambda: perform_conversion(convert_k_to_f),
                    (2, 2): lambda: perform_conversion(do_not_convert)})
dm.print_axis_values()
dm.run()
