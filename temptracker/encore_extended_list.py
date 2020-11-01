"""An extended python list class with included recursive flatten method."""

class EncoreExtendedList(list):
    """Extend `list` base class with custom methods."""
    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        """Initialize base list."""
        super(EncoreExtendedList, self).__init__(*args, **kwargs)  # pylint: disable=super-with-arguments

    def flatten(self, target=None):
        """Return flattened version of given target list recursively.

        Parameters
        ----------
        target : list, optional
            Target list to flatten, by default None

        Returns
        -------
        list
            Flattened version of target list, or self
        """
        flattened_list = []
        for item in target or self:
            if isinstance(item, list):
                flattened_list.extend(self.flatten(item))
                continue
            flattened_list.extend([item])
        return flattened_list
