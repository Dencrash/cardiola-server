from app import db
from flask.ext.restful import Resource
from cardiola_ml.cardiola_predictor import CardiacDiseasePredictor


class PredictionAPI(Resource):

    prediction_object = CardiacDiseasePredictor("ml_model/rc.pkl")

    def get(self, user_id):
        result = self.prediction_object.give_prediction_for_user(user_id)
        return result[0]
