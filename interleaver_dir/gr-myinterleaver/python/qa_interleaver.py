#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr, gr_unittest
from gnuradio import blocks, atsc
import myinterleaver_swig as myinterleaver

class qa_interleaver (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
		src_data1 = (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 20.5)
		src_data2 = (8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 18.3)
		expected_result = (1.0, 8.0, 2.0, 9.0, 3.0, 10.0, 4.0, 11.0, 5.0, 12.0, 6.0, 13.0, 7.0, 14.0, 20.5, 18.3)
		src1 = blocks.vector_source_f(src_data1)
		src2 = blocks.vector_source_f(src_data2)
		inter = myinterleaver.interleaver()
		dst = blocks.vector_sink_f()
		self.tb.connect(src1, (inter, 0))
		self.tb.connect(src2, (inter, 1))
		self.tb.connect(inter, dst)
		self.tb.run()
		result_data = dst.data()
		self.assertFloatTuplesAlmostEqual(expected_result, result_data, 4)

		inter = myinterleaver.interleaver()
		src = blocks.vector_source_f(result_data)
		dst = blocks.vector_sink_f()
		deinter = myinterleaver.deinterleaver()
		dst2 = blocks.vector_sink_f()

		self.tb.connect(src, deinter)
		self.tb.connect((deinter, 0), (dst, 0))
		self.tb.connect((deinter, 1), (dst2, 0))
		self.tb.run()

		result_data1 = dst.data()
		result_data2 = dst2.data()
		print result_data1
		print result_data2
		self.assertFloatTuplesAlmostEqual(src_data1, result_data1, 4)
		self.assertFloatTuplesAlmostEqual(src_data2, result_data2, 4)

if __name__ == '__main__':
    gr_unittest.run(qa_interleaver, "qa_interleaver.xml")
