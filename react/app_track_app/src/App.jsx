import React, { useState } from "react";
import api from "./api";
import "./App.css";  // Import the CSS file

const App = () => {
  const [signupResponse, setSignupResponse] = useState([]);
  const [formdata, setFormdata] = useState({
    username: "",
    password: "",
    email: "",
    role: "",
    phone: "",
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormdata({
      ...formdata,
      [name]: value,
    });
  };

  const handleSignup = async (event) => {
    event.preventDefault();
    try {
      await api.post("/candidates/userSignup", formdata);
      setSignupResponse("Signup successful!");
      setFormdata({
        username: "",
        password: "",
        email: "",
        role: "",
        phone: "",
      });
    } catch (error) {
      setSignupResponse("Signup failed. Please try again.");
    }
  };

  return (
    <div className="app-container">
      {/* Navbar */}
      <nav className="navbar navbar-dark bg-primary">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">
            Twite AI Technologies
          </a>
        </div>
      </nav>

      {/* Signup Form */}
      <div className="container">
        <h2 className="mt-4 mb-4">Signup Form</h2>
        <form onSubmit={handleSignup} className="w-100">
          <div className="mb-3">
            <label htmlFor="username" className="form-label">Username</label>
            <input
              type="text"
              className="form-control"
              id="username"
              name="username"
              value={formdata.username}
              onChange={handleInputChange}
              required
            />
          </div>

          <div className="mb-3">
            <label htmlFor="password" className="form-label">Password</label>
            <input
              type="password"
              className="form-control"
              id="password"
              name="password"
              value={formdata.password}
              onChange={handleInputChange}
              required
            />
          </div>

          <div className="mb-3">
            <label htmlFor="email" className="form-label">Email</label>
            <input
              type="email"
              className="form-control"
              id="email"
              name="email"
              value={formdata.email}
              onChange={handleInputChange}
              required
            />
          </div>

          <div className="mb-3">
            <label htmlFor="role" className="form-label">Role</label>
            <input
              type="text"
              className="form-control"
              id="role"
              name="role"
              value={formdata.role}
              onChange={handleInputChange}
              required
            />
          </div>

          <div className="mb-3">
            <label htmlFor="phone" className="form-label">Phone</label>
            <input
              type="text"
              className="form-control"
              id="phone"
              name="phone"
              value={formdata.phone}
              onChange={handleInputChange}
              required
            />
          </div>

          <button type="submit" className="btn btn-primary">Sign Up</button>
        </form>

        {/* Display signup response */}
        {signupResponse && (
          <div className="mt-4 alert alert-info">
            <p>{signupResponse}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default App;
