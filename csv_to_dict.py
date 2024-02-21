import csv

def csv_to_dict(csv_file_path):
    data = []
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

if __name__ == "__main__":
    csv_file_path = "/home/mchavez76/python/palworld/Copy of CWM Palworld - Pals.csv"
  # Replace with the actual path to your CSV file
    result = csv_to_dict(csv_file_path)
    print(result)
