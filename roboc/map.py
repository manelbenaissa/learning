# !usr/bin/python
# -*-coding: utf-8 -*-

"""Define map class."""


class Map:
    """
    Create a Map object.

    It should be easy to:
    - Add a new map
    - Delete a map
    - Modify a map
    """

    def __init__(self, name):
        """
        Methode constructeur.

        Create a map with a text file.
        Define cases with a tuple (i,j) (matrix like)
        - line axis: i
        - column axis : j
        """
        self.name = name
        self._accepted_char = ['O', '.', 'U', 'X', ' ']
        with open('cartes/%s' % (name), 'r') as my_filemap:
            my_map = my_filemap.read()

        def read_map(mymap):
            # map_data contains the tuples about the positions and the value
            map_data = {}
            i = -1
            lines = mymap.splitlines()
            for line in lines:
                # Increment line
                i += 1
                # scroll through every line
                j = -1
                for value in list(line):
                    # Increment column
                    j += 1
                    if value not in accepted_char:
                        raise TypeError(
                            '''
                        incorrect value : %s
                        Please change line %s column %s
                        The map should only contain the following chars:
                        -O
                        -U
                        -.
                        -X
                        or blank spaces
                            ''' % (value, i, j))
                    map_data[(i, j)] = value
            return map_data, i, j

        self._map_tuple = read_map(my_map)
        self.map_data = self._map_tuple[0]
        self.ix_last_line = self._map_tuple[1]
        self.ix_last_column = self._map_tuple[2]

    def __repr__(self):
        """Improve map representation."""
        return "<Map {}>".format(self.name)

    def __del__(self):
        """Delete object."""
        print 'Map Object deleted.'

    def change_map(self, **kwargs):
        """
        Change a map.

        **kwargs is a "dictionnary" with:
        - key : a tuple (i,j)
        - value : new case value

        Raise an error if:
        - key is out of border or is not an (i,j) tuple of numbers
        - value not in accepted_char
        """
        for key in kwargs:
            if type(key) is not tuple:
                raise TypeError('You should enter a (i,j) tuple')

            line = key[0]
            column = key[1]
            if type(line) != int or type(column) != int:
                raise TypeError('Tuple (i,j) should be made of ints')
            if line > self.ix_last_line or column > self.ix_last_column:
                raise ValueError('Index out of border for i=%s and j=%s'
                                 % (line, column))
            if kwargs[key] not in self._accepted_char:
                raise ValueError('incorrect value %s for key %s'
                                 % (kwargs[key], key))
            else:
                self.map_data[(line, column)] = kwargs[key]
