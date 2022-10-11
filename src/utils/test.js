import React, { useState, useEffect } from 'react';

function Test() {
  const [currentTest, setCurrentTest] = useState("");

  useEffect(() => {
    fetch('/test').then((res) => res.json()).then((data) => setCurrentTest(data.data))
  }, []);

  return (
    <div className="Test">
      { currentTest }
    </div>
  );
}

export default Test;