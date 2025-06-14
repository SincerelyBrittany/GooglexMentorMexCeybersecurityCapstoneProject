import React, { useState } from 'react';

const AdminPanel = () => {
  const [form, setForm] = useState({
    question: '',
    option_a: '',
    option_b: '',
    correct_option: '',
    missed_warning: ''
  });

  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch('http://127.0.0.1:5000/add-question', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      });
      if (res.ok) {
        setMessage('✅ Question added!');
        setForm({ question: '', option_a: '', option_b: '', correct_option: '', missed_warning: '' });
      } else {
        setMessage('❌ Failed to add question.');
      }
    } catch (err) {
      console.error(err);
      setMessage('❌ Server error.');
    }
  };

  return (
    <div className="max-w-xl mx-auto mt-6 p-4 border rounded shadow">
      <h2 className="text-lg font-bold mb-4">Admin Panel – Add New Question</h2>
      <form onSubmit={handleSubmit} className="space-y-3">
        <input type="text" name="question" value={form.question} onChange={handleChange} required placeholder="Question" className="w-full p-2 border rounded" />
        <input type="text" name="option_a" value={form.option_a} onChange={handleChange} required placeholder="Option A" className="w-full p-2 border rounded" />
        <input type="text" name="option_b" value={form.option_b} onChange={handleChange} required placeholder="Option B" className="w-full p-2 border rounded" />

        <select name="correct_option" value={form.correct_option} onChange={handleChange} required className="w-full p-2 border rounded">
          <option value="">Select Correct Option</option>
          <option value="option_a">Option A</option>
          <option value="option_b">Option B</option>
        </select>

        <input type="text" name="missed_warning" value={form.missed_warning} onChange={handleChange} required placeholder="Missed warning description" className="w-full p-2 border rounded" />

        <button type="submit" className="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700">
          Add Question
        </button>

        {message && <p className="text-sm mt-2">{message}</p>}
      </form>
    </div>
  );
};

export default AdminPanel;
