# -*- coding: utf-8 -*-
"""

.. module:: constants.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC Errata - web-service constants.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# HTTP CORS header.
HTTP_HEADER_Access_Control_Allow_Origin = "Access-Control-Allow-Origin"

# Rewriter type: documentation.
REWRITER_TYPE_DOCUMENTATION = 'doc'

# Rewriter type: further infor url.
REWRITER_TYPE_FURTHER_INFO = 'fi'

# Rewriter type: specializations.
REWRITER_TYPE_SPECIALIZATIONS = 'specs'

# Set of rewriter types.
REWRITER_TYPE = {
	REWRITER_TYPE_DOCUMENTATION,
	REWRITER_TYPE_FURTHER_INFO,
	REWRITER_TYPE_SPECIALIZATIONS
}
