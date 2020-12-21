#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	pushd $REWRITER_WS_HOME
	supervisorctl -c $REWRITER_WS_HOME/ops/config/supervisord.conf stop all
	supervisorctl -c $REWRITER_WS_HOME/ops/config/supervisord.conf shutdown
	popd

	log "killed web-service daemon"
}

# Invoke entry point.
main
