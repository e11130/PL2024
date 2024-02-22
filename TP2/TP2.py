#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dario
#
# Created:     18/02/2024
# Copyright:   (c) dario 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re

#archivo que pasa un texto en MArkDown a HTML


def markdown_to_html(texto_md):
    #headings
    texto_md = re.sub(r'# (.+)', r'<h1>\1</h1>', texto_md)
    texto_md = re.sub(r'## (.+)', r'<h2>\1</h2>', texto_md)
    texto_md = re.sub(r'### (.+)', r'<h3>\1</h3>', texto_md)

    #negrita
    texto_md = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', texto_md)

    #curaiva
    texto_md = re.sub(r'\*(.+?)\*', r'<i>\1</i>', texto_md)

    #lista enumerada
    texto_md = re.sub(r'\n(\d+\..+)', r'\n<ol>\n\1\n</ol>', texto_md)
    texto_md = re.sub(r'\n(\d+\..+?)\n\n', r'\n<ol>\n\1\n</ol>\n', texto_md)

    #links
    texto_md = re.sub(r'\[([^]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', texto_md)

    #imagenes
    texto_md = re.sub(r'!\[([^]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', texto_md)

    return texto_md
