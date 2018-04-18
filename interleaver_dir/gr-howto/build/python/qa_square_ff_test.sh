#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/c/Documents/EE504/EE504/interleaver_dir/gr-howto/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/c/Documents/EE504/EE504/interleaver_dir/gr-howto/build/python:$PATH
export LD_LIBRARY_PATH=/home/c/Documents/EE504/EE504/interleaver_dir/gr-howto/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/c/Documents/EE504/EE504/interleaver_dir/gr-howto/build/swig:$PYTHONPATH
/usr/bin/python2 /home/c/Documents/EE504/EE504/interleaver_dir/gr-howto/python/qa_square_ff.py 
