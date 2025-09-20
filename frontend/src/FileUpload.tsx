import React, { useState } from 'react';
import { Form, Button, Container, Row, Col, Spinner, Alert } from 'react-bootstrap';

interface Props {
  onAnalysisResult: (result: any) => void;
}

const FileUpload: React.FC<Props> = ({ onAnalysisResult }) => {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const handleAnalyze = async () => {
    if (!file) {
      setError('Please select a file to analyze.');
      return;
    }

    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:5000/analyze', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Failed to analyze the document.');
      }

      const result = await response.json();
      onAnalysisResult(result);
    } catch (error: any) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container>
      <Row className="justify-content-md-center">
        <Col xs={12} md={6}>
          <Form>
            <Form.Group controlId="formFile" className="mb-3">
              <Form.Label>Upload your legal document</Form.Label>
              <Form.Control type="file" onChange={handleFileChange} />
            </Form.Group>
            <Button variant="primary" onClick={handleAnalyze} disabled={loading}>
              {loading ? (
                <>
                  <Spinner
                    as="span"
                    animation="border"
                    size="sm"
                    role="status"
                    aria-hidden="true"
                  />
                  Analyzing...
                </>
              ) : (
                'Analyze'
              )}
            </Button>
          </Form>
          {error && <Alert variant="danger" style={{ marginTop: '1rem' }}>{error}</Alert>}
        </Col>
      </Row>
    </Container>
  );
};

export default FileUpload;