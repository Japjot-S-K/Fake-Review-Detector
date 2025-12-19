function showSection(id) {
  document.querySelectorAll(".section").forEach(sec => {
    sec.classList.remove("active");
  });
  document.getElementById(id).classList.add("active");
}

async function analyze() {
  const review = document.getElementById("review").value.trim();
  if (!review) return;

  document.getElementById("loading").classList.remove("hidden");
  document.getElementById("result").classList.add("hidden");

  try {
    const response = await fetch("https://fake-review-detector-f0wz.onrender.com/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ review })
    });

    const data = await response.json();

    document.getElementById("credibility").innerText = data.credibility_score;
    document.getElementById("rep").innerText = data.repetition_score;
    document.getElementById("sent").innerText = data.sentiment_score;

    const status = document.getElementById("status");
    if (data.is_suspicious) {
      status.innerText = "Suspicious";
      status.style.color = "#ef4444";
    } else {
      status.innerText = "Genuine";
      status.style.color = "#22c55e";
    }

    document.getElementById("result").classList.remove("hidden");

  } catch (err) {
    alert("Backend is waking up. Please try again in a few seconds.");
  } finally {
    document.getElementById("loading").classList.add("hidden");
  }
}

function rewriteReview() {
  const input = document.getElementById("rewriteInput").value.trim();
  if (!input) return;

  const improved =
`The product performs as expected and provides reasonable quality for its price.
Delivery was on time and packaging was satisfactory.
Overall, the experience was decent and met expectations.`;

  document.getElementById("rewriteOutput").value = improved;
}

