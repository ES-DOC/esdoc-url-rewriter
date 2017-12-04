# -*- coding: utf-8 -*-
"""
.. module:: documentation.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Documentation url factory.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from url_rewriter import handlers



def yield_urls():
    """Returns generator yielding supported URL patterns.

    """
    for project, doc_types in handlers.documentation.DOC_TYPES.items():
        yield r'/({0})'.format(project)
        for doc_type in doc_types:
            yield r'/({0})/({1})'.format(project, doc_type)
            yield r'/({0})/({1})/(.*)'.format(project, doc_type)
