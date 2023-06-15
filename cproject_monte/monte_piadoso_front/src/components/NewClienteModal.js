import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NewClienteForm from "./NewClienteForm";

class NewClienteModal extends Component {
  state = {
    modal: false
  };

  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };

  render() {
    const create = this.props.create;

    var title = "Editando cliente";
    var button = <Button onClick={this.toggle}>Editar</Button>;
    if (create) {
      title = "Creando cliente";

      button = (
        <Button
          color="primary"
          className="float-right"
          onClick={this.toggle}
          style={{ minWidth: "200px" }}
        >
          Crear nuevo
        </Button>
      );
    }

    return (
      <Fragment>
        {button}
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>{title}</ModalHeader>

          <ModalBody>
            <NewClienteForm
              resetState={this.props.resetState}
              toggle={this.toggle}
              cliente={this.props.cliente}
            />
          </ModalBody>
        </Modal>
      </Fragment>
    );
  }
}

export default NewClienteModal;