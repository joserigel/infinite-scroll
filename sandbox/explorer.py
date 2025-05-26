import sys
import json

class BoxTypes:
  FTYP = 'ftyp'
  FREE = 'free'
  MOOV = 'moov'
  MDAT = 'mdat'
  UUID = 'uuid'
  MVHD = 'mvhd'
  TRAK = 'trak'
  TKHD = 'tkhd'
  MDIA = 'mdia'
  MDHD = 'mdhd'
  HDLR = 'hdlr'
  MINF = 'minf'
  VMHD = 'vmhd'
  SMHD = 'smhd'
  DINF = 'dinf'
  STBL = 'stbl'
  STSD = 'stsd'
  STTS = 'stts'
  STSC = 'stsc'
  STSZ = 'stsz'
  STCO = 'stco'
  CO64 = 'co64'

def bytes_to_arr(data):
  x_y = [
    int.from_bytes(data[i:i+2]) + int.from_bytes(data[i+2:i+4]) / 10 
    for i in range(0, 32, 4)
  ]
  z = 
  return x_y
    


def moov_to_json(data):
  offset = 0
  res = dict()
  while offset < len(data):
    size = int.from_bytes(data[offset + 0: offset + 4])
    box_type = data[offset + 4: offset + 8].decode('unicode_escape')
    chunk = data[offset + 8: offset + size]
    if box_type in [BoxTypes.TRAK, BoxTypes.MDIA, BoxTypes.MINF, BoxTypes.STBL]:
      res[box_type] = moov_to_json(chunk)
    elif box_type == BoxTypes.MVHD:
      res[box_type] = {
        "version": int.from_bytes(chunk[0:1]),
        "flags": chunk[1:4].hex(),
        "creation_time": int.from_bytes(chunk[4:8]),
        "modification_time": int.from_bytes(chunk[8:12]),
        "timescale": int.from_bytes(chunk[12:16]),
        "duration": int.from_bytes(chunk[16:20]),
        "rate": int.from_bytes(chunk[20:22]) + int.from_bytes(chunk[22:24]) / 100,
        "volume": int.from_bytes(chunk[24:25]) + int.from_bytes(chunk[25:26]) / 10,
        "reserved": int.from_bytes(chunk[26:36]),
        "matrix": bytes_to_arr(chunk[36:72]),
        "pre_defined": int.from_bytes(chunk[72:96]),
        "next_track_ID": int.from_bytes(chunk[96:100])
      }
    else:
      res[box_type] = "NOT IMPLEMENTED"
    offset += size
  return res
  
  

def decode_by_type(box_type, data):
  if box_type == BoxTypes.MOOV:
    with open("moov.json", "w") as f:
      f.write(json.dumps(moov_to_json(data)))

def explore(file: str):
  with open(file, 'rb') as f:
    while True:
      # Get initial size
      size = f.read(4)
      if size == b'':
        return

      # Decode size as int
      size = int.from_bytes(size)
      
      # Get box type
      box_type = f.read(4).decode('unicode_escape')

      # Get data
      data = f.read(size - 8)

      decode_by_type(box_type, data)
      
      
if __name__ == '__main__':
  file = sys.argv[1]
  if file.endswith('.mp4'):
    explore(file)
  else:
    print(f'Error: {file} must be a valid .mp4 file')