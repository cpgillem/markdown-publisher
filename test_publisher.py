import publisher

def from_html_file():
    source_file = "~/Projects/markdown-publisher/source_test.md"
    print publisher.get_html_from_file(source_file)

def from_html():
    test_source = "# Test heading\n\n- test item 1\n- test item 2"
    print publisher.get_html(test_source)

def from_html_to_pdf():
    test_html = publisher.get_html(publisher.get_text_from_file("README.md"))
    test_pdf_filename = "test.pdf"
    print publisher.write_html_to_pdf(test_html, test_pdf_filename)

from_html_to_pdf()
