#include <gr_block.h>
using namespace gr;

class interleaver : public gr_block {
public:
	interleaver_impl::interleaver_impl()
		: gr::block("interleaver", gr::io_signature::make(2, 2, sizeof (int)), gr::io_signature::make(1, 1, sizeof (int) * 2)) 
	{

	}

	void interleaver_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
	{
		ninput_items_required[0] = noutput_items/2;
	}

	int interleaver_impl::general_work(int noutput_items,
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

		consume_each(0, noutput_items/2);
		consume_each(1, noutput_items/2);
		return noutput_items;
	}
}