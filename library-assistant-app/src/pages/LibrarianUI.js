// App.js
import React, { useState } from 'react';
import TicketForm from '../components/LibrarianUI/TicketForm';
import Queue from '../components/LibrarianUI/Queue';
import TicketList from '../components/LibrarianUI/TicketList';
import '../styles/staff.css'
// import { Box } from '@chakra-ui/react'


function LibrarianUI() {
  const [tickets, setTickets] = useState([]);

  const addTicket = (ticket) => {
    setTickets([...tickets, ticket]);
  };

  return (
    <div className="App">
      <TicketList></TicketList>
    </div>
  );
}

export default LibrarianUI;
