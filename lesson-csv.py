import csv

candidate = {
    'first_name': 'Hrant',
    'last_name': 'Arakelyan',
    'position': 'Junior C++',
    'skills': ['C++', 'Java', 'Python', 'Ruby', 'LabView'],
    'contract_type': 'part-time',
    'student': True,
    'previous_job': None
}
with open('candidate.csv', 'w', newline='') as cand_file:
    fieldnames = [key for key in candidate.keys()]  # fieldnames is for having the list of column names
    # fieldnames = ['first_name', 'last_name']
    print(fieldnames)
    writer = csv.DictWriter(cand_file, fieldnames=fieldnames)

    writer.writeheader()  # this will add column names
    writer.writerow(candidate)  # writes an actual row from given dict
