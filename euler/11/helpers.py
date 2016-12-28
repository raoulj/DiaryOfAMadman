"""
Some helpers I have come across to help with the Euler challenges
"""

# originally written for problem 8
def open_local_file(filename):
    """
    Open a file with the filename + extension in filename parameter
    """
    import os
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    return open(os.path.join(__location__, filename), 'r')

