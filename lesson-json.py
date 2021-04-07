import json

candidates = [
    {
        'first_name': 'Hrant',
        'last_name': 'Arakelyan',
        'position': 'Junior C++',
        'skills': ['C++', 'Java', 'Python', 'Ruby', 'LabView'],
        'contract_type': 'part-time',
        'student': True,
        'previous_job': None
    },
    {
        'name': 'Avet',
        'last_name': 'Barseghyan',
        'position': 'Junior content manager',
        'skills': ['songwriter', 'TV host'],
        'student': False,
        'special signs': 'selfish',
        'email': 'mi_hrashali@andznavorutyun.com'
    }
]
# dumps method is just converting to a json-format string
candidate_json_format = json.dumps(candidates)
print(candidate_json_format)

# loads method converts json-format to a python format
candidate_python_format = json.loads(candidate_json_format)
print(candidate_python_format)

################
# dump method is saving data to a json file
with open('cand.json', 'w') as out_file:
    # indent is an optional parameter that adds spaces for readability
    # sort_keys is an optional parameter to save json keys in alphabetical order
    json.dump(candidates, out_file, indent=4, sort_keys=True)

# load method is bringing data from a json file to a python object
# with open('cand.json', 'r') as out_file:
#     data = json.load(out_file)
# print(type(data))
# print(data)
# print(candidates)
# print(candidates[0]==data[0])
