// Queue.js
import React from 'react';
import Ticket from './Ticket';
import '../../styles/staff.css'

function Queue({ tickets }) {
  return (
    <div className="queue">
      <h2>Ticket Queue</h2>
      {tickets.map((ticket, index) => (
        <Ticket key={index} ticket={ticket} />
      ))}
    </div>
  );
}

export default Queue;
