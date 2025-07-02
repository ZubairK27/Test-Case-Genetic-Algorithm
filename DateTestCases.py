import random
import json

def DateGenerator():
    day = str(random.randint(1, 31))
    month = str(random.randint(1, 12))
    year = str(random.randint(1, 9999))
    return day + "/" + month + "/" + year

def DateChecker(date):
    ds, ms, ys = date.split("/")
    try:
        d = int(ds)
        m = int(ms)
        y = int(ys)
    except ValueError:
        return None
    
    if m in [4, 6, 9, 11] and d > 30:
        return "unique1"  # Invalid day for months with max 30 days
    elif m == 2:
        is_leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
        max_day = 29 if is_leap else 28
        if d > max_day:
            return "unique2"  # Invalid February date
    
    if (d == 30 and m in [4, 6, 9, 11]) or (d==1) or (d==31 and m not in [4, 6, 9, 11]) or (y == 9999 or y == 1):
        return "unique3"  # Boundary cases
    
    if (d == 31 and m == 12) or (d == 1 and m == 1) or (d == 29 and m == 2 and is_leap) or (d == 28 and m == 2 and not is_leap): 
        return "unique4" #Special Boundary cases
    
    
    return "standard"

def fitness_score(population):
    category_counts = {}
    categories = []
    scores = []
    
    for date in population:
        category = DateChecker(date)
        categories.append(category)
        category_counts[category] = category_counts.get(category, 0) + 1

    for c in categories:
        scores.append(1 / (1 + category_counts[c]))  # Append to the list
    
    return scores


def rank_selection(population, scores):
    ranked = sorted(zip(population, scores), key=lambda x: x[1], reverse=True)
    selected = [item[0] for item in ranked[:len(population)//2]]  # Select top half
    return selected

def crossover(parent1, parent2):
    d1, m1, y1 = parent1.split("/")
    d2, m2, y2 = parent2.split("/")
    child1 = d1 + "/" + m2 + "/" + y1
    child2 = d2 + "/" + m1 + "/" + y2
    return child1, child2

def mutate(date):
    d, m, y = date.split("/")
    if random.random() < 0.15:  # Mutation probability
        d = str(random.randint(1, 31))
    if random.random() < 0.15:
        m = str(random.randint(1, 12))
    if random.random() < 0.15:
        y = str(random.randint(1, 9999))
    return d + "/" + m + "/" + y

def saveCases(valid_cases, invalid_cases, boundary_cases, special_boundaries, filename="test_cases.json"):
    test_data = {
        "valid_cases": [{"date": date, "category": DateChecker(date)} for date in valid_cases],
        "invalid_cases": [{"date": date, "category": DateChecker(date)} for date in invalid_cases],
        "boundary_cases": [{"date": date, "category": DateChecker(date)} for date in boundary_cases],
        "special_boundaries": [{"date": date, "category": DateChecker(date)} for date in special_boundaries]
    }
    
    with open(filename, "w") as json_file:
        json.dump(test_data, json_file, indent=4)


def GeneticAlgo(generations=100, population_size=50):
    population = [DateGenerator() for _ in range(population_size)]
    coverage = False
    
    print("Genetic Algorithm Running...")
    while not coverage:
        for _ in range(generations):
            scores = fitness_score(population)
            selected = rank_selection(population, scores)
        
            new_population = []
            while len(new_population) < population_size:
                children = []
                for i in range(0, 12, 2):  # Pairwise crossover
                    c1, c2 = crossover(selected[i], selected[i+1])
                    children.extend([mutate(c1), mutate(c2)])
                new_population.extend(children)
        
            population = new_population[:population_size]

        valid_cases = [date for date in population if DateChecker(date) == "standard"][:10]
        invalid_cases = [date for date in population if DateChecker(date) in ("unique1", "unique2")][:10]
        boundary_cases = [date for date in population if DateChecker(date) == "unique3"][:5]
        special_boundaries = [date for date in population if DateChecker(date) == "unique4"][:5]

        print(f"categories: valid_cases: {len(valid_cases)}\ninvalid_cases: {len(invalid_cases)}\nboundary_cases: {len(boundary_cases)}\nspecial: {len(special_boundaries)}\n")
        if len(valid_cases) >= 10 and len(invalid_cases) >= 10 and len(boundary_cases) >= 5 and len(special_boundaries) >= 5:
            coverage = True

    print("Valid Cases:")
    for case in valid_cases:
        print(f"Date: {case}")
    
    print("\nInvalid Cases:")
    for case in invalid_cases:
        print(f"Date: {case}")
    
    print("\nBoundary Cases:")
    for case in boundary_cases:
        print(f"Date: {case}")

    print(f"\nSpecial Boundary Cases:")
    for case in special_boundaries:
        print(f"Date: {case}")

    saveCases(valid_cases, invalid_cases, boundary_cases, special_boundaries)

GeneticAlgo()
