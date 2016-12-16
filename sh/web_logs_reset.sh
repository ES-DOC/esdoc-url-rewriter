#!/bin/bash

# Import utils.
source $ESDOC_URL_REWRITER_HOME/sh/init.sh

# Main entry point.
main()
{
	rm $ESDOC_URL_REWRITER_HOME/ops/*.log

	log "WEB : reset web-service logs"
}

# Invoke entry point.
main
