# Print texts with colorful fonts
import sys
from pprint import pprint
import os
from IPython.core.display import display # display results in nice format
from colorama import init
from termcolor import colored
from IPython.display import HTML as html_print


# enable cls() on anaconda console
def cls():
    """Enable cls() in python console

    Returns:
        _type_: acts as cls(cmd windows) or clear(bash)
    """
    return os.system('cls' if os.name=='nt' else 'clear')

# Method that works only on python/cmd console
init()
colored('Python Programming !', 'green', 'on_red')

# Method that works on jupyter notebooks.
def cstr(s, color='black'):
    """returns a colored text on python console

    Args:
        s (str): A string that you want to make it colored.
        color (str, optional): color that you want to speficy. Defaults to 'black'.

    Returns:
        _type_: colored str
    """
    return "<text style=color:{}>{}</text>".format(color, s)

# Turn jupyter method into a function

def clean_print(string, color='red'):
    """Prints a colorful print

    Args:
        string (str): string that you want to print f'' also works.
        color (str, optional): color that you want to use. Defaults to 'black'.

    Returns:
        _type_: colored string
    """
    clean_output = html_print(cstr(f'{string:}', color))
    return display(clean_output)

clean_print('You have imported fancy print function!', 'red')

if __name__ == '__main__':
    init()
    print(colored('Python Programming !', 'green', 'on_red'))
    clean_print('You have imported fancy print function!', 'red')
    left, word, right = 'foo' , 'abc' , 'bar'
    display(html_print(cstr(' '.join([left, cstr(word, color='red'), right]), color='black')))
    display(html_print(cstr('abc', 'red')))
    del left, word, right
