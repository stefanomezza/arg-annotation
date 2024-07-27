import json
if __name__ == "__main__":
    experiments = ['bulbasaur.json', 'charmander.json', 'squirtle.json', 'pikachu.json']
    #experiments=['squirtle.json']
    metrics = ['argumentativeness', 'factuality', 'relevance', 'best_overall']
    results = {
            'A': {m:{str(x): [] for x in range(0,40)} for m in metrics},
            'B': {m:{str(x): [] for x in range(0,40)} for m in metrics},
            'C': {m:{str(x): [] for x in range(0,40)} for m in metrics}
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
                        results[exp_key][metric][exp_index].append(metric_winner)

    for res in results:
       print(f'---------{res}--------')
       for m in metrics:
            print(f"---{m}---")
            wins = {}
            for exp in results[res][m]:
                l = results[res][m][exp]
                winner = (max(set(l), key = l.count))
                wins[winner]= wins.get(winner,0)+1
            for candidate in wins:
                print(f"{candidate}: {wins[candidate]/40}")
    with open('out.json', 'w') as f:
        json.dump(results, f, indent=4)
