Using Python in music
=====================

Examples of audio and MIDI with Python 3.

The examples are being published in
the wiki at LinuxCabal:

https://wiki.cabal.mx/wiki/Python_en_la_música

Audio
=====
`wsine.py` has a simple function that generates
a sine wave at a given frequency, with a specified
sampling rate, for a certain duration.

The data is stored in a simple file that can be
reproduced with a standard audio player.

To run::

 python3 wsine.py

This produces the file `sine.raw`.  Each data
is 16-bit signed little endian, with a sampling
rate of 44,100Hz and a single channel (mono).

To playback on the ALSA default PCM device::

 aplay -f S16 -r 44100 -c 1 sine.raw

The meaning of the options:
 - -f = format
 - -r = sampling rate
 - -c = channels
