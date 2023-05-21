import re

ITALICS = re.compile(r'<em>(.+?)</em>')
SPACES = re.compile(r'\s+')
PARAGRAPHS = re.compile(r'<p>(.+?)</p>')
LINKS = re.compile(r'<a href="(.+?)">(.+?)</a>')

def html2markdown(html):
    '''Take in html text as input and return markdown'''
    markdown = ITALICS.sub(r'*\1*', html)
    markdown = SPACES.sub(r' ', markdown)
    markdown = PARAGRAPHS.sub(r'\n\n\1', markdown)
    markdown = LINKS.sub(r'[\2](\1)', markdown)
    return markdown.strip()