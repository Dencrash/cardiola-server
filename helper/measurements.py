from app import db
from models import FrequencyMeasurement, FrequencyMeasurementDaily
import datetime
from sqlalchemy import func


def group_frequency_measurements():
    """Groups all frequency measurements by day and calculates minimum, maximum and average."""

    now = datetime.datetime.now()
    today = datetime.datetime(now.year, now.month, now.day)
    groups = FrequencyMeasurement.query \
        .filter(FrequencyMeasurement.timestamp < today) \
        .group_by(func.date(FrequencyMeasurement.timestamp),
                  FrequencyMeasurement.user_id) \
        .all()

    for group in groups:
        measurements_query_data = db.session \
            .query(func.min(FrequencyMeasurement.rate).label('min'),
                   func.max(FrequencyMeasurement.rate).label('max'),
                   func.avg(FrequencyMeasurement.rate).label('avg')) \
            .filter(func.date(FrequencyMeasurement.timestamp) == group.timestamp.date(),
                    FrequencyMeasurement.user_id == group.user_id) \
            .first()

        measurement = FrequencyMeasurementDaily()
        measurement.date = group.timestamp.date()
        measurement.user_id = group.user_id
        measurement.rate_min = measurements_query_data[0]
        measurement.rate_max = measurements_query_data[1]
        measurement.rate_avg = measurements_query_data[2]

        db.session.add(measurement)
        FrequencyMeasurement.query \
            .filter(func.date(FrequencyMeasurement.timestamp) == group.timestamp.date(),
                    FrequencyMeasurement.user_id == group.user_id) \
            .delete(synchronize_session='fetch')

        print(measurement)

        db.session.commit()


def delete_old_measurements(days=30):
    now = datetime.datetime.now()
    today = datetime.datetime(now.year, now.month, now.day)
    expiration_date = today - datetime.timedelta(days=days)

    deleted_rows = 0
    deleted_rows += FrequencyMeasurement.query \
        .filter(FrequencyMeasurement.timestamp < expiration_date) \
        .delete()

    deleted_rows += FrequencyMeasurementDaily.query \
        .filter(FrequencyMeasurementDaily.date < expiration_date.date()) \
        .delete()

    db.session.commit()

    return deleted_rows
