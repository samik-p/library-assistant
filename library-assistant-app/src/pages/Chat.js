import React, { useState } from 'react';
import {
  ChakraProvider,
  Box,
  Input,
  Button,
  VStack,
  Text,
  Divider,
} from '@chakra-ui/react';





function Chat() {
  const [messages, setMessages] = useState([]);
  const [inputText, setInputText] = useState('');

  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  const handleSendMessage = () => {
    if (inputText.trim() !== '') {
      // console.log("PRINT: " + get_assistant_response("ok"));
      get_assistant_response(inputText);
      setInputText('');
    }
  };

  const get_assistant_response = (user_input) => {
    fetch("http://localhost:8000/api/chat/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ "user_message": user_input, "pk": 1 })
    }).then((response) => {
      // first then: checks for error
      // console.log("First then")
      // console.log(response)
      if (!response.ok) {
        throw new Error('HTTP error! Status: ' + response.status)
      }
      return response.json();
    })
      .then((data) => {
        // console.log("Second then")
        // process the JSON response data
        console.log("RESPONSE: " + data["response"])
        // return data["response"];
        setMessages([...messages, { text: inputText, isUser: true }, { text: data["response"], isUser: false }])
      })
      .catch((error) => {
        console.log("Error")
        // handle errors
        console.error('Fetch error:', error)
      })
  };

  return (
    <div className="chat-page">
      <Box h="100vh" pt="100px" display="flex" alignItems="center" justifyContent="center" overflowY="scroll" marginBottom="40px">
        <Box maxW="90vw" borderWidth="1px" borderRadius="lg" p="4">
          <VStack spacing="4">
            <Box flex="1">
              <Text fontSize="lg" fontWeight="bold" align="center">
                Chatbot
              </Text>
              <Divider mt="2" mb="4" />
              <Box
                height="80vh"  // Adjust the height as needed
                width="80vw"
                overflowY="scroll"
                borderRadius="md"
                p="2"
                bg="gray.100"
              >
                {messages.map((message, index) => (
                  <Text
                    key={index}
                    bg={message.isUser ? 'blue.200' : 'gray.200'}
                    p="2"
                    borderRadius="md"
                    color="black"
                    margin="0.5vh"
                  >
                    {message.text}
                  </Text>
                ))}
              </Box>
            </Box>
            <Input
              value={inputText}
              onChange={handleInputChange}
              placeholder="Type your message..."
            />
            <Button colorScheme="blue" onClick={handleSendMessage}>
              Send
            </Button>
          </VStack>
        </Box>
      </Box>
    </div>
  );
}

export default Chat;