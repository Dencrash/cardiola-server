from sklearn.externals import joblib
from models.user import User
import numpy as np
from models.measurement import (Measurement, FrequencyMeasurement,
                                FrequencyMeasurementDaily)


class CardiacDiseasePredictor:

    def __init__(self, path_to_model):
        self.model = joblib.load(path_to_model)

    def give_prediction_for_user(self, user_id):
        boolean_features = {'atyp_angina': False, 'asympt': False, 'non_anginal': False,
                            'normal': False, 'left_vent_hyper': False,
                            'st_t_wave_abnormality': False}
        user = User.query.get(user_id)
        measurement = Measurement.query \
                                 .filter(Measurement.user_id == user_id) \
                                 .order_by(Measurement.timestamp.desc()) \
                                 .first()
        daily_pulse = FrequencyMeasurement.query \
                                          .filter(FrequencyMeasurement.user_id == user_id) \
                                          .value(FrequencyMeasurement.rate)
        try:
            max_daily_pulse = max(daily_pulse)
        except:
            max_daily_pulse = daily_pulse
        monthly_pulse = FrequencyMeasurementDaily.query \
                                                 .filter(FrequencyMeasurementDaily.user_id == user_id) \
                                                 .value(FrequencyMeasurementDaily.rate_max)
        try:
            max_monthly_pulse = max(monthly_pulse)
        except:
            max_monthly_pulse = monthly_pulse
        if max_monthly_pulse:
            pulse = max([max_monthly_pulse, max_daily_pulse])
        else:
            pulse = max_daily_pulse
        try:
            boolean_features[user.chest_pain] = True
        except:
            pass
        try:
            boolean_features[user.eck_result] = True
        except:
            pass
        feature_vector = [[user.age, measurement.systolic,
                           pulse, boolean_features['atyp_angina'],
                           boolean_features['asympt'],
                           boolean_features['non_anginal'],
                           user.blood_sugar,
                           boolean_features['normal'],
                           boolean_features['left_vent_hyper'],
                           boolean_features['st_t_wave_abnormality'],
                           user.angina]]
        np_feature_vector = np.array(feature_vector, dtype=float)
        return self.model.predict(np_feature_vector)
