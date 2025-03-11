import json

sample_json = [
    {
        "name": "Mary",
        "modules": [
            {
                "name": "science",
                "grade": 80
            },
            {
                "name": "maths",
                "grade": 90
            }
        ]
    }
]
def do_save(filename):
    with open(filename, "tw") as fp:
        json.dump(sample_json,fp)