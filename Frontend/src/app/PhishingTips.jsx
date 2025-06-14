const PhishingTips = () => (
    <div className="max-w-lg mx-auto mt-6 p-4 border rounded shadow">
      <h2 className="text-lg font-bold mb-2">How to Spot a Phishing Email</h2>
      <ul className="list-disc pl-5 space-y-1 text-sm">
        <li>Check the sender’s email address carefully.</li>
        <li>Watch for urgent or threatening language like “Act now!”</li>
        <li>Don’t click links—hover to preview them first.</li>
        <li>Look for grammar or spelling errors.</li>
        <li>Never provide passwords or sensitive info via email.</li>
      </ul>
      <p className="text-xs mt-3">
        Learn more at{' '}
        <a
          href="https://www.consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams"
          target="_blank"
          rel="noreferrer"
          className="text-blue-600 underline"
        >
          FTC.gov
        </a>
      </p>
    </div>
  );
  
  export default PhishingTips;
  