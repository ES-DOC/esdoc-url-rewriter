#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	supervisorctl -c $REWRITER_WS_HOME/ops/config/supervisord.conf status all
}

# Invoke entry point.
main
