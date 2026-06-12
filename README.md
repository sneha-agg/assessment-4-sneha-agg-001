# Slime Laboratory Management System

## Overview

The Slime Laboratory Management System is a Python-based object-oriented application that simulates the creation, management, and interaction of different slime species inside a laboratory environment.

The project demonstrates key Object-Oriented Programming (OOP) concepts including:

- Abstraction
- Inheritance
- Encapsulation
- Polymorphism
- Composition
- Property Validation

The system supports multiple slime types, power calculations, environmental interactions, and slime combination mechanics.

---

## Project Structure

```
assessment-4-sneha-agg-001/
│
├── slime.py              # Abstract base class for all slimes
├── shadow_slime.py       # Shadow Slime implementation
├── storm_slime.py        # Storm Slime implementation
├── laboratory.py         # Laboratory management system
├── weather_station.py    # Environmental effects on slimes
├── README.md             # Project documentation
└── .gitignore
```

---

## Features

### 1. Abstract Slime Base Class

The `Slime` class serves as the foundation for all slime types.

#### Attributes

- `id` – Unique slime identifier
- `name` – Slime name
- `size` – Physical size of the slime
- `volatility` – Random value between 0 and 10
- `base_power` – Starting power value
- `power` – Calculated power level

#### Methods

- `calculate_power()`
- `get_slime_type()` *(abstract)*
- `get_special_attributes()` *(abstract)*

---

### 2. Shadow Slime

Represents stealth-based slimes.

#### Additional Attributes

- `shadow_density`
- `stealth_mode`

#### Methods

- `hide()`
- `reveal()`
- `get_slime_type()`
- `get_special_attributes()`

---

### 3. Storm Slime

Represents weather-based slimes with lightning abilities.

#### Additional Attributes

- `lightning_charge`
- `rain_intensity`

#### Methods

- `charge_storm()`
- `release_lightning()`
- `get_slime_type()`
- `get_special_attributes()`

---

### 4. Laboratory

Manages all slimes in the system.

#### Features

- Add slimes
- Remove slimes
- Combine slimes
- Store slimes using unique IDs

#### Combination Logic

When two slimes are combined:

1. Explosion probability is calculated using both slime volatilities.
2. If an explosion occurs:
   - Both slimes are removed.
   - `"EXPLOSION"` is returned.
3. Otherwise:
   - One parent slime is selected randomly.
   - A deep copy is created.
   - The child slime receives a new ID.
   - The new slime is added to the laboratory.

---

### 5. Weather Station

Provides environmental interactions for Storm Slimes.

#### Attributes

- `humidity`
- `air_pressure`

#### Methods

##### `boost_storm(storm_slime)`

Enhances a Storm Slime by:

- Increasing lightning charge by 5
- Increasing rain intensity by 1

##### `monitor_conditions()`

Returns current weather conditions.

---

## Power Calculation

The slime power is calculated using:

- Base power
- Numeric attributes
- String values (converted using ASCII values)
- Boolean attributes

Formula Components:

1. Sum all numeric values.
2. Convert strings into ASCII totals.
3. Multiply string contribution by π.
4. Apply boolean modifiers:
   - `True` → double power
   - `False` → halve power

The final value is rounded to 2 decimal places.

---

## Example Usage

```python
from shadow_slime import ShadowSlime
from storm_slime import StormSlime
from laboratory import Laboratory
from weather_station import WeatherStation

# Create slimes
shadow = ShadowSlime(
    "S1",
    "NightCrawler",
    4,
    shadow_density=8,
    stealth_mode=True
)

storm = StormSlime(
    "ST1",
    "Thunder",
    5,
    lightning_charge=20,
    rain_intensity=3
)

# Calculate power
print(shadow.calculate_power())
print(storm.calculate_power())

# Laboratory
lab = Laboratory()
lab.add_slime(shadow)
lab.add_slime(storm)

print(lab)

# Weather interaction
weather = WeatherStation(70, 1013)
weather.boost_storm(storm)

print(weather.monitor_conditions())
```

---

## OOP Concepts Demonstrated

| Concept | Implementation |
|----------|---------------|
| Abstraction | `Slime` abstract class |
| Inheritance | `ShadowSlime`, `StormSlime` |
| Encapsulation | Property getters/setters |
| Polymorphism | Overridden abstract methods |
| Composition | Laboratory manages slime objects |
| Validation | Type checking in properties |

---

## Requirements

- Python 3.8+
- No external libraries required

---

## Learning Outcomes

This project demonstrates:

- Designing class hierarchies
- Using abstract base classes
- Working with inheritance and polymorphism
- Managing object collections
- Implementing simulation-style business logic
- Applying object-oriented design principles

---

## Author

**Sneha Aggarwal**

Assessment 4 – Object-Oriented Programming Project
