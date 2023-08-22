import React, { useState } from 'react';
import './staff2.css';
import Ticket from "./Ticket.js"
import {VStack, Text, Divider, Box} from '@chakra-ui/react'

function TicketList() {
  const [tickets, setTickets] = useState([
    { id: 1, subject: 'Website Not Loading', description: 'I am unable to access the website.' },
    { id: 2, subject: 'Password Reset', description: 'I forgot my password and need to reset it.' },
    { id: 3, subject: 'Payment Issue', description: 'I was charged incorrectly for my subscription.' },
    // { id: 4, subject: 'Website Not Loading', description: 'I am unable to access the website.' },
    // { id: 5, subject: 'Password Reset', description: 'I forgot my password and need to reset it.' },
    // { id: 6, subject: 'Payment Issue', description: 'I was charged incorrectly for my subscription.' },
    // { id: 7, subject: 'Website Not Loading', description: 'I am unable to access the website.' },
    // { id: 8, subject: 'Password Reset', description: 'I forgot my password and need to reset it.' },
    // { id: 9, subject: 'Payment Issue', description: 'I was charged incorrectly for my subscription.' },
    // { id: 10, subject: 'Website Not Loading', description: 'I am unable to access the website.' },
    // { id: 11, subject: 'Password Reset', description: 'I forgot my password and need to reset it.' },
    // { id: 12, subject: 'Payment Issue', description: 'I was charged incorrectly for my subscription.' },
    // { id: 13, subject: 'Website Not Loading', description: 'I am unable to access the website.' },
    // { id: 14, subject: 'Password Reset', description: 'I forgot my password and need to reset it.' },
    // { id: 15, subject: 'Payment Issue', description: 'I was charged incorrectly for my subscription.' },
  ]);

  return (
    <VStack align="center" spacing={4} p={4} borderRadius="md" bg="gray.800">
      <Text fontSize="xl" fontWeight="bold" align="center">Help Ticket List</Text>
      <Divider />
      {tickets.map(ticket => (
        <Ticket ticket={ticket}></Ticket>
      ))}
    </VStack>
  );
}

export default TicketList;
