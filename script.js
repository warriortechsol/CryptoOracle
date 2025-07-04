ddocument.addEventListener("DOMContentLoaded", () => {
  const predictBtn = document.getElementById("predictBtn");

  predictBtn.addEventListener("click", async () => {
    const symbol = document.getElementById("symbolInput").value.trim();
    const price = parseFloat(document.getElementById("priceInput").value);

    if (!symbol || isNaN(price)) {
      alert("Please enter a valid crypto symbol and price.");
      return;
    }

    try {
      const apiRes = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ symbol, current_price: price })
      });

      const data = await apiRes.json();

      document.getElementById("predicted").textContent = `Predicted Price: $${data.predicted_price.toFixed(2)}`;
      document.getElementById("sentiment").textContent = `Sentiment Score: ${data.sentiment_score.toFixed(2)}`;
      document.getElementById("recommendation").textContent = `Recommendation: ${data.recommendation}`;

    } catch (error) {
      console.error("Error fetching prediction:", error);
      alert("Something went wrong while fetching data.");
    }
  });

  // 🌙 Dark mode toggle handler
  const modeToggle = document.getElementById("modeToggle");
  modeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
  });
});
