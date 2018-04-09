from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter as filt
from gnuradio import gr
import osmosdr

class fm_rx(gr.top_block):
	def __init__(self, station):

		gr.top_block.__init__(self, "FM Receiver")
		self.samp_rate = 2e6

		self.audio_sink = audio.sink(self.samp_rate, "", True)

		self.usrp_source = osmosdr.source(args="numchan=1")
		self.usrp_source.set_sample_rate(self.samp_rate)
		self.usrp_source.set_center_freq(station*1e6, 0)
		self.usrp_source.set_freq_corr(0, 0)
		self.usrp_source.set_dc_offset_mode(0, 0)
		self.usrp_source.set_iq_balance_mode(0, 0)
		self.usrp_source.set_gain_mode(False, 0)
		self.usrp_source.set_gain(10, 0)
		self.usrp_source.set_if_gain(20, 0)
		self.usrp_source.set_bb_gain(20, 0)
		self.usrp_source.set_antenna("", 0)
		self.usrp_source.set_bandwidth(0, 0)

		#self.rational_resampler = filt.rational_resampler_base_ccc(192e3, 25e4, None)
		self.rational_resampler = filt.rational_resampler_ccc(interpolation=48e4, decimation=2e5, taps=None, fractional_bw=None)
		self.filter = filt.fir_filter_ccf(1, filt.firdes.low_pass(1, self.samp_rate, 1e5, 1e6, filt.firdes.WIN_HAMMING, 6.76))
		self.wbfm_rcv = analog.wfm_rcv(quad_rate=48e4, audio_decimation=10)


		self.connect(self.usrp_source, self.filter)
		self.connect(self.filter, self.rational_resampler)
		self.connect(self.rational_resampler, self.wbfm_rcv)
		self.connect(self.wbfm_rcv, self.audio_sink)

	def get_samp_rate(self):
		return self.samp_rate

if __name__ == '__main__':
	station = argv[1]
	radio = fm_rx(station)
	try:
		radio.run()
	except [[KeyboardInterrupt]]:
		pass
