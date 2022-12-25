import json

DELIMITER = ','
NEW_LINE = '\n'
INPUT_FILE = "input.csv"


def csv_to_list_dict(file) -> list[dict]:
    def create_element(list_):
        return {headers[j]: list_[j] for j in range(len(headers))}

    with open(file, 'r') as f:
        str_file = f.read()
    rows = []
    for i in str_file.split(NEW_LINE):
        rows.append(i.split(DELIMITER))
    headers = rows[0]
    return [create_element(rows[i]) for i in range(1, len(rows))]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
