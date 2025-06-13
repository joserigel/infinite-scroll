import React from "react";
import Layout from "../components/Layout";
import { Button } from "../components/Button";
import { AiFillLike, AiFillDislike } from "react-icons/ai";
import { FaChevronUp } from "react-icons/fa";



const Index = () => {
  return (
    <Layout>
      <div className="flex flex-col p-5 grow justify-center items-center ">
        <div className="grow flex-row flex gap-3">
          
          <div className="w-96 deboss rounded-2xl p-10 flex flex-col items-center justify-center">
            <div className="bg-black h-full aspect-[9/16]">

            </div>
          </div>

          <div className="flex flex-col justify-end">
            
            <Button className="w-16 h-16">
              <AiFillLike className="w-8 h-8"/>
            </Button>
            
            <Button className="w-16 h-16">
              <AiFillDislike className="w-8 h-8"/>
            </Button>

          </div>
        </div>
      </div>
    </Layout>
  );
}

export default Index;