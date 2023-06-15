import React, { Component } from "react";

class Header extends Component {
  render() {
    return (
      <div className="text-center">
        <img
          src={require('../Monte_Piadoso.png')}
          width="300"
          alt="Logo de empresa"
          className="img-thumbnail"
          style={{ marginTop: "20px" }}
        />
        <hr />
        <h5>
          <i></i>
        </h5>
        <h1>Lista de clientes</h1>
      </div>
    );
  }
}

export default Header;