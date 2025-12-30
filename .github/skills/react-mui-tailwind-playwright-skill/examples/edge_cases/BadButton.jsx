import React from 'react';
import { Button } from '@mui/material';

function BadButton() {
  return (
    <div className="bg-red-500 text-white p-2 cursor-pointer" onClick={() => alert('Clicked!')}>
      Click me (bad: using div instead of button)
    </div>
  );
}

export default BadButton;