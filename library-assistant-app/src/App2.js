
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Chat from './pages/Chat';
import LibrarianUI from './pages/LibrarianUI';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Chat} />
        {/* {<Route path="/about" component={About} />} */}
        <Route path="styles/staff" component={LibrarianUI} />
      </Switch>
    </Router>
  );
}

export default App;
