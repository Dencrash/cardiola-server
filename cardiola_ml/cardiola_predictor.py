from sklearn.externals import joblib
from models.user import User
from models.measurement import (Measurement, FrequencyMeasurement,
                                FrequencyMeasurementDaily)


class CardiacDiseasePredictor:

    def __init__(self, path_to_model):
        self.model = joblib.load(path_to_model)

    def give_prediction_for_user(self, user_id):
        user = User.query.get(user_id)
        measurement = Measurement.query \
                                 .filter(Measurement.user_id == user_id) \
                                 .order_by(Measurement.timestamp.desc()) \
                                 .first()
        daily_pulse = FrequencyMeasurement.query \
                                          .filter(FrequencyMeasurement.user_id == user_id) \
                                          .value(FrequencyMeasurement.rate)
        max_daily_pulse = max(daily_pulse)
        monthly_pulse = FrequencyMeasurementDaily.query \
                                                 .filter(FrequencyMeasurementDaily.user_id == user_id) \
                                                 .value(FrequencyMeasurementDaily.rate_max)
        max_monthly_pulse = max(monthly_pulse)
        pulse = max([max_monthly_pulse, max_daily_pulse])
        print(user)
        print(pulse)
        return False
