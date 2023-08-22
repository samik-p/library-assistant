import React, { useState } from 'react';
import {
  ChakraProvider,
  Box,
  Input,
  Button,
  VStack,
  Text,
  Divider,
  Link,
} from '@chakra-ui/react';

import { BrowserRouter as Router, Route, Routes, RouterProvider, createBrowserRouter, createRoutesFromElements } from 'react-router-dom';
import Chat from './pages/Chat';
import LibrarianUI from './pages/LibrarianUI';
import RootLayout from './layout/RootLayout';
import Test from './pages/Test';


function App() {

  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path="/" element={<RootLayout />}>
        <Route index element={<Chat />} />
        <Route path="/" element={<Chat />} />
        <Route path="/staff" element={<LibrarianUI />} />
        <Route path="/test" element={<Test />} />
      </Route>
    )
  )

  return (
    <ChakraProvider>
      <div className='App'>
        <RouterProvider router={router} />
      </div>
    </ChakraProvider>

  )
}

export default App;
