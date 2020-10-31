# TempTracker - an outline of a basic simple Python application deployment using `pip`.

Record temperature readings as integers, and perform math operations on the collection of readings.

As a bonus feature, temperature-readings are stored using `EncoreExtendedList` list, allowing for
non-destructive nesting of readings.

Some important features have been intentionally left as 'TODO' markers to demonstrate documentation
style.


## Getting Started

Clone or download this repository and navigate to its directory:
```bash
git clone https://github.com/jacobmartinez3d/temptracker.git
cd temptracker
```

#### It is reccomended to first create a virtual-environment to avoid installing globally:

Linux:
```bash
virtualenv venv
source venv/bin/activate
```

Windows:
```cmd
virtualenv venv
venv\Scripts\activatee
```

#### Install using `pip`:
```bash
pip install .
```

### Prerequisites

Must have at least `Python 2.7` as well as `pip` installed.

### Running

With the virtual environment still active, launch your Python interpereter and try out the following commands:
```python
from temptracker import TempTracker

# instantiate with a list of readings
tt = TempTracker([5, 8, 15, 90])

# get max temperature
tt.get_max()

# get min temperature
tt.get_min()

# get mean of all temperature-readings
tt.get_mean()

# insert new reading
tt.insert(110)

# lists can be nested, for organization
nested_readings_example = TempTracker([2, [68, 70, [[110]]], 98, 109, [5, [101, 102]]])

# retrieve current readings
nested_readings_example.readings

# get mean of all values
nested_readings_example.get_mean()
```
### Running tests

Unittest module is used and tests are kept outside of the core module in `tests` directory.

From the project root run tests from terminal with:
```bash
python -m unittest discover -s tests --verbose
```

## Authors

* **Jacob Martinez** - *Developer* - [Magnetic-Lab](https://www.magnetic-lab.com)
