// Ticket.js
import React from 'react';
import '../../styles/staff.css'

import {
  Box,
  Button,
  Flex,
  FormControl,
  FormLabel,
  FormErrorMessage,
  FormHelperText,
  Grid,
  Input,
  Spacer,
  Text,
  Divider,
} from '@chakra-ui/react'
import MoreInfoModal from './MoreInfoModal';


function Ticket({ ticket }) {
  return (
    <Box key={ticket.id} p={3} borderWidth={1} borderRadius="md" borderColor="gray.200" width="50vw" maxWidth="800" boxShadow="md">
      <Flex>
        <Box>
          <Text fontSize="lg" color="white" fontWeight="semibold">{ticket.subject}</Text>
          <Text color="white">{ticket.description}</Text>
        </Box>
        <Spacer />
        <Box width="200px" align="right">
          <MoreInfoModal info={ticket}>More Info</MoreInfoModal> {/* TODO: add props */}
        </Box>
      </Flex>

      <Divider />
      <Divider />


      <FormControl isRequired marginTop="10px">
        <FormLabel>Answer</FormLabel>
        <Input type='text' />
        <FormHelperText>Press ENTER to submit</FormHelperText>
      </FormControl>
        
    </Box>
  );
}

export default Ticket;
