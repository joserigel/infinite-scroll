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
  UDTA = 'udta'
  DREF = 'dref'
  STSD = 'stsd'
  STTS = 'stts'
  STTS = 'ctts'
  STSC = 'stsc'
  STSZ = 'stsz'
  STCO = 'stco'
  MP4A = 'mp4a'
  ESDS = 'esds'

def bytes_to_arr(data):
  x_y = [
    int.from_bytes(data[i:i+2]) + int.from_bytes(data[i+2:i+4]) / 10 
    for i in range(0, 24, 4)
  ]
  z = [
    (int.from_bytes(data[i:i+1]) >> 6) + ((int.from_bytes(data[i:i+4]) & ~(3 << 30)) / (1 << 30)) 
    for i in range(24, 36, 4)
  ] 
  return [*x_y, *z]
    


def moov_to_json(data):
  offset = 0
  res = dict()
  while offset < len(data):
    size = int.from_bytes(data[offset + 0: offset + 4])
    box_type = data[offset + 4: offset + 8].decode('unicode_escape')
    chunk = data[offset + 8: offset + size]

    if box_type in [BoxTypes.TRAK, BoxTypes.MDIA, BoxTypes.MINF, BoxTypes.DINF, BoxTypes.STBL]:
      parsed = moov_to_json(chunk)
    elif box_type == BoxTypes.MVHD:
      parsed = {
        "version": int.from_bytes(chunk[0:1]),
        "flags": chunk[1:4].hex(),
        "creation_time": int.from_bytes(chunk[4:8]),
        "modification_time": int.from_bytes(chunk[8:12]),
        "timescale": int.from_bytes(chunk[12:16]),
        "duration": int.from_bytes(chunk[16:20]),
        "rate": int.from_bytes(chunk[20:22]) + int.from_bytes(chunk[22:24]) / (1 << 16),
        "volume": int.from_bytes(chunk[24:25]) + int.from_bytes(chunk[25:26]) / (1 << 1),
        "reserved": int.from_bytes(chunk[26:36]),
        "matrix": bytes_to_arr(chunk[36:72]),
        "pre_defined": int.from_bytes(chunk[72:96]),
        "next_track_ID": int.from_bytes(chunk[96:100])
      }
    elif box_type == BoxTypes.TKHD:
      parsed = {
        "version": int.from_bytes(chunk[0:1]),
        "flags": chunk[1:4].hex(),
        "creation_time": int.from_bytes(chunk[4:8]),
        "modification_time": int.from_bytes(chunk[8:12]),
        "track_id": int.from_bytes(chunk[12:16]),
        "reserved": int.from_bytes(chunk[16:20]),
        "duration": int.from_bytes(chunk[20:24]),
        "reserved": int.from_bytes(chunk[24:32]),
        "layer": int.from_bytes(chunk[32:34]),
        "alternate_group": int.from_bytes(chunk[34:36]),
        "volume": int.from_bytes(chunk[36:38]),
        "reserved": int.from_bytes(chunk[38:40]),
        "matrix": bytes_to_arr(chunk[40:76]),
        "width": int.from_bytes(chunk[76:80]),
        "height": int.from_bytes(chunk[80:84])
      }
    elif box_type == BoxTypes.MDHD:
      parsed = {
        "version": int.from_bytes(chunk[0:1]),
        "flags": chunk[1:4].hex(),
        "creation_time": int.from_bytes(chunk[4:8]),
        "modification_time": int.from_bytes(chunk[8:12]),
        "time_scale": int.from_bytes(chunk[12:16]),
        "duration": int.from_bytes(chunk[16:20]),
        "language": int.from_bytes(chunk[20:22]),
        "quality": int.from_bytes(chunk[22:24])
      }
    elif box_type == BoxTypes.HDLR:
      parsed = {
        "version": int.from_bytes(chunk[0:1]),
        "flags": chunk[1:4].hex(),
        "predefined": int.from_bytes(chunk[4:8]),
        "handler_type": int.from_bytes(chunk[8:12]),
        "reserved": int.from_bytes(chunk[12:24]),
        "name": chunk[24:].decode('unicode_escape').replace('\u0000', '')
      }
    elif box_type == BoxTypes.VMHD:
      parsed = {
        "version": int.from_bytes(chunk[0:1]),
        "flags": chunk[1:4].hex(),
        "graphics_mode": int.from_bytes(chunk[4:6]),
        "opcolor": int.from_bytes(chunk[6:12])
      }
    elif box_type == BoxTypes.SMHD:
      parsed = {
        "version": int.from_bytes(chunk[0:1]),
        "flags": chunk[1:4].hex(),
        "balance": int.from_bytes(chunk[4:6]),
        "reserved": int.from_bytes(chunk[6:8])
      }
    elif box_type == BoxTypes.DREF:
      entry_count = int.from_bytes(chunk[4:8])
      entries = []
      for i in range(entry_count):
        entries.append(chunk[8 + (i * 12): 20 + (i * 12)].decode('unicode_escape').replace('\u0000', ''))
      parsed = {
        "entries": entries
      }
    elif box_type == BoxTypes.MP4A:
      parsed = {
        "reserved": int.from_bytes(chunk[:6]),
        "data_reference_index": int.from_bytes(chunk[6:8]),
        "reserved": int.from_bytes(chunk[8:16]),
        "channel_count": int.from_bytes(chunk[16:18]),
        "sample_size": int.from_bytes(chunk[18:20]),
        "pre_defined": int.from_bytes(chunk[20:22]),
        "reserved": int.from_bytes(chunk[22:24]),
        "sample_rate": int.from_bytes(chunk[24:26]) + int.from_bytes(chunk[26:28]) / (1 << 16),
        "esds": moov_to_json(chunk[28:])["esds"]
      }
    elif box_type == BoxTypes.UDTA:
      parsed = chunk.decode('utf-8', 'ignore').replace('\u0000', '')
    elif box_type == BoxTypes.ESDS:
      
    elif box_type == BoxTypes.STSD:
      parsed = {
        "version": int.from_bytes(chunk[0:1]),
        "flags": chunk[1:4].hex(),
        "number_of_entires": int.from_bytes(chunk[4:8]),
        "sample_description_table": moov_to_json(chunk[8:])
      }
    else:
      parsed = "NOT IMPLEMENTED"

    if box_type not in res:
      res[box_type] = parsed
    elif isinstance(res[box_type], list):
      res[box_type].append(parsed)
    else:
      res[box_type] = [res[box_type], parsed]

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