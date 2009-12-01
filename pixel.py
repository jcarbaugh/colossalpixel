#!/usr/bin/env python
from array import array
import struct
import zlib

def render_png(rgb):
    
    # png header and standard chunks

    PNG_HEADER = '\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
    IHDR_CHUNK = '\x00\x00\x00\x0D\x49\x48\x44\x52\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90\x77\x53\xDE'
    IEND_CHUNK = '\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82'
    
    # parse rgb color
    
    if rgb.startswith('#'):
        rgb = rgb[1:]
    
    if len(rgb) == 3:
        r,g,b = (int(c, 16) << 4 for c in rgb)
    elif len(rgb) == 6:
        r,g,b = (int(rgb[:2], 16), int(rgb[2:4], 16), int(rgb[4:], 16))

    # generate one pixel scanline

    scanline = array('B')
    scanline.extend((0,r,g,b))
    
    # create IDAT chunk
    
    idat_data = zlib.compress(scanline.tostring())

    idat_chunk = struct.pack("!I", len(idat_data))
    idat_chunk += 'IDAT' + idat_data
    idat_chunk += struct.pack("!i", zlib.crc32(idat_data, zlib.crc32('IDAT')))

    # build png

    png = PNG_HEADER + IHDR_CHUNK + idat_chunk + IEND_CHUNK
    
    return png

if __name__ == '__main__':
    import sys
    png = render_png('f2d')
    sys.stdout.write(png)
    
