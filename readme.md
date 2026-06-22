# Slimepocalypse Initiative

**COMP1005 – Object-Oriented Programming Project**

## GitHub Repository

GitHub Classroom Repository:

https://github.com/sneha-agg/assessment-4-sneha-agg-001.git


## Overview

The Slimepocalypse Initiative is a slime experimentation and management system developed using Object-Oriented Programming principles in Python.

The system allows different slime species to be created, managed, enhanced through environmental conditions, and combined within a laboratory environment.

This project demonstrates key software engineering and object-oriented design concepts including:

* Abstraction
* Encapsulation
* Inheritance
* Polymorphism
* Composition
* Exception Handling
* Unit Testing
* UML Design

---

# UML Design

A UML Class Diagram has been provided with the submission:

```text
Slime_Project_UML.puml
```

The UML diagram documents:

* Class relationships
* Inheritance hierarchy
* Composition relationships
* Dependencies
* Attributes
* Methods

---

# Project Structure

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
├── Slime_Project_UML.puml
├── self_evaluation.txt
├── README.md
└── requirements.txt
```

---

# Object-Oriented Design

## Abstract Base Class

### Slime

The `Slime` class is implemented as an abstract base class.

Common slime functionality is defined once and reused by all slime types.

Abstract methods:

```python
get_slime_type()
get_special_attributes()
```

These methods must be implemented by all subclasses.

---

## Inheritance

The project uses inheritance to reduce duplication and improve maintainability.

```text
Slime
│
├── ShadowSlime
│
└── StormSlime
```

Each slime type inherits common behaviour while implementing its own specialised functionality.

---

## Encapsulation

Encapsulation is achieved through:

* Properties
* Setters
* Validation logic

Examples:

* ID validation
* Size validation
* Constructor validation

This prevents invalid object creation and improves reliability.

---

## Polymorphism

Polymorphism is demonstrated through the use of shared interfaces.

Different slime types implement:

```python
get_slime_type()
get_special_attributes()
```

The `Laboratory` class can work with any slime type through the common `Slime` interface.

---

## Composition

Composition is demonstrated through the relationship between:

```text
Laboratory -> Slime
```

The laboratory stores and manages multiple slime objects.

---

# Features

## Shadow Slime

Attributes:

* shadow_density
* stealth_mode

Methods:

* hide()
* reveal()
* calculate_power()

---

## Storm Slime

Attributes:

* lightning_charge
* rain_intensity

Methods:

* charge_storm()
* release_lightning()
* calculate_power()

---

## Weather Station

The Weather Station affects Storm Slimes by modifying environmental conditions.

Methods:

```python
boost_storm()
monitor_conditions()
```

---

## Laboratory

The Laboratory is responsible for:

* Adding slimes
* Removing slimes
* Managing slime collections
* Combining slimes
* Tracking active slime instances

---

# Slime Combination Logic

When two slimes are combined:

1. Volatility values are evaluated.
2. Explosion probability is calculated.
3. If an explosion occurs:

   * Both slimes are removed.
   * "EXPLOSION" is returned.
4. Otherwise:

   * A parent slime is selected.
   * A deep copy is created.
   * The offspring receives a new ID.
   * The offspring is added to the laboratory.

---

# Exception Handling

Exception handling has been implemented to improve robustness.

Examples include:

* Invalid slime IDs
* Invalid slime sizes
* Invalid humidity values
* Missing slime references
* Invalid laboratory operations

Exceptions used:

```python
ValueError
TypeError
KeyError
```

---

# Running the Application

Execute the demonstration program:

```bash
python3 main.py
```

The program demonstrates:

* Slime creation
* Power calculations
* Weather interactions
* Laboratory management
* Slime combination mechanics

---

# Testing

Unit testing is implemented using Pytest.

Run all tests:

```bash
pytest
```

Run verbose tests:

```bash
pytest -v
```

Generate a coverage report:

```bash
pytest --cov=. --cov-report=term-missing
```

Testing covers:

* Slime creation
* Validation logic
* Power calculation
* Weather effects
* Laboratory operations
* Slime combination behaviour

---

# Requirements

* Python 3.10+
* pytest
* pytest-cov

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Documentation

Additional documentation included in this submission:

```text
README.md
Slime_Project_UML.puml
self_evaluation.txt
```

---

# Learning Outcomes

This project demonstrates practical application of:

* Object-Oriented Programming
* Abstract Base Classes
* Inheritance
* Encapsulation
* Polymorphism
* Composition
* Exception Handling
* Unit Testing
* Software Documentation

---

# Author

Sneha Aggarwal

COMP1005 – Object-Oriented Programming

Slimepocalypse Initiative Project
