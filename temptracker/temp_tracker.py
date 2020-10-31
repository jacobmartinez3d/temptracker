"""An application for recording and performing math on temperature readings."""
from .encore_extended_list import EncoreExtendedList


class TempTrackerError(Exception):
    """An error has occured preventing TempTracker to continue."""
    
class InvalidTemperatureError(TempTrackerError):
    """User has submitted an invalid temperature reading."""
    def __init__(self, reading):
        """Initialize with the invalid reading val

        Parameters
        ----------
        reading : not int
            The invalid reading value given by user.
        """
        self.reading = reading
        self.message = "{0} is an invalid reading, must be of type: `int`.".format(reading)

class TempTracker:
    """This class holds state with the `readings` attribute.
    
    When performing math on `readings` the contents are first flattened - so lists can be nested.
    """
    def __init__(self, initial_temperatures=None):
        """Initialize with optional list of readings.
        
        TODO: contents of initial list need to be validated as integers

        Parameters
        ----------
        initial_temperatures : list, optional
            List of integer temperature readings, by default None

        Raises
        ------
        TempTrackerError
            Initialization failed
        """
        if not initial_temperatures:
            initial_temperatures = []
        elif not isinstance(initial_temperatures, list):
            raise TempTrackerError("First argument must be a list of integers.")
        self.readings = EncoreExtendedList(initial_temperatures)
        
    def __str__(self):
        """Override default string-representation for readabilty.

        Returns
        -------
        str
            Human-readable string representation of current state.
        """
        return "<TempTracker: readings={readings}>".format(
            readings=", ".join([str(r) for r in self.readings])
        )
    
    def __repr__(self):
        return self.__str__()
    
    def insert(self, temperature):
        """Append new temperature-reading integer to `readings`.

        Parameters
        ----------
        temperature : int
            Temperature reading to append to state
        """
        if not isinstance(temperature, int):
            raise(InvalidTemperatureError(temperature))
        self.readings.append(temperature)
        
    def get_max(self):
        """Retrieve the highest temperature currently held.

        Returns
        -------
        int
            The highest-value temperature currently stored in `readings`
        """
        return max(self.readings.flatten())
    
    def get_min(self):
        """Retrieve the lowest temperature currently held.

        Returns
        -------
        int
            The lowest-value temperature currently stored in `readings`
        """
        return min(self.readings.flatten())
    
    def get_mean(self):
        """Retrieve the mean of all currently held temperature readings.

        Returns
        -------
        float
            The mean of all currently held temperature readings
        """
        return float(sum(self.readings.flatten()) / len(self.readings.flatten()))