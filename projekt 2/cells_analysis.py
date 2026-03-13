import json

def load_samples(filename="samples.csv"):
    samples = {}
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            name = parts[0]
            values = list(map(int, parts[1:]))
            samples[name] = values
    return samples

def calculate_growth_rate(values):
    differences = []
    for i in range(len(values) - 1):
        diff = values[i + 1] - values[i]
        differences.append(diff)
    if len(set(differences)) == 1:
        return differences[0]
    else:
        return None

def analyze_samples(samples):
    results = {}
    for name, values in samples.items():
        rate = calculate_growth_rate(values)
        results[name] = {
            "linear_growth": rate is not None,
            "growth_rate": rate,
            "min": min(values),
            "max": max(values),
            "average": sum(values) / len(values)
        }
    return results

def save_results(results, filename="results.json"):
    with open(filename, "w") as file:
        json.dump(results, file, indent=4)

def main():
    samples = load_samples()
    results = analyze_samples(samples)
    save_results(results)

if __name__ == "__main__":
    main()