import React, { Component } from "react";
import { Table } from "reactstrap";
import NewClienteModal from "./NewClienteModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class ClienteList extends Component {
  render() {
    const clientes = this.props.clientes;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Telefono</th>
            <th>Email</th>
            <th>Cantidad pedida</th>
            <th>Fecha de registro</th>
            <th>Pk</th>
          </tr>
        </thead>
        <tbody>
          {!clientes || clientes.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Aun no hay clientes</b>
              </td>
            </tr>
          ) : (
            clientes.map(cliente => (
              <tr key={cliente.id}>
                <td>{cliente.nombre}</td>
                <td>{cliente.apellido}</td>
                <td>{cliente.telefono}</td>
                <td>{cliente.email}</td>
                <td>{cliente.cantidad_pedida}</td>
                <td>{cliente.fecha_inicio}</td>
                <td>{cliente.id}</td>
                <td align="center">
                  <NewClienteModal
                    create={false}
                    cliente={cliente}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    pk={cliente.id}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default ClienteList;