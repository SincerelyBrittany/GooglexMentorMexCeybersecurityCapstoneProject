import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import PhishingQuiz from './app/PhishingQuiz';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <PhishingQuiz />
    </>
  )
}

export default App
