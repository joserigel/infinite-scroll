import React from "react";
import Layout from "../components/Layout";
import { Button } from "../components/Button";
import { Link } from "react-router";

const Login = () => {
  return (
    <Layout>
      <div className="h-full w-full grow flex flex-col justify-center items-center">
        <div className="bg-gray-200 max-w-96 emboss rounded-xl py-2 px-5 flex flex-col gap-3">
          <h1 className="text-center font-bold text-xl">Create your Account</h1>
          
          <div className="flex flex-col">
            <label>Username</label>
            <input type="text" 
              className="deboss rounded-full text-xl py-2 px-3 bg-gray-200"
              placeholder="bob1234"/>
          </div>

          <div className="flex flex-col">
            <label>Password</label>
            <input type="password" 
              className="deboss rounded-full text-xl py-2 px-3 bg-gray-200"
              placeholder="pass456"/>
          </div>

          <div className="flex flex-col">
            <label>Confirm Password</label>
            <input type="password" 
              className="deboss rounded-full text-xl py-2 px-3 bg-gray-200"
              placeholder="pass456"/>
          </div>

          <Button>Register</Button>
          <label className="text-center">
            Already have an account? <span/>
            <Link to="/login" className="font-medium">Click here</Link>
          </label>
        </div>
      </div>
    </Layout>
  )
}

export default Login;