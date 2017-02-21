#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	source $REWRITER_WS_HOME/sh/daemon_stop.sh
	source $REWRITER_WS_HOME/sh/daemon_start.sh
	sleep 3.0
	source $REWRITER_WS_HOME/sh/daemon_status.sh
}

# Invoke entry point.
main
