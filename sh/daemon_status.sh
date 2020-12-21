#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	pushd $REWRITER_WS_HOME
	supervisorctl -c $REWRITER_WS_HOME/ops/config/supervisord.conf status all
	popd
}

# Invoke entry point.
main
