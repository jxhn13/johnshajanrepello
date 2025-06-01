import React, { useState, useEffect, useRef } from "react";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [loadingMessage, setLoadingMessage] = useState("Your response is coming");
  const [isThinking, setIsThinking] = useState(false);

  const loadingIntervalRef = useRef(null);
  function linkify(text) {
    const urlPattern = /(\bhttps?:\/\/[^\s]+)/g;
    return text.replace(urlPattern, (url) => {
      return `<a href="${url}" target="_blank" rel="noopener noreferrer">${url}</a>`;
    });
  }

  useEffect(() => {
    if (loading) {
      let dots = 0;
      loadingIntervalRef.current = setInterval(() => {
        dots = (dots + 1) % 4; // cycles 0..3 dots
        setLoadingMessage("Your response is coming" + ".".repeat(dots));
      }, 500);
    } else {
      clearInterval(loadingIntervalRef.current);
      setLoadingMessage("Your response is coming");
    }

    return () => clearInterval(loadingIntervalRef.current);
  }, [loading]);

  const handleSubmit = async () => {
    if (!query.trim()) return;
    setIsThinking(true);      // Start thinking
    setResponse(""); 
    setLoading(true);
    setResponse("");

    try {
      const res = await fetch("http://localhost:5000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });

      const data = await res.json();
      setResponse(data.answer);
    } catch (error) {
      setResponse("Error: Could not fetch response.");
    } finally {
      setLoading(false);
      setIsThinking(false); 
    }
  };

  return (
    <div className="app-container">
      <h1 className="header">AI Research Assistant with Web Browsing </h1>
      <textarea
        className="query-box"
        placeholder="Ask me anything..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        rows={4}
        disabled={loading}
      />
      <button
        className="generate-button"
        onClick={handleSubmit}
        disabled={loading || !query.trim()}
      >
        {loading ? "Thinking..." : "Generate"}
      </button>
      <pre
        className="response-box"
        dangerouslySetInnerHTML={{
          __html: loading ? loadingMessage : linkify(response )|| "Your answer will appear here.",
        }}
      />
    </div>
  );
}

export default App;
