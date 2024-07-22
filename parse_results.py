import json
if __name__ == "__main__":
    experiments = ['bulbasaur.json', 'charmander.json']
    metrics = ['argumentativeness', 'factuality', 'relevance', 'best_overall']
    results = {
        'A': {m:[] for m in metrics},
        'B': {m:[] for m in metrics},
        'C': {m:[] for m in metrics}
    }
    for exp in experiments:
        with open(f'data/{exp}') as f:
            data = json.load(f)
        for exp_name in data:
            exp_key = exp_name.replace(".json", "").split("-")[0]
            if exp_key not in results.keys():
                raise ValueError(f"Found unrecognised experiment file: {exp_name}")
            for exp_index in data[exp_name]:
                for metric in metrics:
                    for response in data[exp_name][exp_index][metric]:
                        metric_winner = data[exp_name][exp_index][f"model{response}"]
                        results[exp_key][metric].append(metric_winner)
    for res in results:
        print(f'---------{res}--------')
        for m in metrics:
            metric_candidates = list(set(results[res][m]))
            print(f"---{m}---")
            for candidate in metric_candidates:
                print(f"{candidate}: {str(len([x for x in results[res][m] if x==candidate])/len(results[res][m])*100)+'%'}")
    with open('out.json', 'w') as f:
        json.dump(results, f, indent=4)
