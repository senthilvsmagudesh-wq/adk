import React, { useState } from 'react';
import { Navbar, Container, Tabs, Tab } from 'react-bootstrap';
import FileUpload from './FileUpload';
import Results from './Results';
import AgentList from './AgentList';
import './App.css';

function App() {
  const [analysisResult, setAnalysisResult] = useState<any>(null);

  return (
    <div className="App">
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="#home">Legis Synapse</Navbar.Brand>
        </Container>
      </Navbar>
      <Container style={{ marginTop: '2rem' }}>
        <Tabs defaultActiveKey="analysis" id="main-tabs" className="mb-3">
          <Tab eventKey="analysis" title="Document Analysis">
            <FileUpload onAnalysisResult={setAnalysisResult} />
            <div style={{ marginTop: '2rem' }}>
              <Results result={analysisResult} />
            </div>
          </Tab>
          <Tab eventKey="agents" title="Available Agents">
            <AgentList />
          </Tab>
        </Tabs>
      </Container>
    </div>
  );
}

export default App;