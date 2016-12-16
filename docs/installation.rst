Installing
------------------------------

**Step 1: Download source code from GitHub**

```
cd YOUR_WORKING_DIRECTORY
git clone https://github.com/ES-DOC/esdoc-ws-url-rewriter.git
```

**Step 2: Edit your .bash_rc settings**

```
export ESDOC_URL_REWRITER_HOME=YOUR_WORKING_DIRECTORY/esdoc-ws-url-rewriter
```

```
export PYTHONPATH=$PYTHONPATH:$ESDOC_URL_REWRITER_HOME
```

```
source $ESDOC_URL_REWRITER_HOME/sh/activate
```
