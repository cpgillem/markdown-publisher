import publisher

test_pdf_filename = "test/test.pdf"
test_css_filename = "test/test.css"
test_md_filename = "test/test.md"
test_html_filename = "test/test.html"

test_md = "# Test heading\n\n- test item 1\n- test item 2"

def from_html_file():
    print publisher.md_to_html(publisher.from_file(test_md_filename))

def md_to_html():
    print publisher.md_to_html(test_source)

def md_and_css_to_html():
    html_source = publisher.md_and_css_to_html(publisher.from_file(test_md_filename),
        publisher.from_file(test_css_filename))
    print html_source
    publisher.to_file(html_source, test_html_filename)

def from_md_file_to_pdf_file():
    test_html = publisher.md_to_html(publisher.from_file("README.md"))
    print publisher.html_to_pdf_file(test_html, test_pdf_filename, [test_css_filename])

md_and_css_to_html()
