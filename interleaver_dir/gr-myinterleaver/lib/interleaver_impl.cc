/* -*- c++ -*- */
/* 
 * Copyright 2018 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "interleaver_impl.h"

namespace gr {
  namespace myinterleaver {

    interleaver::sptr
    interleaver::make()
    {
      return gnuradio::get_initial_sptr
        (new interleaver_impl());
    }

    /*
     * The private constructor
     */
    interleaver_impl::interleaver_impl()
      : gr::block("interleaver",
              gr::io_signature::make(2, 2, sizeof(int)),
              gr::io_signature::make(1, 1, sizeof(int)))
    {}

    /*
     * Our virtual destructor.
     */
    interleaver_impl::~interleaver_impl()
    {
    }

    void
    interleaver_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
      ninput_items_required[0] = noutput_items/2;
    }

    int
    interleaver_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const int *in1 = (const int *) input_items[0];
      const int *in2 = (const int *) input_items[1];
      const int *out = (const int *) output_items[0];

      for (int i=0; i < noutput_items, i += 2) {
        out[i] = in1[i/2]
        if (i+1 < noutput_items) {
          out[i+1] = in2[i/2]
        }
      }

      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items/2);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace myinterleaver */
} /* namespace gr */

