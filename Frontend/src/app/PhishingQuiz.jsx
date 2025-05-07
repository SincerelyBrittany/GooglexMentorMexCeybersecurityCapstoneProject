import React, { useState } from "react";

const PhishingQuiz = () => {
  const [email, setEmail] = useState("");
  const [selected, setSelected] = useState("");
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!selected) return alert("Please select an answer.");

    const score = selected === "urgent" ? 1 : 0;
    const missed_warning = selected !== "urgent" ? "Didn't recognize urgency" : "";

    const payload = { email, score, missed_warning };

    try {
      const response = await fetch("http://127.0.0.1:5000/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      if (response.ok) {
        setSubmitted(true);
      } else {
        alert("There was an error saving your response.");
      }
    } catch (error) {
      console.error("Submission error:", error);
      alert("Could not connect to the server.");
    }
  };

  return (
    <div className="max-w-xl mx-auto p-4 border rounded-xl shadow">
      <h1 className="text-xl font-bold mb-4">Phishing Awareness Quiz</h1>

      {!submitted ? (
        <form onSubmit={handleSubmit}>
          <label className="block mb-2">
            Your Email:
            <input
              type="email"
              required
              className="block w-full p-2 border rounded my-1"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </label>

          <p className="font-semibold mt-4">Which is a common phishing red flag?</p>
          <div className="my-2">
            <label className="block">
              <input
                type="radio"
                value="urgent"
                checked={selected === "urgent"}
                onChange={(e) => setSelected(e.target.value)}
              />
              &nbsp;"Urgent action required"
            </label>
            <label className="block">
              <input
                type="radio"
                value="genuine"
                checked={selected === "genuine"}
                onChange={(e) => setSelected(e.target.value)}
              />
              &nbsp;"Have a great day!"
            </label>
          </div>

          <button
            type="submit"
            className="mt-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
          >
            Submit
          </button>
        </form>
      ) : (
        <p className="text-green-600 mt-4">Thanks! Your result has been saved.</p>
      )}
    </div>
  );
};

export default PhishingQuiz;
