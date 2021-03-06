"""Prettify HTML with BeautifulSoup.

Primarily manages indentation.

"""

from sakura.common import ini
from bs4 import BeautifulSoup
import os


SAKURA_ARGS = ['document', 'document_path']
REPLACE_ALL = True


def pretty(document, document_path):
    """Prettify HTML source..."""

    __, file_extension = os.path.splitext(document_path)

    if file_extension not in ('.html', '.htm'):
        return document

    soup = BeautifulSoup(document)
    soup = soup.prettify()
    return str(soup.encode('utf-8'))

