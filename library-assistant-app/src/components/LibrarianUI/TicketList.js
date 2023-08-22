import React, { useState } from 'react';
import './staff2.css';
import Ticket from "./Ticket.js"
import {VStack, Text, Divider, Box} from '@chakra-ui/react'

function TicketList() {
  const [tickets, setTickets] = useState([
    { id: 1, subject: 'Website Not Loading', description: 'I am unable to access the website.' },
    { id: 2, subject: 'Password Reset', description: 'I forgot my password and need to reset it.' },
    { id: 3, subject: 'Payment Issue', description: 'I was charged incorrectly for my subscription.' },
  ]);

  return (
    <VStack align="stretch" spacing={4} p={4} boxShadow="md" borderRadius="md" bg="white">
      <Text fontSize="xl" fontWeight="bold">Help Ticket List</Text>
      <Divider />
      {tickets.map(ticket => (
        <Box key={ticket.id} p={3} borderWidth={1} borderRadius="md" borderColor="gray.200">
          <Text fontSize="lg" color="black" fontWeight="semibold">{ticket.subject}</Text>
          <Text color="black">{ticket.description}</Text>
        </Box>
      ))}
    </VStack>
  );
}

export default TicketList;
