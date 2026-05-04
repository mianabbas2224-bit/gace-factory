const API_KEY = "AIzaSyAx4wp84rJhIm4wnUjWvox8Ygd_tQZL_jM";
// We are using the v1beta endpoint and the specific gemini-1.5-flash-latest model
const URL = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=${API_KEY}`;

async function runAgent() {
    console.log("Connecting directly to the GACE Intelligence Network...");

    const data = {
        contents: [{
            parts: [{ text: "Role: Luxury Minimalist Copywriter. Task: Write a 5-word headline for a Matte Black EV Charger." }]
        }]
    };

    try {
        const response = await fetch(URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const json = await response.json();
        
        if (json.candidates && json.candidates[0].content) {
            console.log("\n--- AGENT OUTPUT ---");
            console.log(json.candidates[0].content.parts[0].text);
            console.log("--------------------\n");
        } else {
            console.log("Error Detail: " + JSON.stringify(json));
        }
    } catch (error) {
        console.log("Connection Error: " + error.message);
    }
}

runAgent();



