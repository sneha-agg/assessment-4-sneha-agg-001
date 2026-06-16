# Slimepocalypse Initiative

COMP1005 – Object-Oriented Programming Project

A slime experimentation system built using Object-Oriented Programming principles in Python.

---

## Project Structure

```text
slime_project/
│
├── slime.py
├── shadow_slime.py
├── storm_slime.py
├── weather_station.py
├── laboratory.py
├── main.py
│
├── tests/
│   ├── test_slime.py
│   ├── test_shadow_slime.py
│   ├── test_storm_slime.py
│   ├── test_weather_station.py
│   └── test_laboratory.py
│
├── self_evaluation.txt
└── README.md
```

---

## Requirements

- Python 3.10 or newer
- pip
- pytest
- pytest-cov

---

## Ubuntu Setup

### Update package list

```bash
sudo apt update
```

### Install Python and pip

```bash
sudo apt install python3 python3-pip python3-venv -y
```

Verify installation:

```bash
python3 --version
pip3 --version
```

---

## Create Virtual Environment

Navigate to the project folder:

```bash
cd slime_project
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

You should now see:

```text
(venv)
```

at the beginning of your terminal prompt.

---

## Install Dependencies

Install testing packages:

```bash
pip install pytest pytest-cov
```

Verify:

```bash
pytest --version
```

---

## Running the Application

Execute the main demonstration program:

```bash
python3 main.py
```

The program will:

- Create Shadow Slimes
- Create Storm Slimes
- Create a Weather Station
- Calculate slime powers
- Store slimes in a Laboratory
- Demonstrate slime interactions
- Demonstrate replication/explosion functionality

---

## Running Tests

Run all tests:

```bash
pytest
```

Expected output:

```text
===== test session starts =====
...
5 passed
```

---

## Run Tests Verbosely

```bash
pytest -v
```

---

## Generate Coverage Report

```bash
pytest --cov=. --cov-report=term-missing
```

Example:

```text
Name                    Stmts   Miss  Cover
--------------------------------------------
slime.py                  60      2    97%
shadow_slime.py           18      0   100%
storm_slime.py            20      0   100%
weather_station.py        10      0   100%
laboratory.py             30      1    97%
--------------------------------------------
TOTAL                    138      3    98%
```

---

## Deactivate Virtual Environment

When finished:

```bash
deactivate
```

---

## Creating Submission ZIP

From the directory above the project folder:

```bash
zip -r slime_project.zip slime_project
```

Or:

```bash
tar -czvf slime_project.tar.gz slime_project
```

---

## Key OOP Concepts Demonstrated

### Encapsulation

- Private attributes
- Properties
- Setters with validation

### Inheritance

- ShadowSlime inherits from Slime
- StormSlime inherits from Slime

### Abstraction

- Slime is an abstract base class
- Abstract methods enforce implementation

### Polymorphism

- Different slime types implement shared methods differently

### Composition

- Laboratory manages Slime objects
- WeatherStation interacts with StormSlime

### Testing

- Pytest unit tests
- Coverage reporting

---

## Author

Sneha

COMP1005 Object-Oriented Programming

Slimepocalypse Initiative Project