import json

data = {
    'employees': [
        {
            'name': 'John Doe',
            'department': 'Marketing',
            'place': 'Remote'
        },
        {
            'name': 'Jane Doe',
            'department': 'Software Engineering',
            'place': 'Remote'
        },
        {
            'name': 'Don Joe',
            'department': 'Software Engineering',
            'place': 'Office'
        }
    ]
}


json_string = json.dumps(data)
print(json.dumps(data, indent=4))
""" with open('json_data.json', 'w') as outfile:
    outfile.write(json_string) """