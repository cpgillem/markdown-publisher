# Markdown Publisher for CCaWMU

This is a little project to provide automated publishing capabilities for the Computer Club at WMU as well as anyone else interested. The goals of this module in order:

1. Provide professional and aesthetically pleasing publications for CCaWMU
1. Allow these publications to take on any form (PDF, email, blog post, etc.)
1. Allow as much freedom as possible in the design, font, and color choices
1. Require as little effort as possible in generating individual publications

# Packages Used

- [mistune](https://github.com/lepture/mistune) for parsing Markdown syntax into HTML
- [wkhtmltopdf](http://wkhtmltopdf.org/) for converting HTML and CSS to PDF documents
- [pdfkit](https://pypi.python.org/pypi/pdfkit), a Python package that uses wkhtmltopdf 

# API Reference

## publisher Module

- function **from_file(filename)**: Reads the text content of a file. This can be markdown, HTML, CSS, or anything else.
  - **filename**: filename to read from with path
- function **to_file(source, filename)**: Writes text to a file, overwriting any data.
  - **source**: Text to write to the file.
- function **md_to_html(source_md, source_css)**: Takes markdown syntax with CSS formatting and turns it into HTML. 
  - **source_md**: Markdown syntax to convert
  - **source_css**: Optional CSS to put into the HTML output. If this is specified, a style tag is inserted before the HTML.
- function **css_to_html_tag(source_css)**: Takes CSS and turns it into an HTML style tag.
  - **source_css**: CSS styling
- function **html_to_pdf_file(source_html, output_pdf_filename, source_css_filename)**: Uses pdfkit to create a PDF file out of HTML with optional CSS.
  - **source_html**: The HTML source of the file
  - **output_pdf_filename**: Filename of the destination PDF
  - **source_css_filename**: Filename of the CSS source file if it is necessary. If not specified, the PDF will be plain HTML.
- function **md_to_html_email(source_md, source_css)**: Creates an HTML email out of markdown source with optional CSS formatting. This function will create a Python email object with a MIME HTML attachment as well as a plaintext attachment containing the original Markdown, as a fallback. **returns a Python MIMEMultipart object.**
  - **source_md**: Markdown source to put in the email.
  - **source_css**: CSS to apply to the HTML document. This will be embedded into the page. **Optional**. If not specified, there will be no CSS.
- function **pdf_file_to_pdf_attachment(source_pdf_filename)**: Creates a Python MIMEBase object out of an existing PDF file for attaching to emails. This object will be sent as a PDF attachment. **returns a Python MIMEBase object.**
