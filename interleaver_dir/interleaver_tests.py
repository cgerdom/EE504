from gnuradio import gr, gr_unittest
from gnuradio import blocks
import interleaver
import sys

yellow = '\033[93m'
red = '\033[91m'

class interleaver_test_class(gr_unittest.TestCase):

	def setup(self):
		self.tb = gr.top_block()

	def tearDown (self):
		self.tb = None

	def test_1(self):
		#TODO
		src_data = (3, 4, 0, 0, -1, -1, -2, -1, -1, -2, -65537, -1, -1, -65537)
		expected_result = (37, 0, 0, 0, -1, -1, -2, -1, -3, -1, -1, -65537, -1, -131073)
		print_src_list(src_data)

		src = blocks.vector_source_f(src_data)
		inter = interleaver.interleaver()
		dst = blocks.vector_sink_f()

		self.tb.connect(src, inter)
		self.tb.connect(inter, dst)
		self.tb.run()

		result_data = dst.data()
		print_result_list(result_data)
		self.assertEqual(expected_result, result_data, 6)

def print_src_list(arr):
	count = 0
	for val in arr:
		if count % 2 == 0:
			print_src_num(val, yellow)
		else:
			print_src_num(val, red)
		count += 1

def print_result_list(arr):
	count = 0
	for val in arr:
		print_colored_bits(val)

def print_src_num(num, color):
	string = ''
	if num < 0:
		if num & 1 == 1:
			string = '1'
		else:
			string = '0'
		num = num >> 1
		num &= sys.maxint

	while num:
		if num & 1 == 1:
			string = '1' + string
		else:
			string = '0' + string
		num = num >> 1

	for _ in range(32-len(string)):
		string = '0' + string

	print color + string + '\033[0m'

def print_colored_bits(num):
	count = 0
	string = ""
	if num < 0:
		if num & 1 == 1:
			string = yellow + '1' + '\033[0m'
		else:
			string = yellow + '0' + '\033[0m'
		num = num >> 1
		num &= sys.maxint
		count = 1

	while num:
		val = '0'
		if num & 1 == 1:
			val = '1'

		if count % 2 == 0:
			string = yellow + val + '\033[0m' + string # print first array's bit in yellow
		else:
			string = red + val + '\033[0m' + string # print second array's bit in red

		num = num >> 1
		count += 1

	for i in range(count, 32):
		if i % 2 == 0:
			string = yellow + '0' + '\033[0m' + string # print first array's bit in yellow
		else:
			string = red + '0' + '\033[0m' + string # print second array's bit in red

	print string

if __name__ == '__main__':
	gr_unittest.run(interleaver_test_class, "interleaver_test_class.xml")