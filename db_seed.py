from app import db
from models import User, Plan, PlanEntry, Measurement, FrequencyMeasurement
import datetime
import random


def seed():
    # Users
    user1 = User()
    user1.name = 'Daniel'
    user1.chest_pain = ''
    user1.eck_result = ''
    user1.blood_sugar = False
    user1.angina = False
    user1.age = 21
    db.session.add(user1)

    user2 = User()
    user2.name = 'Bernd'
    user2.chest_pain = ''
    user2.eck_result = ''
    user2.blood_sugar = True
    user2.angina = False
    user2.age = 67
    db.session.add(user2)

    # Plans
    plan1 = Plan()
    plan1.user = user1
    db.session.add(plan1)

    plan2 = Plan()
    plan2.user = user2
    db.session.add(plan2)

    # Plan entries
    for _ in range(10):
        entry1 = PlanEntry()
        entry1.timestamp = datetime.time(random.randint(0, 23), random.randint(0, 59))
        entry1.mandatory = random.randint(0, 1) == 0
        entry1.plan = plan1
        db.session.add(entry1)

        entry2 = PlanEntry()
        entry2.timestamp = datetime.time(random.randint(0, 23), random.randint(0, 59))
        entry2.mandatory = random.randint(0, 1) == 0
        entry2.plan = plan2
        db.session.add(entry1)

    # Measurements
    for _ in range(100):
        measurement = Measurement()
        measurement.user = user1 if random.randint(0, 1) == 0 else user2
        measurement.pulse = random.randint(60, 120)
        measurement.systolic = random.randint(100, 130)
        measurement.diastolic = random.randint(60, 100)
        measurement.timestamp = datetime.datetime(
            2016,
            1,                      # Monat
            random.randint(1, 31),  # Tag (vereinfacht)
            random.randint(0, 23),  # Stunde
            random.randint(0, 59)   # Minute
        )
        db.session.add(measurement)

    # Frequency Measurements
    for _ in range(1000):
        measurement = FrequencyMeasurement()
        measurement.user = user1 if random.randint(0, 1) == 0 else user2
        measurement.rate = random.randint(60, 120)
        measurement.timestamp = datetime.datetime(
            2016,
            1,                      # Monat
            random.randint(1, 31),  # Tag (vereinfacht)
            random.randint(0, 23),  # Stunde
            random.randint(0, 59)   # Minute
        )
        db.session.add(measurement)

    db.session.commit()


if __name__ == '__main__':
    seed()
