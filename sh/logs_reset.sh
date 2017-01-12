#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	rm $REWRITER_WS_HOME/ops/logs/*.log

	log "logs reset"
}

# Invoke entry point.
main
