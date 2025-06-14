// import React, { useEffect, useState } from 'react';

// const TopKeywords = () => {
//   const [keywords, setKeywords] = useState([]);
//   const [showOnlyCommon, setShowOnlyCommon] = useState(false);

//   useEffect(() => {
//     const fetchKeywords = async () => {
//       const res = await fetch('http://127.0.0.1:5000/phishing-patterns');
//       const data = await res.json();
//       setKeywords(data.sort((a, b) => b.frequency - a.frequency));
//     };
//     fetchKeywords();
//   }, []);

//   const filtered = showOnlyCommon
//     ? keywords.filter((k) => k.is_common)
//     : keywords;

//   return (
//     <div className="max-w-lg mx-auto mt-6 p-4 border rounded shadow">
//       <div className="flex justify-between items-center mb-2">
//         <h2 className="text-lg font-bold">Top Phishing Keywords</h2>
//         <label className="text-sm">
//           <input
//             type="checkbox"
//             checked={showOnlyCommon}
//             onChange={() => setShowOnlyCommon(!showOnlyCommon)}
//             className="mr-1"
//           />
//           Show Common Only
//         </label>
//       </div>

//       <ul className="list-disc pl-5 space-y-1">
//         {filtered.map((item, idx) => (
//           <li key={idx}>
//             <span className="font-medium">{item.keyword}</span> – {item.frequency} uses
//             {item.is_common && (
//               <span className="ml-2 px-2 text-xs bg-red-100 text-red-600 rounded-full">Common Threat</span>
//             )}
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// };

// export default TopKeywords;


// import React, { useEffect, useState } from 'react';
// import { Container, Title, Badge } from './styled-components';
// import { List, ListItem } from './styled-components'; // or define here

// const TopKeywords = () => {
//   const [keywords, setKeywords] = useState([]);

//   useEffect(() => {
//     const fetchKeywords = async () => {
//       const response = await fetch('http://127.0.0.1:5000/phishing-patterns');
//       const data = await response.json();
//       console.log('Fetched keywords:', data);

//       setKeywords(data);
//     };
//     fetchKeywords();
//   }, []);

//   return (
//     <Container>
//       <Title>Top Phishing Keywords</Title>
//       <List>
//         {keywords.map((item, index) => (
//           <ListItem key={index}>
//             {item.keyword} ({item.frequency})
//             {item.is_common && <Badge>Common</Badge>}
//           </ListItem>
//         ))}
//       </List>
//     </Container>
//   );
// };

// export default TopKeywords;


import React, { useEffect, useState } from 'react';
import { Container, Title, Badge, Button } from './styled-components';

const TopKeywords = () => {
  const [keywords, setKeywords] = useState([]);
  const [filter, setFilter] = useState('all');

  const fetchKeywords = async (filterType) => {
    const response = await fetch(`http://127.0.0.1:5000/top-keywords?filter=${filterType}`);
    const data = await response.json();
    setKeywords(data);
  };

  useEffect(() => {
    fetchKeywords(filter);
  }, [filter]);

  return (
    <Container>
      <Title>Top Phishing Keywords</Title>
      <div style={{ marginBottom: '1rem' }}>
        <Button onClick={() => setFilter('all')}>All</Button>{' '}
        <Button onClick={() => setFilter('common')}>Common</Button>{' '}
        <Button onClick={() => setFilter('uncommon')}>Uncommon</Button>
      </div>
      <ul>
        {keywords.map((item, index) => (
          <li key={index}>
            {item.keyword} ({item.frequency})
            {item.is_common && <Badge>Common</Badge>}
          </li>
        ))}
      </ul>
    </Container>
  );
};

export default TopKeywords;
