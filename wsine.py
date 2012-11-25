import sys
import math
from fractions import Fraction as F

f = open('sine.raw', 'wb')
f2 = open('sine', 'w')

def create_sine( frequency, amplitude=30000, duration=1000, sampleRate=44100 ):

    samplesPerCycle = F(sampleRate)/F(frequency)
    samples = samplesPerCycle.numerator
    cycles = samplesPerCycle.denominator

    print(frequency, 'cycles/s', sampleRate, 'samples/s:', \
        samples, 'samples for', cycles, 'cycles')

    ivalues = []
    values = []
    for sample in range( samples ):
        t = 2 * math.pi * sample / samplesPerCycle
        value = int( math.sin( t ) * amplitude )
        low_byte = value & 255
        high_byte = (value >> 8 ) & 255
        # print sample, t, value, high_byte, low_byte
        values.append( ( low_byte, high_byte ) )
        ivalues.append( value )

    repeat = int( sampleRate / samples * duration / 1000. )
    print('  repeat', repeat, 'times for one second.')
    for i in range( repeat ):
        for low_byte, high_byte in values:
            f.write( bytes( (low_byte, high_byte) ) )
        for value in ivalues:
            f2.write( str(value) + '\n' )


create_sine( 10, amplitude=30000 )
create_sine( 100, amplitude=30000 )
create_sine( 200, amplitude=30000 )
create_sine( 300, amplitude=30000 )
create_sine( 333, amplitude=30000 )
create_sine( 1000, amplitude=30000 )
create_sine( 2000, amplitude=30000 )
create_sine( 3000, amplitude=30000 )
create_sine( 4000, amplitude=30000 )
create_sine( 5000, amplitude=30000 )
create_sine( 440, amplitude=30000, duration=500 )
create_sine( 880, amplitude=30000, duration=500 )
create_sine( 1320, amplitude=30000, duration=500 )
create_sine( 880, amplitude=30000, duration=500 )
create_sine( 440, amplitude=30000, duration=500 )
create_sine( 880, amplitude=30000, duration=500 )
create_sine( 440, amplitude=30000, duration=1000 )
