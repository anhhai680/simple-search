import React from 'react';
import { Button, Card, CardContent, Typography } from '@mui/material';

function UserCard({ name, email }) {
  return (
    <Card className="max-w-sm mx-auto bg-white shadow-lg rounded-lg overflow-hidden">
      <CardContent className="p-6">
        <Typography variant="h5" component="div" className="text-gray-800 font-bold mb-2">
          {name}
        </Typography>
        <Typography variant="body2" className="text-gray-600 mb-4">
          {email}
        </Typography>
        <Button variant="contained" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          View Profile
        </Button>
      </CardContent>
    </Card>
  );
}

export default UserCard;