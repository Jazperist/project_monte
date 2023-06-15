import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class NewClienteForm extends React.Component {
  state = {
    id: 0,
    nombre: "",
    apellido: "",
    telefono: "",
    email: "",
    fecha_inicio: "",
    cantidad_pedida:"",
    plazo: "",
    total: "0.00"
  };

  componentDidMount() {
    if (this.props.cliente) {
      const { id, nombre, apellido, telefono, email, fecha_inicio, cantidad_pedida, plazo, total } = this.props.cliente;
      this.setState({ id, nombre, apellido, telefono, email, fecha_inicio, cantidad_pedida, plazo, total });
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  createCliente = e => {
    e.preventDefault();
    axios.post(API_URL, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  editCliente = e => {
    e.preventDefault();
    axios.put(API_URL + this.state.id, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.cliente ? this.editCliente : this.createCliente}>
        <FormGroup>
          <Label for="nombre">Nombre:</Label>
          <Input
            type="text"
            name="nombre"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.nombre)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="apellido">Apellido:</Label>
          <Input
            type="text"
            name="apellido"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.apellido)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="telefono">Teléfono:</Label>
          <Input
            type="text"
            name="telefono"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.telefono)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="email">Email:</Label>
          <Input
            type="email"
            name="email"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.email)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="fecha_inicio">Fecha de inicio:</Label>
          <Input
            type="date"
            name="fecha_inicio"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.fecha_inicio)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="cantidad_pedida">Cantidad pedida:</Label>
          <Input
            type="text"
            name="cantidad_pedida"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.cantidad_pedida)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="plazo">Plazo:</Label>
          <Input
            type="text"
            name="plazo"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.plazo)}
          />
          <small>Solo acepta 3, 6 o 9 (meses)</small>
        </FormGroup>
        
        <Button>Enviar</Button>
      </Form>
    );
  }
}

export default NewClienteForm;