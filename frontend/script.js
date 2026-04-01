let chart;
let historyList = [];

async function analyze() {
    const text = document.getElementById("text").value;

    const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text })
    });

    const data = await response.json();

    document.getElementById("result").innerText =
    "Emotion: " + data.sentiment.toUpperCase();

    document.getElementById("confidence").innerText =
        "Confidence: " + data.confidence + "%";

    drawChart(data.sentiment);
    updateHistory(text, data.sentiment);
}

function drawChart(sentiment) {
    const ctx = document.getElementById('chart').getContext('2d');

    if (chart) chart.destroy();

    let values = [0, 0, 0, 0];

    if (sentiment === "positive") values[0] = 1;
    else if (sentiment === "negative") values[1] = 1;
    else if (sentiment === "neutral") values[2] = 1;
    else values[3] = 1;

    chart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Positive', 'Negative', 'Neutral', 'Mixed'],
            datasets: [{
                data: values
            }]
        }
    });
}

function updateHistory(text, sentiment) {
    historyList.unshift({ text, sentiment });

    const list = document.getElementById("history");
    list.innerHTML = "";

    historyList.slice(0, 5).forEach(item => {
        const li = document.createElement("li");
        li.innerText = `${item.text} → ${item.sentiment}`;
        list.appendChild(li);
    });
}