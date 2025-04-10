import React from 'react';
import { Bar } from 'react-chartjs-2';

const data = {
  labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
  datasets: [
    {
      label: '# of Votes',
      data: [12, 19, 3, 5, 2, 3],
      backgroundColor: 'rgba(75,192,192,0.4)',
    }
  ]
};

function App() {
  return (
    <div>
      <h1>Sample Chart</h1>
      <Bar data={data} />
    </div>
  );
}

export default App;
