#!/usr/bin/python

'''
Computer Club of WMU Markdown Publishing System
by cpg

This is a module that can be used to process any computer club documentation 
from markdown to one of the following formats:
- HTML with simple, built-in CSS
- Plain HTML
- PDF
- PNG? This would be for a flat, poster-style graphic
'''

import mistune
import pdfkit

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def from_file(filename):
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

def to_file(source, filename):
    ''' Writes given text to a file. '''
    try:
        with open(filename, 'w') as destination_file:
            destination_file.write(source)
    except:
        print "Could not write to %s." % filename

def md_to_html(source_md, source_css=""):
    ''' Basic function for getting the HTML source for a string. 
		If some css is given, adds that to the beginning as a <style> tag. '''
    html_output = mistune.markdown(source_md)
	if len(source_css > 0):
		html_output = css_to_html_tag + html_output

	return html_output

def css_to_html_tag(source_css):
    ''' Gets an HTML tag for inline CSS formatting from some basic CSS. '''
    return '<style type="text/css">%s</style>' % source_css

def html_to_pdf_file(source_html, output_html_filename, source_css_filename):
    ''' Writes HTML/CSS to a PDF file. 
        Uses one CSS file for simplicity. This is passed on as a single item 
        list. '''
    pdfkit.from_string(source_html, output_html_filename, css=source_css_filename)

def html_to_email(source_html, attachments=[]):
	''' Puts HTML (assuming with inline CSS if necessary) into an email message. '''
	
