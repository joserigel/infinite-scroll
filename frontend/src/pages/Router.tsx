import React from "react";
import { createBrowserRouter } from "react-router";
import Index from "./Index";
import Upload from "./Upload";
import Login from "./Login";
import Register from "./Register"

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Index/>
  },
  {
    path: "/upload",
    element: <Upload/>
  },
  {
    path: "/login",
    element: <Login/>
  },
  {
    path: "/register",
    element: <Register/>
  }
])