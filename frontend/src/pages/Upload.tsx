import React, { useState } from "react";
import Layout from "../components/Layout";

const Upload = () => {
  const [isDragging, setIsDragging] = useState<boolean>(false);

  const dragOverHandler = (e: React.DragEvent<Element>) => {
    e.preventDefault();
    setIsDragging(true);
  }

  const dropHandler = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setIsDragging(false);
    console.log(e)
  }

  return (
    <Layout>
      <div className="grow p-3 items-center flex justify-center">
        <div className="
          rounded-xl emboss p-5
          bg-gradient-to-b from-[#eee] to-white
        ">
          <h1 className="text-center font-medium text-xl m-0 p-0 mb-3">Upload Video</h1>
          <div className="rounded-xl h-32 deboss flex p-3 w-72">
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
            </div>
          </div>
        </div>
      </div>
    </Layout>
  )
}

export default Upload;