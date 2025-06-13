import React, { JSX } from "react";
import "./components.css";

interface ButtonProps {
  children?: string | JSX.Element | JSX.Element[];
  className?: string;
  [x: string]: any;
}

export const Button = ({children, className, ...rest}: ButtonProps) => (
  <div className={`rounded-button p-1 rounded-full emboss ${className}`}>
    <button 
      className={`
        w-full rounded-full h-full
        p-2
      `} 
      {...rest}
    >
      <div className="font-bold text-lg flex flex-col items-center justify-center">
        { children }
      </div>
    </button>
  </div>
)