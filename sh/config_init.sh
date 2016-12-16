#!/bin/bash

# Import utils.
source $ESDOC_URL_REWRITER_HOME/sh/init.sh

# Main entry point.
main()
{
	cp $ESDOC_URL_REWRITER_HOME/templates/template-supervisord.conf $ESDOC_URL_REWRITER_HOME/ops/supervisord.conf
	cp $ESDOC_URL_REWRITER_HOME/templates/template-ws.conf $ESDOC_URL_REWRITER_HOME/ops/ws.conf

	log "WEB : initialized web-service configuation"
}

# Invoke entry point.
main
