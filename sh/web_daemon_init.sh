#!/bin/bash

# Import utils.
source $ESDOC_URL_REWRITER_HOME/sh/init.sh

# Main entry point.
main()
{
	source $ESDOC_URL_REWRITER_HOME/sh/web_logs_reset.sh
	supervisord -c $ESDOC_URL_REWRITER_HOME/ops/supervisord.conf

	log "WEB : initialized web-service daemon"
}

# Invoke entry point.
main
