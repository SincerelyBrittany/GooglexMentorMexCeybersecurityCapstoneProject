import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import PhishingQuiz from './app/PhishingQuiz';
import TopKeywords from './app/TopKeywords';
import PhishingTips from './app/PhishingTips';
import AdminPanel from './app/AdminPanel';
import KeywordChecker from './app/KeywordChecker';

function App() {
  return (
    <div className="p-4">
      <PhishingQuiz />
      {/* <TopKeywords /> */}
      <KeywordChecker/>
      <PhishingTips />
      {/* <AdminPanel /> */}
    </div>
  );
}

export default App
