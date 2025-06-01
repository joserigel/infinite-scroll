import React from "react";
import { createBrowserRouter } from "react-router";
import Index from "./Index";
import Upload from "./Upload";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Index/>
  },
  {
    path: "/upload",
    element: <Upload/>
  }
])