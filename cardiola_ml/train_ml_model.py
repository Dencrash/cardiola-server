from sklearn.ensemble import RandomForestClassifier
from dataset_creation import load_dataset
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib
import argparse


def main(data, output):
    dataset = load_dataset(data)
    train_set, test_set = train_test_split(dataset, train_size=0.8)
    classifier = RandomForestClassifier()
    classifier.fit(train_set[:, :-1], train_set[:, -1])
    joblib.dump(classifier, output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create simple ml-model')
    parser.add_argument('data',
                        help='Csv file with the patient data')
    parser.add_argument('output', help='directory to save the pickle model')
    args = parser.parse_args()
    main(args.data, args.output)
