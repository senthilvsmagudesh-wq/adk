
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# It's important to import your agent after initializing the Flask app
# to avoid potential circular dependencies or context issues.
from my_project.agent import get_agent_async

app = Flask(__name__)
CORS(app)

# Initialize the agent once, not on every request
root_agent = get_agent_async()

@app.route('/analyze', methods=['POST'])
def analyze_document():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # For a real application, you would save the file to a secure location
        # and pass the path to the agent.
        # For this example, we'll just simulate the analysis.
        # filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Simulate the agent's analysis
        # In a real application, you would call your agent here, e.g.:
        # result = root_agent.analyze(file.read())
        sample_result = {
            'intake_digitization': {
                'title': 'Intake & Digitization',
                'agents': [
                    { 'name': 'Document Ingestion Agent', 'output': 'File uploaded → Detected: Residential Rental Agreement on ₹20 Non-Judicial Stamp Paper.' },
                    { 'name': 'OCR Agent', 'output': 'Text extracted from scanned stamp paper successfully.' },
                    { 'name': 'Data Cleaning Agent', 'output': 'Removed headers/footers; structured raw text for analysis.' },
                ],
            },
            'core_comprehension': {
                'title': 'Core Comprehension',
                'agents': [
                    { 'name': 'Document Classifier Agent', 'output': 'Classified as Lease/Rental Agreement.' },
                    { 'name': 'Clause Segmenter Agent', 'output': 'Extracted sections: Parties, Rent, Security Deposit, Lease Term, Termination, Jurisdiction.' },
                    { 'name': 'Entity Recognition Agent', 'output': 'Found placeholders but missing key fields → Tenant Name ❌, Landlord Name ❌, Monthly Rent ❌, Deposit ❌, Lease Duration ❌.' },
                    { 'name': 'Jargon Buster Agent', 'output': 'Simplified terms like “Non-Judicial Stamp Duty” → “Government fee to make the document legally recognized.”' },
                ],
            },
            'deep_analysis': {
                'title': 'Deep Analysis & Simplification',
                'agents': [
                    { 'name': 'Clause Simplifier Agent', 'output': 'Rewrote each clause in plain English (example: “The lessee shall hereafter pay…” → “The tenant must pay rent every month”).' },
                    { 'name': 'Obligations & Rights Extractor', 'output': 'You Must Do: Fill in missing details, sign, and register with sub-registrar. You Can Do: Use premises as agreed once contract is valid.' },
                    { 'name': 'High-Level Summarizer', 'output': '“This is a rental agreement draft, but it is incomplete. Without tenant/landlord details, rent, deposit, and term, it is not enforceable.”' },
                ],
            },
            'initial_risk': {
                'title': 'Initial Risk & Compliance',
                'agents': [
                    { 'name': 'Risk Assessor Agent', 'output': '🚨 High Risk → Document invalid in current form.' },
                    { 'name': 'Ambiguity Detector Agent', 'output': '“Premises details” vague; no exact address.' },
                    { 'name': 'Missing Clause Agent', 'output': 'Missing Notice Period clause, Maintenance Responsibility, and Deposit Refund Conditions.' },
                    { 'name': 'Jurisdictional Compliance Agent', 'output': 'Tamil Nadu Rent Control Act requires rent + term + parties — all absent → ❌ Non-compliant.' },
                ],
            },
            'user_interaction': {
                'title': 'User Interaction',
                'agents': [
                    { 'name': 'Q&A Agent', 'output': 'If user asks: “Is this agreement legal?” → Answer: “No, not until all details are filled and registered.”' },
                    { 'name': 'Report Generator Agent', 'output': 'Compiles all agent outputs into structured dashboard (with risks, compliance, suggestions).' },
                    { 'name': 'Multilingual Translator Agent', 'output': 'Generates Tamil translation for accessibility.' },
                ],
            },
            'orchestration_control': {
                'title': 'Orchestration & Control',
                'agents': [
                    { 'name': 'Orchestrator Agent', 'output': 'Directed workflow → ensured each module triggered correctly.' },
                    { 'name': 'Privacy Guard Agent', 'output': 'Redacted placeholder PII markers.' },
                ],
            },
            'strategist_agents': {
                'title': 'Advanced Strategist Agents',
                'agents': [
                    { 'name': 'Precedent Analysis Agent', 'output': 'Retrieved Madras High Court case (fictional example): “Deposits exceeding 3 months’ rent without agreement ruled invalid.” Insight: Deposit clause (currently missing) must be clearly defined or could be challenged.' },
                    { 'name': 'Compliance Verification Agent', 'output': 'Checked with Tamil Nadu Rent Control Act (2017). Finding: Minimum details (parties, rent, deposit, term) are mandatory. Missing → Agreement unenforceable.' },
                    { 'name': 'Graph Reasoning Agent', 'output': 'Linked clauses: Without names → tenancy undefined; without rent → financial obligation unclear; without term → lease period invalid. Hidden consequence: Even if signed, landlord/tenant cannot enforce eviction or recovery of dues.' },
                    { 'name': 'Argument Miner Agent', 'output': 'Weakness detected: Tenant has no protection for refund of deposit. Negotiation leverage: Landlord must comply with legal requirements before signing.' },
                    { 'name': 'Negotiation Strategist Agent', 'output': 'Drafted polite negotiation email: “Dear Landlord, I reviewed the draft rental agreement. As per Tamil Nadu Rent Control Act, key details like names, rent, duration, and security deposit must be included. I request these be added along with a clear clause on deposit refund and notice period. Once updated, I’ll be happy to proceed.”' },
                ],
            },
            'final_summary': {
                'title': 'Final User-Friendly Summary (Plain English)',
                'summary': '“This rental. agreement is currently invalid because crucial details like tenant/landlord names, rent, deposit, and term are missing. Tamil Nadu law requires these to make the agreement enforceable. Additionally, the draft lacks notice period and deposit refund clauses, leaving the tenant unprotected. You should request the landlord to add these details before signing. Otherwise, the agreement cannot protect your rights in court.”'
            },
        }
        return jsonify(sample_result)

    return jsonify({'error': 'Something went wrong'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
