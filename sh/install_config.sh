#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	cp $REWRITER_WS_HOME/resources/template-supervisord.conf $REWRITER_WS_HOME/ops/config/supervisord.conf
	cp $REWRITER_WS_HOME/resources/template-ws.conf $REWRITER_WS_HOME/ops/config/ws.conf

	log "configuration files initialized"
}

# Invoke entry point.
main
