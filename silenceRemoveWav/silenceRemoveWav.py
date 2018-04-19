from pydub import AudioSegment


def remove_silence(sound, silence_threshold=-20.0, chunk_size=100):
    '''
    :param sound:
    :param silence_threshold: in dB
    :param chunk_size: in ms
    :return:returns the sound without silence

    method
    read each chunk if it is noise append it to the output
    '''

    assert chunk_size > 0
    index = 0
    short_sound = AudioSegment.empty()
    while (index + chunk_size) < len(sound):

        if sound[index:(index + chunk_size)].dBFS > 6.03:  # silence_threshold based on observed wav file silence
            short_sound = short_sound.append(sound[index:(index + chunk_size)], crossfade=0)
            #short_sound = short_sound.append(AudioSegment.silent(duration=1000), crossfade=0)

        index += chunk_size
        print('working on chunk ' + repr(index) + ' of ' +repr(len(sound)) + ' ms')

    return short_sound


sound_in = AudioSegment.from_file("acarsNew.wav", format="wav")

new_sound = remove_silence(sound_in)

file_handle = new_sound.export("acarsShort1347.wav", format="wav")

file_handle2 = sound_in.export("test.wav", format="wav")
