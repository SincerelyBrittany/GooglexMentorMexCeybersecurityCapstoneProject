// import React, { useState } from "react";

// const PhishingQuiz = () => {
//   const [email, setEmail] = useState("");
//   const [selected, setSelected] = useState("");
//   const [submitted, setSubmitted] = useState(false);

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     if (!selected) return alert("Please select an answer.");

//     const score = selected === "urgent" ? 1 : 0;
//     const missed_warning = selected !== "urgent" ? "Didn't recognize urgency" : "";

//     const payload = { email, score, missed_warning };

//     try {
//       const response = await fetch("http://127.0.0.1:5000/submit", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify(payload),
//       });

//       if (response.ok) {
//         setSubmitted(true);
//       } else {
//         alert("There was an error saving your response.");
//       }
//     } catch (error) {
//       console.error("Submission error:", error);
//       alert("Could not connect to the server.");
//     }
//   };

//   return (
//     <div className="max-w-xl mx-auto p-4 border rounded-xl shadow">
//       <h1 className="text-xl font-bold mb-4">Phishing Awareness Quiz</h1>

//       {!submitted ? (
//         <form onSubmit={handleSubmit}>
//           <label className="block mb-2">
//             Your Email:
//             <input
//               type="email"
//               required
//               className="block w-full p-2 border rounded my-1"
//               value={email}
//               onChange={(e) => setEmail(e.target.value)}
//             />
//           </label>

//           <p className="font-semibold mt-4">Which is a common phishing red flag?</p>
//           <div className="my-2">
//             <label className="block">
//               <input
//                 type="radio"
//                 value="urgent"
//                 checked={selected === "urgent"}
//                 onChange={(e) => setSelected(e.target.value)}
//               />
//               &nbsp;"Urgent action required"
//             </label>
//             <label className="block">
//               <input
//                 type="radio"
//                 value="genuine"
//                 checked={selected === "genuine"}
//                 onChange={(e) => setSelected(e.target.value)}
//               />
//               &nbsp;"Have a great day!"
//             </label>
//           </div>

//           <button
//             type="submit"
//             className="mt-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
//           >
//             Submit
//           </button>
//         </form>
//       ) : (
//         <p className="text-green-600 mt-4">Thanks! Your result has been saved.</p>
//       )}
//     </div>
//   );
// };

// export default PhishingQuiz;


// import React, { useState, useEffect } from 'react';

// const PhishingQuiz = () => {
//   const [email, setEmail] = useState('');
//   const [questions, setQuestions] = useState([]);
//   const [current, setCurrent] = useState(0);
//   const [selected, setSelected] = useState('');
//   const [score, setScore] = useState(0);
//   const [missed, setMissed] = useState([]);
//   const [submitted, setSubmitted] = useState(false);

//   useEffect(() => {
//     const loadQuestions = async () => {
//       const res = await fetch('http://127.0.0.1:5000/questions');
//       const data = await res.json();
//       setQuestions(data);
//     };
//     loadQuestions();
//   }, []);

//   const handleNext = () => {
//     const currentQ = questions[current];
//     if (selected === currentQ.correct) {
//       setScore(score + 1);
//     } else {
//       setMissed([...missed, currentQ.missed_warning]);
//     }

//     setSelected('');
//     if (current < questions.length - 1) {
//       setCurrent(current + 1);
//     } else {
//       submitResults();
//     }
//   };

//   const submitResults = async () => {
//     await fetch('http://127.0.0.1:5000/submit', {
//       method: 'POST',
//       headers: { 'Content-Type': 'application/json' },
//       body: JSON.stringify({ email, score, missed_warning: missed.join('; ') })
//     });
//     setSubmitted(true);
//   };

//   if (submitted) {
//     return (
//       <div className="max-w-xl mx-auto p-4">
//         <h2 className="text-lg font-bold">Thanks for completing the quiz!</h2>
//         <p>Your score: {score} / {questions.length}</p>
//         <p className="text-sm mt-2 text-gray-600">Warnings missed: {missed.join(', ')}</p>
//       </div>
//     );
//   }

