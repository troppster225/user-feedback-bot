document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("feedback-form");
    const result = document.getElementById("result");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const content = new FormData(form).get("content");
        if (!content.trim()) {
            result.textContent = "Please enter some feedback before submitting.";
            return;
        }

        try {
            const res = await fetch("http://127.0.0.1:8000/feedback/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ content }),

            });
            
            if (!res.ok) {
                const error = await res.text();
                throw new Error(error || "Request failed");
            }

            const data = await res.json();
            result.textContent = `Feedback submitted successfully: ${data.id}`;
        } catch (err) {
            console.error(err)
            result.textContent = `Error: ${err.message}`;
        }
    });
});