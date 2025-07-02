Date Test Case Generator using Genetic Algorithm

This project uses a Genetic Algorithm to generate diverse and categorized date test cases for testing date validation logic. The algorithm evolves a population of randomly generated dates to achieve coverage across various edge and boundary conditions.
 Features

    ✅ Valid Dates — Typical calendar-valid dates.

    ❌ Invalid Dates — Dates that are not possible (e.g., 31/04/2024).

    ⚠️ Boundary Cases — Dates on the edge of validity (e.g., 1/1/1000, 30/4/yyyy).

    ⭐ Special Boundary Cases — Rare but valid edge cases (e.g., leap day 29/2/yyyy, 31/12/yyyy).

 How It Works

    Initial Population
    Randomly generates a population of date strings.

    Fitness Evaluation
    Each date is categorized:

        "standard": Valid

        "unique1": Invalid day in a 30-day month

        "unique2": Invalid February date

        "unique3": General boundary cases

        "unique4": Special cases like leap day, 31/12, etc.

    Dates in overrepresented categories receive lower fitness.

    Selection
    Top 50% of the population is selected based on fitness.

    Crossover
    Combines parts of parent dates to produce new children.

    Mutation
    Randomly alters parts of some dates to introduce variation.

    Termination Condition
    The algorithm stops when it generates at least:

        10 valid cases

        10 invalid cases

        5 boundary cases

        5 special boundary cases

    Saving Output
    All test cases are saved in test_cases.json.

🧪 Output Example

{
    "valid_cases": [
        { "date": "12/10/2020", "category": "standard" },
        ...
    ],
    "invalid_cases": [
        { "date": "31/04/2022", "category": "unique1" },
        ...
    ],
    "boundary_cases": [
        { "date": "1/6/2023", "category": "unique3" },
        ...
    ],
    "special_boundaries": [
        { "date": "29/2/2024", "category": "unique4" },
        ...
    ]
}

How to Run
Requirements

    Python 3.x

Run the Algorithm

python your_script_name.py

The algorithm will print out categorized test cases and save them in test_cases.json.
Concepts Covered

    Genetic Algorithms: Initialization, fitness, selection, crossover, mutation

    Date validation and categorization

    Test case generation for software testing
Author

    Zubair Khalid
