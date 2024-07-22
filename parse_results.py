import json
if __name__ == "__main__":
    experiments = ['bulbasaur.json', 'charmander.json']
    results = {
        'A-1': {
            "relevance": [],
            "argumentativeness": [],
            "factuality": [],
            "best_overall": []
        },
        'A-2': {
            "relevance": [],
            "argumentativeness": [],
            "factuality": [],
            "best_overall": []
        },
        'B-1': {
            "relevance": [],
            "argumentativeness": [],
            "factuality": [],
            "best_overall": []
        },
        'B-2': {
            "relevance": [],
            "argumentativeness": [],
            "factuality": [],
            "best_overall": []
        },
        'C-1': {
            "relevance": [],
            "argumentativeness": [],
            "factuality": [],
            "best_overall": []
        },
        'C-2': {
            "relevance": [],
            "argumentativeness": [],
            "factuality": [],
            "best_overall": []
        }
    }
    for exp in experiments:
        with open(f'data/{exp}') as f:
            data = json.load(f)
        for exp_name in data:
            exp_key = exp_name.replace(".json", "")
            if exp_key not in results.keys():
                raise ValueError(f"Found unrecognised experiment file: {exp_name}")
            for exp_index in data[exp_name]:
                for metric in ['argumentativeness', 'factuality', 'relevance', 'overall']:
                    for response in data[exp_name][exp_index][metric]:
                        metric_winner = f"model{data[exp_name][exp_index][metric]}"
                        results[exp_key][metric].append(metric_winner)
    with open('out.json', 'w') as f:
        json.dump(results, f, indent=4)