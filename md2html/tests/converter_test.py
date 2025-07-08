from md2html.converter import md_to_html

def md_html_html_test():
    md_text = "Hello GSoC." \
    "This is **bold** and this is *italic*."

    html = md_to_html(md_text)
    

    assert "<strong>bold<strong>" in html
    assert "<em>italic<em>" in html