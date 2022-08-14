"""Functions to parse a file containing villager data."""


from re import search


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    villagers_data = open(filename)
    for line in villagers_data:
        line = line.rstrip()
        tokens = line.split("|")

        species.add(tokens[1])

    return species

# To test then function
# print(all_species('villagers.csv'))

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    villager_data = open(filename)

    for line in villager_data:
        line = line.rstrip()
        tokens = line.split("|")
        villager_name, villager_specie, *_ = tokens

        # print(villager_name, villager_specie)

        if search_string == "All":
            villagers.append(villager_name)
        elif villager_specie == search_string:
            villagers.append(villager_name)

    return sorted(villagers)

# To test then function
# print(get_villagers_by_species('villagers.csv', 'Wolf'))

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code

    return []


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
