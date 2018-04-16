from pydub import AudioSegment
from typing import List, Any, Union


def remove_silence(sound, silence_threshold=-30.0, chunk_size=10):
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
    short_sound = AudioSegment.empty()  # type: List[Union[int, Any]]
    while (index + chunk_size) < len(sound):
        index += chunk_size

        if sound[index:index + chunk_size].dBFS > silence_threshold:
            short_sound.extend(sound[index:index + chunk_size])

    return short_sound


soundin = AudioSegment.from_file("~/Desktop/acarsTest.wav", format="wav")

new_sound = remove_silence(soundin)

file_handle = new_sound.export("~/Desktop/acarsShort.wav", format="wav")
