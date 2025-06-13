interface MP4Chunk {
  type: string;
  size: number;
  buffer: ArrayBuffer;
}

export async function splitMP4Semantically(file: File) {
  if (file.type !== "video/mp4") {
    throw new Error("Only video/mp4 is supported!");
  }

  let i = 0;
  const chunks: MP4Chunk[] = [];
  while (i < file.size) {
    const size = new DataView(await file.slice(i, i+4).arrayBuffer()).getUint32(0);
    const type = await file.slice(i + 4, i + 8).text();
    chunks.push({
      type: type,
      size: size,
      buffer: await file.slice(i, i + size).arrayBuffer()
    });
    i += size;
  }

  return chunks;
}