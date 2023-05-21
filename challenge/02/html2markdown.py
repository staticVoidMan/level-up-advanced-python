import re

def html2markdown(html):
    '''Take in html text as input and return markdown'''
    html = re.sub(r"</?em>", "*", html)
    html = re.sub(r"\s+", " ", html)
    html = re.sub(r"<p>", "\n\n", html).strip()
    html = re.sub(r"</p>", "", html)
    html = re.sub(r'<a href="(.+?)">(.+?)</a>', r"[\2](\1)", html)
    return html