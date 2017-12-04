# -*- coding: utf-8 -*-
"""
.. module:: further_info.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Further info url factory.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import pyessv



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
	for source in pyessv.load('wcrp:cmip6:source-id'):
		for institution_id in source.data['institution_id']:
			institution = pyessv.load('wcrp:cmip6:institution-id:{}'.format(institution_id))
			for experiment in pyessv.load('wcrp:cmip6:experiment-id'):
				for sub_experiment_id in [i for i in experiment.data['sub_experiment_id']]:
					for field in {'canonical_name', 'raw_name'}:
						yield r'/{}.{}.{}.{}.{}.r[0-9]i[0-9]p[0-9]f[0-9]'.format(
							'cmip6' if field == 'canonical_name' else 'CMIP6',
							getattr(institution, field),
							getattr(source, field),
							getattr(experiment, field),
							sub_experiment_id
							)
