#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	# Create backups.
	cp $REWRITER_WS_HOME/ops/config/supervisord.conf $REWRITER_WS_HOME/ops/config/supervisord-backup.conf
	cp $REWRITER_WS_HOME/ops/config/ws.conf $REWRITER_WS_HOME/ops/config/ws-backup.conf

	# Update.
	cp $REWRITER_WS_HOME/resources/supervisord.conf $REWRITER_WS_HOME/ops/config
	cp $REWRITER_WS_HOME/resources/ws.conf $REWRITER_WS_HOME/ops/config

	log "configuration files updated"
}

# Invoke entry point.
main
