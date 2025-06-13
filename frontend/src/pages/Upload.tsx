import React, { useState } from "react";
import Layout from "../components/Layout";
import { splitMP4Semantically } from "../utils/parser";

const Upload = () => {
  const [isDragging, setIsDragging] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>("");

  const dragOverHandler = (e: React.DragEvent<Element>) => {
    e.preventDefault();
    setIsDragging(true);
  }

  const dropHandler = async (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setIsDragging(false);
    setError("");
    setLoading(true);
    try {
      const files = e.dataTransfer.files
      if (files.length !== 1) {
        throw new Error("Only 1 file at a time is supported!")
      }

      const file = files[0];
      const chunks = await splitMP4Semantically(file);
    } catch (e: any) {
      setError(e.message ?? String(e));
    }
  }

  return (
    <Layout>
      <div className="grow p-3 items-center flex justify-center">
        <div className="
          rounded-xl emboss p-5 flex flex-col gap-3
          bg-gray-200
        ">
          <h1 className="text-center font-medium text-xl m-0 p-0">Upload Video</h1>
          <div className="rounded-xl h-32 deboss flex p-3 w-72">
            { !loading ? 
              <div 
                onDragOver={(e) => dragOverHandler(e)} 
                onDragLeave={() => setIsDragging(false)}
                onDrop={(e) => dropHandler(e)}
                className={`
                  grow rounded-md flex justify-center items-center
                  border-2 border-gray-400
                  ${ isDragging ? "border-solid" : "border-dashed" }
                `}>
                  <h1 className="text-gray-400 text-center">Click or drag your video file over</h1>
              </div> :
              <div className="[border:2px_solid_red] grow flex items-center justify-center">
                <div className="h-10 w-10 bg-red-500 rounded-tl-full rounded-tr-full"/>
              </div>
            }
          </div>
          <label className="text-red-600 font-medium">{error}</label>
        </div>
      </div>
    </Layout>
  )
}

export default Upload;