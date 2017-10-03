"""
This file will deal with getting colour schemes set up
"""

class ColourScheme:
    """
    A very basic class for holding colour schemes.
    """
    def __init__(self, lightest, lighter, darker, darkest):
        self.lightest = lightest
        self.lighter = lighter
        self.darker = darker
        self.darkest = darkest

# Set up some colour schemes
BLUESCHEME = ColourScheme("#FFFFFF", "#6699FF", "#3366CC", "#003399")
GREENSCHEME = ColourScheme("#CCFFBB", "#88E188", "#3A5F0B", "#005A04")
