import React, { useState } from 'react';
import { Container, Title, Input, Button } from './styled-components';

const KeywordChecker = () => {
  const [input, setInput] = useState('');
  const [result, setResult] = useState(null);

  const handleCheck = async () => {
    if (!input.trim()) return;
    const res = await fetch(`http://127.0.0.1:5000/check-keyword?q=${input}`);
    const data = await res.json();
    setResult(data);
  };

  return (
    <Container>
      <Title>Phishing Keyword Checker</Title>
      <Input
        placeholder="Enter a keyword..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <Button onClick={handleCheck}>Check</Button>

      {result && (
        <div style={{ marginTop: '1rem' }}>
          {result.error && <p>{result.error}</p>}
          {result.found === false && <p>❌ Not found in phishing dataset.</p>}
          {result.frequency && (
            <p>
              ✅ Found! <strong>{result.keyword}</strong> appeared <strong>{result.frequency}</strong> times. <br />
              It is considered <strong>{result.is_common ? 'Common' : 'Uncommon'}</strong>.
            </p>
          )}
        </div>
      )}
    </Container>
  );
};

export default KeywordChecker;
