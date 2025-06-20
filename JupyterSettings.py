#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2024 Rui Ribeiro
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
A Python library of functions for modifying Jupyter settings.
"""

__author__ = "Rui P. Ribeiro"
__email__ = "ruipedrofr@gmail.com"
__version__ = "1.0.0"

def AutoReload():
    """
    Enabling automatic reloading of modules before executing each line of code.
    """
    from IPython import get_ipython

    # Load the autoreload extension
    get_ipython().run_line_magic('load_ext', 'autoreload')

    # Set autoreload behavior
    get_ipython().run_line_magic('autoreload', '2')

def CellSize(size):
    """
    Defining the cell size based on percentage of space that cell will occupy.

    :parameter size: (int) percentage (eg: 98)
    """
    from IPython.display import display, HTML
    

    try:
        import notebook
        if int(notebook.__version__.split('.')[0])>= 7:
            #display(HTML(f'<style>.jp-WindowedPanel-outer {{padding-left: 2% !important; padding-right: 2% !important; width:{size}% !important;}} </style>'))
            display(HTML(f'<style>.container {{width: {size}% !important;}}</style>'))


        else: display(HTML(f'<style>.container {{width: {size}% !important;}}</style>'))
    except: display(HTML(f'<style>.container {{width: {size}% !important;}}</style>'))

def PlotlyNotebook():
    """
    Rendering plotly plots in notebooks.
    """
    import plotly.io as pio
    pio.renderers.default = 'notebook'
        
def Retina():
    """
    Rendering matplotlib plots in high resolution.
    """
    import matplotlib_inline
    matplotlib_inline.backend_inline.set_matplotlib_formats('retina')

def SideBySide(bool):
    """
    Displaying widgets horizontally when True
    """
    from IPython.display import display, HTML
    if bool==True: display(HTML("<style>.output {flex-direction: row;}</style>"))
    else: display(HTML("<style>.output {flex-direction: column;}</style>"))

