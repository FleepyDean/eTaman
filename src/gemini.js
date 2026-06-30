export const callGeminiAPI = async (prompt) => {
    const apiKey = import.meta.env.VITE_GEMINI_API_KEY || "";
    const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key=${apiKey}`;
    const payload = {
        contents: [{ parts: [{ text: prompt }] }],
    };

    let retries = 5;
    let delay = 1000;

    while (retries > 0) {
        try {
            const response = await fetch(url, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload),
            });

            if (!response.ok)
                throw new Error(`HTTP error! status: ${response.status}`);

            const result = await response.json();
            return result.candidates?.[0]?.content?.parts?.[0]?.text || "";
        } catch (error) {
            retries--;
            if (retries === 0) {
                console.error("Gemini API Error:", error);
                throw new Error("Gagal menyambung ke pelayan AI. Sila cuba lagi.");
            }
            await new Promise((res) => setTimeout(res, delay));
            delay *= 2;
        }
    }
};
