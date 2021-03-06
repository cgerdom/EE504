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


#ifndef INCLUDED_MYINTERLEAVER_INTERLEAVER_H
#define INCLUDED_MYINTERLEAVER_INTERLEAVER_H

#include <myinterleaver/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace myinterleaver {

    /*!
     * \brief <+description of block+>
     * \ingroup myinterleaver
     *
     */
    class MYINTERLEAVER_API interleaver : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<interleaver> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of myinterleaver::interleaver.
       *
       * To avoid accidental use of raw pointers, myinterleaver::interleaver's
       * constructor is in a private implementation
       * class. myinterleaver::interleaver::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace myinterleaver
} // namespace gr

#endif /* INCLUDED_MYINTERLEAVER_INTERLEAVER_H */

