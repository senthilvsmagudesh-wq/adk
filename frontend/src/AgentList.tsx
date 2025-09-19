
import React from 'react';
import { Accordion } from 'react-bootstrap';

const AGENT_PROMPTS = [
    {
        "agent_name": "Precedent Analysis Agent",
        "module": "Elite Squad / Strategist",
        "purpose": "Queries the legal case database to find relevant history.",
    },
    {
        "agent_name": "Compliance Verification Agent",
        "module": "Elite Squad / Strategist",
        "purpose": "Queries the statutory (legal code) database to check for compliance.",
    },
    {
        "agent_name": "Graph Reasoning Agent",
        "module": "Elite Squad / Strategist",
        "purpose": "Performs complex logic queries on the knowledge graph.",
    },
    {
        "agent_name": "Argument Miner Agent",
        "module": "Elite Squad / Strategist",
        "purpose": "Proactively finds weaknesses and points of leverage for negotiation.",
    },
    {
        "agent_name": "Negotiation Strategist Agent",
        "module": "Elite Squad / Strategist",
        "purpose": "Drafts alternative, fairer clauses and suggests negotiation strategies.",
    },
    {
        "agent_name": "Document Ingestion Agent",
        "module": "Intake & Digitization",
        "purpose": "Handles file uploads (PDF, DOCX, JPG).",
    },
    {
        "agent_name": "OCR Agent",
        "module": "Intake & Digitization",
        "purpose": "Extracts text from images or scanned PDFs.",
    },
    {
        "agent_name": "Data Cleaning Agent",
        "module": "Intake & Digitization",
        "purpose": "Removes headers, footers, and formatting noise.",
    },
    {
        "agent_name": "Document Classifier Agent",
        "module": "Core Comprehension",
        "purpose": "Identifies the document type (e.g., Lease, NDA).",
    },
    {
        "agent_name": "Clause Segmenter Agent",
        "module": "Core Comprehension",
        "purpose": "Breaks the full text into individual clauses.",
    },
    {
        "agent_name": "Entity Recognition Agent",
        "module": "Core Comprehension",
        "purpose": "Extracts key facts like names, dates, and amounts.",
    },
    {
        "agent_name": "Jargon Buster Agent",
        "module": "Core Comprehension",
        "purpose": "Defines complex legal terms in simple language.",
    },
    {
        "agent_name": "Clause Simplifier Agent",
        "module": "Deep Analysis & Simplification",
        "purpose": "Rewrites legal clauses into plain English.",
    },
    {
        "agent_name": "Obligations & Rights Extractor Agent",
        "module": "Deep Analysis & Simplification",
        "purpose": "Creates 'You Must Do' and 'You Can Do' lists.",
    },
    {
        "agent_name": "High-Level Summarizer Agent",
        "module": "Deep Analysis & Simplification",
        "purpose": "Generates a one-paragraph summary of the document.",
    },
    {
        "agent_name": "Risk Assessor Agent",
        "module": "Initial Risk & Compliance",
        "purpose": "Flags clauses with a Red/Yellow/Green risk score.",
    },
    {
        "agent_name": "Ambiguity Detector Agent",
        "module": "Initial Risk & Compliance",
        "purpose": "Finds vague phrases that could cause disputes.",
    },
    {
        "agent_name": "Missing Clause Agent",
        "module": "Initial Risk & Compliance",
        "purpose": "Identifies standard clauses that are absent.",
    },
    {
        "agent_name": "Jurisdictional Compliance Agent",
        "module": "Initial Risk & Compliance",
        "purpose": "Performs a check against jurisdiction-specific laws.",
    },
    {
        "agent_name": "Q&A Agent",
        "module": "User Interaction",
        "purpose": "Answers user-specific questions about the document.",
    },
    {
        "agent_name": "Report Generator Agent",
        "module": "User Interaction",
        "purpose": "Assembles outputs into a clean, final report.",
    },
    {
        "agent_name": "Multilingual Translator Agent",
        "module": "User Interaction",
        "purpose": "Translates the final report into local languages.",
    },
    {
        "agent_name": "Orchestrator Agent",
        "module": "Orchestration & Control",
        "purpose": "Manages the entire workflow and agent calls.",
    },
    {
        "agent_name": "Privacy Guard Agent",
        "module": "Orchestration & Control",
        "purpose": "Anonymizes Personally Identifiable Information (PII).",
    }
];

const AgentList: React.FC = () => {
  return (
    <Accordion>
      {AGENT_PROMPTS.map((agent, index) => (
        <Accordion.Item eventKey={String(index)} key={index}>
          <Accordion.Header>{agent.agent_name}</Accordion.Header>
          <Accordion.Body>
            <strong>Module:</strong> {agent.module}
            <br />
            <strong>Purpose:</strong> {agent.purpose}
          </Accordion.Body>
        </Accordion.Item>
      ))}
    </Accordion>
  );
};

export default AgentList;