//   if (questions.length === 0) return <p>Loading questions...</p>;

//   const q = questions[current];

//   return (
//     <div className="max-w-xl mx-auto p-4 border rounded shadow">
//       <h2 className="text-lg font-bold mb-4">Phishing Quiz</h2>
//       {current === 0 && (
//         <label className="block mb-4">
//           Enter your email:
//           <input
//             className="block w-full p-2 border rounded mt-1"
//             value={email}
//             onChange={(e) => setEmail(e.target.value)}
//             required
//           />
//         </label>
//       )}

//       <p className="font-semibold">{q.question}</p>
//       <div className="my-3">
//         {Object.entries(q.options).map(([key, val]) => (
//           <label key={key} className="block">
//             <input
//               type="radio"
//               name="option"
//               value={key}
//               checked={selected === key}
//               onChange={(e) => setSelected(e.target.value)}
//             />{' '}
//             {val}
//           </label>
//         ))}
//       </div>

//       <button
//         onClick={handleNext}
//         disabled={!selected}
//         className="px-4 py-2 mt-2 bg-blue-600 text-white rounded hover:bg-blue-700"
//       >
//         {current === questions.length - 1 ? 'Submit' : 'Next'}
//       </button>
//     </div>
//   );
// };

// export default PhishingQuiz;


// styled-components.jsx (optional if reusing shared styles)
// You can use this file to define reusable styled components across the app


// PhishingQuiz.jsx
import React, { useState, useEffect } from 'react';
import { Container, Label, Input, Button } from './styled-components';

function shuffleArray(array) {
  return [...array].sort(() => Math.random() - 0.5);
}

const PhishingQuiz = () => {
  const [email, setEmail] = useState('');
  const [questions, setQuestions] = useState([]);
  const [current, setCurrent] = useState(0);
  const [selected, setSelected] = useState('');
  const [score, setScore] = useState(0);
  const [missed, setMissed] = useState([]);
  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    const loadQuestions = async () => {
      const res = await fetch('http://127.0.0.1:5000/questions');
      const data = await res.json();
      const randomThree = shuffleArray(data).slice(0, 3);
      setQuestions(randomThree);
    };
    loadQuestions();
  }, []);

  const handleNext = () => {
    const currentQ = questions[current];
    if (selected === currentQ.correct) {
      setScore(score + 1);
    } else {
      setMissed([...missed, currentQ.missed_warning]);
    }
    setSelected('');
    if (current < questions.length - 1) {
      setCurrent(current + 1);
    } else {
      submitResults();
    }
  };

  const submitResults = async () => {
    await fetch('http://127.0.0.1:5000/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, score, missed_warning: missed.join('; ') })
    });
    setSubmitted(true);
  };

  if (submitted) {
    return (
      <Container>
        <h2>Thanks for completing the quiz!</h2>
        <p>Your score: {score} / {questions.length}</p>
        <p>Warnings missed: {missed.join(', ')}</p>
      </Container>
    );
  }

  if (questions.length === 0) return <Container><p>Loading questions...</p></Container>;

  const q = questions[current];

  return (
    <Container>
      <h2>Phishing Quiz</h2>
      {/* {current === 0 && (
        <Label>Email:
          <Input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </Label>
      )} */}

      <p>{q.question}</p>
      {Object.entries(q.options).map(([key, val]) => (
        <Label key={key}>
          <Input
            type="radio"
            name="option"
            value={key}
            checked={selected === key}
            onChange={(e) => setSelected(e.target.value)}
          />{' '}{val}
        </Label>
      ))}

      <Button onClick={handleNext} disabled={!selected}>
        {current === questions.length - 1 ? 'Submit' : 'Next'}
      </Button>
    </Container>
  );
};

export default PhishingQuiz;
