import React, { useState } from 'react';
import { 
    Box,
    Button, 
    Flex,
    FormControl,
    FormHelperText,
    FormLabel,
    Heading,
    Input,
    Modal, 
    ModalBody,
    ModalCloseButton,
    ModalContent,
    ModalFooter,
    ModalHeader,
    ModalOverlay,
    Text,
} from '@chakra-ui/react';

function MoreInfoModal({ info }) {

  const sampleInfo = {
    "subject": "This is a test title",
    "description": "This is test summary of a sample ticket.",
    "messages": [
        {"sender": "user", "content": "Lorem ipsum whatever"},
        {"sender": "assistant", "content": "Lorem ipsum whatever"},
        {"sender": "user", "content": "Lorem ipsum whatever"}
    ]
  }
  
  const [isOpen, setIsOpen] = useState(false);

  const toggleModal = () => {
    setIsOpen(!isOpen);
  };

  // retrieve messages from JSON
  const messages = sampleInfo.messages;

  return (
    <>
      <Button colorScheme="blue" onClick={toggleModal}>
        More Info
      </Button>

      <Modal isOpen={isOpen} onClose={toggleModal} size="3xl">
        <ModalOverlay />
        <ModalContent>
          <ModalHeader marginBottom="-15px">
            <Heading>
              {info.subject}
            </Heading>
          </ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <Box>
              <Text fontSize="lg" color="white" fontWeight="semibold"></Text>
              <Box borderRadius="md" borderColor="gray.200" marginBottom="10px">
                <Heading color="white" size="md" marginBottom="5px"><b>Summary:</b> </Heading>
                <Text marginLeft={5}>{info.description}</Text>
              </Box>

              <Box borderRadius="md" borderColor="gray.200">
                <Heading color="white" size="md" marginBottom="5px"><b>Conversation:</b></Heading>
                <Flex>
                  <Box>
                    {messages.map(message => <Text marginLeft={5}><b>{message.sender}:</b></Text>)}
                  </Box>
                  <Box marginLeft={5}>
                    {messages.map(message => <Text marginLeft={5}>{message.content}</Text>)}
                  </Box>
                </Flex>
              </Box>
            </Box>

            <FormControl isRequired marginTop="10px">
              <FormLabel>Answer</FormLabel>
              <Input type='text' />
              <FormHelperText>Press ENTER to submit</FormHelperText>
            </FormControl>
          </ModalBody>
          <ModalFooter>
            <Button variant="ghost" onClick={toggleModal}>
              Close
            </Button>
            <Button colorScheme="blue" ml={3}>
              Save Changes
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  );
}

export default MoreInfoModal;