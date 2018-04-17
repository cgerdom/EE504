/* -*- c++ -*- */

#define MYINTERLEAVER_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "myinterleaver_swig_doc.i"

%{
#include "myinterleaver/interleaver.h"
#include "myinterleaver/deinterleaver.h"
%}


%include "myinterleaver/interleaver.h"
GR_SWIG_BLOCK_MAGIC2(myinterleaver, interleaver);
%include "myinterleaver/deinterleaver.h"
GR_SWIG_BLOCK_MAGIC2(myinterleaver, deinterleaver);
