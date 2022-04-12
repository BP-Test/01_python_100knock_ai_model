# Print texts with colorful fonts
import sys
from pprint import pprint
import os
from IPython.core.display import display # display results in nice format
from colorama import init
from termcolor import colored
from IPython.display import HTML as html_print


# Current system path
pprint(sys.path)

os.chdir(os.path.dirname(os.path.abspath("__file__")))
__dir__ = os.getcwd()
pprint(__dir__)


# enable cls() on anaconda console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')




# Method that works only on python/cmd console
init()
print(colored('Python Programming !', 'green', 'on_red'))

# Method that works on jupyter notebooks.
def cstr(s, color='black'):
    return "<text style=color:{}>{}</text>".format(color, s)

left, word, right = 'foo' , 'abc' , 'bar'
display(html_print(cstr(' '.join([left, cstr(word, color='red'), right]), color='black')))
display(html_print(cstr('abc', 'red')))
del left, word, right

# Turn jupyter method into a function

def clean_print(string, color='black'):
    return html_print(cstr(f'{string:}', color))

