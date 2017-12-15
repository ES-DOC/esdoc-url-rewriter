# -*- coding: utf-8 -*-
"""
.. module:: further_info.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Further info url factory.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyessv import vocabs



def yield_urls():
	"""Returns generator yielding supported URL patterns.

	"""
	for url in _yield_cmip6():
		yield url


def _yield_cmip6():
	"""Yields valid CMIP6 urls.

	NOTE 1: CMIP6 global attributes are defined here: http://goo.gl/v1drZl
	NOTE 2: Normative form: mip_era.institution_id.source_id.experiment_id.sub_experiment_id.variant_label

	"""
	# Set pointer to CMIP6 vocabs accessor.
	cmip6 = vocabs.wcrp.cmip6

	# Yield URL's based upon vocab canonical or raw names.
	for source in cmip6.source_id:
		for institution in [cmip6.institution_id[i] for i in source.institution_id]:
			for experiment in cmip6.experiment_id:
				for sub_experiment_id in experiment.sub_experiment_id:
					for field in {'canonical_name', 'raw_name'}:
						yield r'/{}.{}.{}.{}.{}.{}'.format(
							'cmip6' if field == 'canonical_name' else 'CMIP6',
							getattr(institution, field),
							getattr(source, field),
							getattr(experiment, field),
							sub_experiment_id,
							cmip6.ensemble.term_regex
							)
