async function askAI() {
  const question = document.getElementById('question').value;
  document.getElementById('answer').textContent = "Thinking...";
  const res = await fetch('https://takori-finetune.onrender.com/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question })
  });
  const data = await res.json();
  document.getElementById('answer').textContent = data.answer;
}