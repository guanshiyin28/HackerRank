import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [firstText, setFirstText] = useState('');
  const [secondText, setSecondText] = useState('');
  const [appendedText, setAppendedText] = useState('');

  useEffect(() => {
    setAppendedText(`${firstText} ${secondText}`);
  }, [firstText, secondText]);

  const handleFirstTextChange = (event) => {
    setFirstText(event.target.value);
  };

  const handleSecondTextChange = (event) => {
    setSecondText(event.target.value);
  };

  return (
    <div>
      <h1>Text Append</h1>
      <div>
        <label>First Text:</label>
        <input type="text" value={firstText} onChange={handleFirstTextChange} />

        <label>Second Text:</label>
        <input type="text" value={secondText} onChange={handleSecondTextChange} />
      </div>

      <p>Appended Text:</p>
      <p>{appendedText}</p>
    </div>
  );
}

export default App;
