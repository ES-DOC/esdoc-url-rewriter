#!/bin/bash

# Import utils.
source $ESDOC_URL_REWRITER_HOME/sh/init.sh

# Main entry point.
main()
{
	supervisorctl -c $ESDOC_URL_REWRITER_HOME/ops/supervisord.conf status all
}

# Invoke entry point.
main
