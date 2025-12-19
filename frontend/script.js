async function analyze() {
  const review = document.getElementById("review").value;

  const response = await fetch("https://fake-review-detector-f0wz.onrender.com/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ review })
  });

  const data = await response.json();

  document.getElementById("result").innerHTML = `
    <p>Repetition Score: ${data.repetition_score}</p>
    <p>Sentiment Score: ${data.sentiment_score}</p>
    <p><b>Credibility Score: ${data.credibility_score}</b></p>
    <p>Status: ${data.is_suspicious ? "⚠️ Suspicious" : "✅ Genuine"}</p>
  `;
}
