#!/usr/bin/python

'''
Computer Club of WMU Markdown Publishing System
by cpg

This is a package that can be used to process any computer club documentation 
from markdown to one of the following formats:
- HTML with simple, built-in CSS
- Plain HTML
- PDF
- PNG? This would be for a flat, poster-style graphic
'''

import mistune
import pdfkit

def get_html(source, css=""):
    ''' Basic function for getting the HTML source for a string. '''
    return mistune.markdown(source)

def get_text_from_file(filename):
    ''' Gets the text from a file. If the file isn't found, return an empty 
        string. '''

    # Start with a default empty output string.
    source = ""
    
    # Try to read the file.
    try:
        with open(filename, 'r') as source_file:
            source = source_file.read()
    except:
        # Continue to use the empty string.
        print "%s not found." % filename

    return source

def write_text_to_file(source, filename):
    ''' Writes given text to a file. '''
    try:
        with open(filename, 'w') as destination_file:
            destination_file.write(source)
    except:
        print "Could not write to %s." % filename

def write_html_to_pdf(source, output_filename):
    ''' Writes HTML/CSS to a PDF file. '''
    print pdfkit.from_string(source, output_filename)
