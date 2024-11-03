const apiUrl = "http://localhost:8000";

async function getCount() {
    try {
        const response = await fetch(apiUrl + "/count");
        const data = await response.json();
        console.log("Fetched count:", data); // Should log the fetched data
        document.getElementById("count").innerText = data.count || 0; // Ensure data.count is valid
    } catch (error) {
        console.error("Error fetching count:", error);
        document.getElementById("count").innerText = "Error";
    }
}


async function changeCount(delta) {
    const endpoint = delta > 0 ? "/increment" : "/decrement";
    const response = await fetch(apiUrl + endpoint, { method: "POST" });
    const data = await response.json();
    document.getElementById("count").innerText = data.count;
}

// Fetch and set the initial count when the page loads
getCount();
