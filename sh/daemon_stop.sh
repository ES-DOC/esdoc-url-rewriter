#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	supervisorctl -c $REWRITER_WS_HOME/ops/config/supervisord.conf stop all
	supervisorctl -c $REWRITER_WS_HOME/ops/config/supervisord.conf shutdown

	log "killed web-service daemon"
}

# Invoke entry point.
main
