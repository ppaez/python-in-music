Using Python in music
=====================

Examples of audio and MIDI with Python.

The examples are being published in
the wiki at LinuxCabal:

https://wiki.cabal.mx/wiki/Python_en_la_música

Audio
=====

To run::
 python wsine.py
This produes the file `sine.raw`.  Each data
is 16-bit unsigned, with a sampling rate of
44,100Hz and a single channel.

To playback on the ALSA default PCM device::
 aplay -f U16 -r 44100 -c 1 sine.raw
