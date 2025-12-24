/* =========================
   API ENVIRONMENT SWITCHING
   ========================= */

const API_BASE =
  location.hostname === "localhost" ||
  location.hostname === "127.0.0.1" ||
  location.protocol === "file:"
    ? "http://127.0.0.1:5000"
    : "https://fake-review-detector-f0wz.onrender.com";

/* =========================
   NAVIGATION
   ========================= */

function showSection(id) {
  document.querySelectorAll(".section").forEach(sec => {
    sec.classList.remove("active");
  });
  document.getElementById(id).classList.add("active");
}

/* =========================
   FAKE REVIEW ANALYSIS
   ========================= */

async function analyze() {
  const review = document.getElementById("review").value.trim();
  if (!review) return;

  document.getElementById("loading").classList.remove("hidden");
  document.getElementById("result").classList.add("hidden");

  try {
    const response = await fetch(`${API_BASE}/analyze`, {
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

    const reasonsList = document.getElementById("reasons");
    reasonsList.innerHTML = "";
    data.reasons.forEach(reason => {
      const li = document.createElement("li");
      li.innerText = reason;
      reasonsList.appendChild(li);
    });

    document.getElementById("result").classList.remove("hidden");

  } catch (err) {
    alert("Backend is waking up. Please try again in a few seconds.");
  } finally {
    document.getElementById("loading").classList.add("hidden");
  }
}

/* =========================
   REVIEW REWRITE (FREE NLP)
   ========================= */

async function rewriteReview() {
  const input = document.getElementById("rewriteInput").value.trim();
  if (!input) return;

  try {
    const response = await fetch(`${API_BASE}/rewrite`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ review: input })
    });

    const data = await response.json();
    document.getElementById("rewriteOutput").value = data.rewritten_review;

  } catch (err) {
    alert("Unable to rewrite review. Please try again.");
  }
}
