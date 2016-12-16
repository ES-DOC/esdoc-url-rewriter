#!/bin/bash

# Import utils.
source $ESDOC_URL_REWRITER_HOME/sh/init.sh

# Main entry point.
main()
{
	supervisorctl -c $ESDOC_URL_REWRITER_HOME/ops/supervisord.conf stop all
	supervisorctl -c $ESDOC_URL_REWRITER_HOME/ops/supervisord.conf shutdown

	log "WEB : killed web-service daemon"
}

# Invoke entry point.
main
