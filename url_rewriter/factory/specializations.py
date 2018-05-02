# -*- coding: utf-8 -*-
"""
.. module:: specializations.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Specializations url factory.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from url_rewriter import handlers



def yield_urls():
    """Returns generator yielding supported URL patterns.

    """
    for project, topics in handlers.specializations.PROJECTS.items():
        yield r'/({0})'.format(project)
        for topic in topics:
            yield r'/({0})/({1})'.format(project, topic)
