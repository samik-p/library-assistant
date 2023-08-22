// Ticket.js
import React from 'react';
import '../../styles/staff.css'


function Ticket({ ticket }) {
  return (
    <div className="ticket">
      <h4>{ticket.title}</h4>
      <p>{ticket.description}</p>
    </div>
  );
}

export default Ticket;
