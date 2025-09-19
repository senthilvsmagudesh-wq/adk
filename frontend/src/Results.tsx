
import React from 'react';
import { Card, Accordion } from 'react-bootstrap';

interface Props {
  result: any;
}

const Results: React.FC<Props> = ({ result }) => {
  if (!result) {
    return (
      <Card>
        <Card.Body>
          <p>Please upload a document and click "Analyze" to see the results.</p>
        </Card.Body>
      </Card>
    );
  }

  const renderAgentGroup = (group: any) => (
    <Accordion.Item eventKey={group.title} key={group.title}>
      <Accordion.Header>{group.title}</Accordion.Header>
      <Accordion.Body>
        {group.agents.map((agent: any, index: number) => (
          <div key={index}>
            <h5>{agent.name}</h5>
            <p>{agent.output}</p>
          </div>
        ))}
      </Accordion.Body>
    </Accordion.Item>
  );

  return (
    <Card>
      <Card.Body>
        <Card.Title>Analysis Results</Card.Title>
        <Accordion defaultActiveKey="0">
          {renderAgentGroup(result.intake_digitization)}
          {renderAgentGroup(result.core_comprehension)}
          {renderAgentGroup(result.deep_analysis)}
          {renderAgentGroup(result.initial_risk)}
          {renderAgentGroup(result.user_interaction)}
          {renderAgentGroup(result.orchestration_control)}
          {renderAgentGroup(result.strategist_agents)}
        </Accordion>
        <Card.Title style={{ marginTop: '2rem' }}>{result.final_summary.title}</Card.Title>
        <p>{result.final_summary.summary}</p>
      </Card.Body>
    </Card>
  );
};

export default Results;
