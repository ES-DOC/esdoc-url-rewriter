#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	_install_ops_dir
	_install_config
	_install_venv
	log "web-service installed"
}

_install_ops_dir()
{
	mkdir -p $REWRITER_WS_HOME/ops
	mkdir -p $REWRITER_WS_HOME/ops/config
	mkdir -p $REWRITER_WS_HOME/ops/daemon
	mkdir -p $REWRITER_WS_HOME/ops/logs
	log "ops directory installed"
}

_install_config()
{
	cp $REWRITER_WS_HOME/resources/*.conf $REWRITER_WS_HOME/ops/config
}

_install_venv()
{
	pushd $REWRITER_WS_HOME
    pip2 install --upgrade pip
    pip2 install --upgrade pipenv
	pipenv install
}

# Invoke entry point.
main
