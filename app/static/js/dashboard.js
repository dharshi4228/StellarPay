async function loadStats() {
    const token = localStorage.getItem("token");

    if (!token) {
        console.warn("No token found. Redirecting to login...");
        window.location.href = "/auth/login";
        return;
    }

    try {
        const res = await fetch("/api/stats", {
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });

        if (!res.ok) {
            if (res.status === 401 || res.status === 422) {
                console.warn("Token invalid or expired. Redirecting to login...");
                localStorage.removeItem("token");
                window.location.href = "/auth/login";
                return;
            }
            throw new Error(`API returned ${res.status}`);
        }

        const data = await res.json();
        document.getElementById("totalTxns").innerText = data.total || 0;

        const ctx = document.getElementById("txnChart").getContext("2d");
        new Chart(ctx, {
            type: "bar",
            data: {
                labels: (data.amounts || []).map((_, i) => `Txn ${i + 1}`),
                datasets: [{
                    label: "Transaction Amount",
                    data: data.amounts || [],
                    backgroundColor: "#38bdf8"
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        labels: { color: "white" }
                    }
                },
                scales: {
                    x: { ticks: { color: "white" } },
                    y: { ticks: { color: "white" } }
                }
            }
        });
    } catch (error) {
        console.error("Error loading stats:", error);
        document.getElementById("totalTxns").innerText = "Error";
    }
}

// Load stats when page loads
window.addEventListener("load", loadStats);
