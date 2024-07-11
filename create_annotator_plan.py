import json
if __name__ == "__main__":
    with open('data/raw/A-1.json') as f:
        a1 = json.load(f)

    with open('data/raw/A-2.json') as f:
        a2 = json.load(f)

    with open('data/raw/B-1.json') as f:
        b1 = json.load(f)

    with open('data/raw/B-2.json') as f:
        b2 = json.load(f)

    with open('data/raw/C-1.json') as f:
        c1 = json.load(f)

    with open('data/raw/C-2.json') as f:
        c2 = json.load(f)

    annotator_plan = {
        'Bulbasaur': {
            'A-1.json': {k:a1[str(k)] for k in range(0,30)},
            'B-1.json': {k:b1[str(k)] for k in range(0,30)},
            'C-1.json': {k:c1[str(k)] for k in range(0,30)},
            'A-2.json': {},
            'B-2.json': {},
            'C-2.json': {},
        },
        'Charmander': {
            'A-1.json': {k:a1[str(k)] for k in range(30,40)},
            'B-1.json': {k:b1[str(k)] for k in range(30,40)},
            'C-1.json': {k:c1[str(k)] for k in range(30,40)},
            'A-2.json': {k:a2[str(k)] for k in range(0,20)},
            'B-2.json': {k:b2[str(k)] for k in range(0,10)},
            'C-2.json': {k:c2[str(k)] for k in range(0,30)},
        },
        'Squirtle': {
            'A-1.json': {k:a1[str(k)] for k in range(0,20)},
            'B-1.json': {},
            'C-1.json': {k:c1[str(k)] for k in range(0,10)},
            'A-2.json': {k:a2[str(k)] for k in range(20,40)},
            'B-2.json': {k:b2[str(k)] for k in range(10,40)},
            'C-2.json': {k:c2[str(k)] for k in range(30,40)},
        },
        'Pikachu': {
            'A-1.json': {},
            'B-1.json': {k:b1[str(k)] for k in range(0,20)},
            'C-1.json': {k:c1[str(k)] for k in range(10,40)},
            'A-2.json': {k:a2[str(k)] for k in range(20,40)},
            'B-2.json': {k:b2[str(k)] for k in range(20,40)},
            'C-2.json': {},
        },
        'Pilot': {
            'A-1.json': {k:b1[str(k)] for k in range(0,5)},
            'B-1.json': {k:b1[str(k)] for k in range(0,5)},
            'C-1.json': {k:b1[str(k)] for k in range(0,5)},
            'A-2.json': {},
            'B-2.json': {},
            'C-2.json': {},
        }
    }

    with open('data/charmander.json', 'w') as f:
        json.dump(annotator_plan['Charmander'], f, indent=4)

    with open('data/squirtle.json', 'w') as f:
        json.dump(annotator_plan['Squirtle'], f, indent=4)

    with open('data/bulbasaur.json', 'w') as f:
        json.dump(annotator_plan['Bulbasaur'], f, indent=4)

    with open('data/pikachu.json', 'w') as f:
        json.dump(annotator_plan['Pikachu'], f, indent=4)

    with open('data/pilot.json', 'w') as f:
        json.dump(annotator_plan['Pilot'], f, indent=4)
