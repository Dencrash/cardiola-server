import csv
import numpy


def load_dataset(path):
    with open(path) as f:
        dataset = csv.reader(f)
        result = []
        next(dataset)
        for (age, chest_pain, bp, bs,
             eck, heart_rate, angina, disease) in dataset:
            atyp = chest_pain == "atyp_angina"
            asympt = chest_pain == "asympt"
            non_aginal = chest_pain == "non_anginal"
            bp_normal = eck == "normal"
            bp_left_vent = eck == "left_vent_hyper"
            bp_st_wave = eck == "st_t_wave_abnormality"
            ex_angina = angina == "yes"
            high_blood_sugar = bs == "t"
            dis = disease == "positive"
            result.append([age, bp, heart_rate, atyp, asympt,
                           non_aginal, high_blood_sugar, bp_normal,
                           bp_left_vent, bp_st_wave, ex_angina,
                           dis])
    output = numpy.array(result, dtype=float)
    return output
