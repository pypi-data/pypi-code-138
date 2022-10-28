"""Python module to print coloured text and background

see: https://www.geeksforgeeks.org/print-colours-python-terminal/
"""

# from dvbctrl.errors import errorNotify


class colours:
    """colours class:reset all colours with colours.reset; two
    sub classes fg for foreground
    and bg for background; use as colours.subclass.colourname.
    i.e. colours.fg.red or colours.bg.green also, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colours.bold
    """

    reset = "\033[0m"
    bold = "\033[01m"
    disable = "\033[02m"
    underline = "\033[04m"
    reverse = "\033[07m"
    strikethrough = "\033[09m"
    invisible = "\033[08m"

    class fg:
        black = "\033[30m"
        red = "\033[31m"
        green = "\033[32m"
        orange = "\033[33m"
        blue = "\033[34m"
        purple = "\033[35m"
        cyan = "\033[36m"
        lightgray = "\033[37m"
        darkgray = "\033[90m"
        lightred = "\033[91m"
        lightgreen = "\033[92m"
        yellow = "\033[93m"
        lightblue = "\033[94m"
        pink = "\033[95m"
        lightcyan = "\033[96m"

    class bg:
        black = "\033[40m"
        red = "\033[41m"
        green = "\033[42m"
        orange = "\033[43m"
        blue = "\033[44m"
        purple = "\033[45m"
        cyan = "\033[46m"
        lightgray = "\033[47m"
