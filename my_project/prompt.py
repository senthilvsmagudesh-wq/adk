# prompt.py

# Prompts for Foundational Agents (Intake, Comprehension, and Analysis)
FOUNDATIONAL_AGENTS_PROMPTS = [
    # Intake & Digitization
    "Please process and clean this uploaded rental agreement.",  # Triggers Document Ingestion, OCR, Data Cleaning
    "I've scanned my contract as a JPG, can you analyze it?",

    # Core Comprehension
    "What type of document is this? Is it an NDA or a lease?",  # Triggers Document Classifier
    "Break this document down into individual clauses for me.",  # Triggers Clause Segmenter
    "Extract the names, dates, and amounts mentioned in this agreement.",  # Triggers Entity Recognition
    "What does the term 'indemnification' mean in simple language?",  # Triggers Jargon Buster

    # Deep Analysis & Simplification
    "Can you rewrite this complicated clause in plain English?",  # Triggers Clause Simplifier
    "List all the things I 'must do' and 'can do' according to this contract.",  # Triggers Obligations/Rights Extractor
    "Give me a quick, one-paragraph summary of the entire document.",  # Triggers High-Level Summarizer
]

# Prompts for Risk, Compliance, and User Interaction Agents
RISK_AND_INTERACTION_PROMPTS = [
    # Initial Risk & Compliance
    "Assess the risk level of the 'Security Deposit' clause.",  # Triggers Risk Assessor
    "Is there any vague or ambiguous language in this section?",  # Triggers Ambiguity Detector
    "Are there any standard clauses missing from this agreement?",  # Triggers Missing Clause Agent

    # User Interaction
    "What is the notice period required to terminate the contract?",  # Triggers Q&A Agent
    "Generate a complete, clean report of your analysis.",  # Triggers Report Generator
    "Translate the final report into Tamil for me.",  # Triggers Multilingual Translator
]

# Prompts for Advanced "Strategist" Agents
STRATEGIST_AGENTS_PROMPTS = [
    # Precedent Analysis
    "How have courts interpreted similar 'force majeure' clauses in the past?",  # Triggers Precedent Analysis Agent

    # Compliance Verification
    "The security deposit is ₹1,00,000 for a rent of ₹20,000 in Tamil Nadu. Is this legally compliant?",  # Triggers Compliance Verification Agent

    # Graph Reasoning
    "Based on the whole document, what are the consequences if I miss a payment deadline?",  # Triggers Graph Reasoning Agent

    # Argument Miner
    "Find weaknesses or points of leverage I can use in negotiation.",  # Triggers Argument Miner Agent

    # Negotiation Strategist
    "This security deposit clause seems unfair. Can you help me draft a polite email to the landlord to negotiate it?",  # Triggers Negotiation Strategist Agent
]

# Combine all into one list for the demo
ALL_PROMPTS = FOUNDATIONAL_AGENTS_PROMPTS + RISK_AND_INTERACTION_PROMPTS + STRATEGIST_AGENTS_PROMPTS