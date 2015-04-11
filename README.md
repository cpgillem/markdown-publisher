# Markdown Publisher for CCaWMU

This is a little project to provide automated publishing capabilities for the Computer Club at WMU as well as anyoneelse interested. The goals of this module in order:

1. Provide professional and aesthetically pleasing publications for CCaWMU
1. Allow these publications to take on any form (PDF, email, blog post, etc.)
1. Allow as much freedom as possible in the design, font, and color choices
1. Require as little effort as possible in generating individual publications

# Packages Used

- [mistune](https://github.com/lepture/mistune) for parsing Markdown syntax into HTML
- [wkhtmltopdf](http://wkhtmltopdf.org/) for converting HTML and CSS to PDF documents
- [pdfkit](https://pypi.python.org/pypi/pdfkit), a Python package that uses wkhtmltopdf 

# Design Decisions

## publisher module

This module provides functions for reading and writing text from files and converting that text across formats.

### Functions

*This module is a work in progress but this is a general list of what will be implemented.*

- Writing text to a file
- Reading text from a file
- Converting a markdown string to an HTML string 
- Converting a markdown string to an HTML string with inline CSS
  - This will use a custom mistune Renderer.
  - This will be used in emails.
- Converting an HTML string and a CSS string to PDF
  - This should also take advantage of a TOC and other metadata.
