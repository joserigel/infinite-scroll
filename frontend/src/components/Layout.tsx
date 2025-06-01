import React, { JSX } from "react";

import { MdFileUpload, MdAccountCircle } from "react-icons/md";
import { Link } from "react-router";


interface LayoutProps {
  children?: string | JSX.Element | JSX.Element[] | undefined;
}

const Layout = ({children}: LayoutProps) => {
  return (<div className="absolute min-h-screen w-screen flex flex-col">
    <header className="
      bg-gradient-to-b from-[#ddd] to-white
      items-stretch m-3
      rounded-full emboss
      flex flex-row justify-between sticky">
      <h1 className="font-bold
        items-center justify-center flex
        m-1 px-3 rounded-full">
        InfiniteScroll
      </h1>
      <div className="
        flex m-1 gap-1">
        <Link to="/upload"
          className="duration-300
          hover:bg-[#bbb]
          p-3 rounded-full">
          <MdFileUpload size={20}/>
        </Link>
        <Link to="/upload"
          className="duration-300
          hover:bg-[#bbb]
          p-3 rounded-full">
          <MdAccountCircle size={20}/>
        </Link>
      </div>
    </header>
    <main className="grow flex flex-col">
      { children }
    </main>
    <footer></footer>
  </div>)
}

export default Layout;