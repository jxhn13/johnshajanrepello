Sure! Here’s your **AI Research Assistant with Web Browsing** project description formatted cleanly and professionally — perfect for a README, portfolio, or assignment submission:

---

# AI Research Assistant with Web Browsing

## 🔍 Overview

I developed an intelligent AI Research Assistant designed to answer complex user questions by actively researching information from the web. The assistant decomposes queries, performs live web searches, extracts key insights, and delivers concise, well-structured responses with proper citations.

**Core capabilities:**

* Decompose complex queries into manageable sub-tasks
* Perform real-time web searches via an external API
* Extract and parse relevant content from multiple sources
* Synthesize information using a language model for clear, informative answers
* Provide source attributions for transparency and credibility

---

## ⚙️ Technical Approach

### 🧠 Reasoning Pipeline

1. **User Query Input**
   Users submit complex questions through a React frontend, forwarded to a Flask backend.

2. **Input Safety Filtering**
   Keyword-based filtering blocks unsafe/malicious prompts (e.g., “hack”, “porn”, “attack”). Unsafe inputs trigger a safe rejection response.

3. **Query Decomposition**
   Multi-part queries (detected by commas or conjunctions like “and”) are split into sub-queries for targeted stepwise searching.

4. **Web Search via SerpAPI + Google**
   Executes real-time web searches using SerpAPI integration with Google Search to fetch the latest info from multiple reliable sources.

5. **Dynamic Content Extraction**

   * Uses Playwright (headless Chromium) to fully render web pages (including JavaScript content).
   * Extracts rendered HTML via `page.content()`.
   * Parses articles using `newspaper3k` for clean text extraction.
   * Sanitizes text with a custom `sanitize_text()` function to remove harmful or injected instructions.

6. **Answer Synthesis with LLM (cohere)**
   Combines cleaned texts from multiple sources as input to the Cohere large language model, generating a clear, structured final answer with citations referencing source titles or URLs.

7. **Content Moderation**
   The final output passes through a moderation filter to detect and remove hate speech, explicit content, or policy violations to ensure safe and compliant responses.

---

## 🛠️ Key Tools & Libraries

| Purpose                      | Tool / Library       |
| ---------------------------- | -------------------- |
| Real-time Web Search         | SerpAPI (Google)     |
| Dynamic Webpage Rendering    | Playwright (Python)  |
| Article Parsing              | newspaper3k          |
| Text Sanitization            | bleach, custom funcs |
| Language Model for Synthesis | Cohere LLM           |
| Backend API                  | Flask                |
| Frontend UI                  | React.js             |

---

## 🔐 Security Measures

* **Content Sanitization:**
  Web content is sanitized using `bleach` to strip HTML tags/scripts and prevent malicious code or prompt injections. Custom keyword filtering redacts unsafe phrases like “ignore previous instructions,” “confidential,” or adult content.

* **Toxicity & Content Moderation:**
  Generated text is checked by a toxicity classifier to block harmful or hateful outputs. High toxicity scores result in blocking or flagging content.

* **Query Filtering:**
  User inputs are scanned for banned keywords related to illegal activities, explicit content, or violence. Such queries are rejected with safe fallback responses.

* **Multi-step Reasoning Safety:**
  At each reasoning step, retrieved data is sanitized and safety-checked to prevent propagation of unsafe or misleading content.

---

## ⚠️ Limitations & Future Improvements

* Keyword filtering may produce false positives or miss cleverly disguised unsafe queries. More advanced NLP-based detection could improve accuracy.
* Toxicity classifier relies on pretrained models that may not catch all nuances; fine-tuning and human-in-the-loop moderation could enhance safety.
* Dynamic web content means some malicious/misleading info might bypass filters. Future work could include heuristic analysis and blacklisting untrusted domains.
* Currently, sanitization focuses on text; multimedia content (images, videos) is not filtered and remains a potential risk.

---

## 🚀 Setup & Running Instructions

### 1. Create & activate virtual environment

Example using Conda:

```bash
conda create -n ai-agent python=3.9 -y
conda activate ai-agent
```

### 2. Install dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in `backend/` with API keys and configs, e.g.:

```env
SEARCH_API_KEY=your_google_search_api_key_here
OTHER_CONFIG=value
```

### 4. Run backend

```bash
python run.py
```

### 5. Run frontend

Open a new terminal:

```bash
cd ../frontend
npm install   # if not installed yet
npm start
```

### 6. Access application

Open in browser:

```
http://localhost:3000
```

---

## 📖 Usage Guide

* **Open the app:** Visit `http://localhost:3000`
* **Input your query:** Enter complex questions or multi-part queries (use commas or “and”)
* **Submit query:** Click Generate to start live web search, extraction, sanitization, and synthesis
* **View response:** The agent provides a clear answer with citations
* **Security:** Unsafe queries will be politely rejected; output is filtered for harmful content

---

Here’s the corrected and polished version of your **Example Queries** section with proper formatting and spelling fixes:

---

## 🔎 Example Queries

* “Compare the latest electric vehicle models and summarize their safety features.”
* “What are the recent developments in quantum computing and their impact on cybersecurity?”
* “List and explain the main points from recent climate change reports.”

![aiweb1](https://github.com/user-attachments/assets/6078a329-d49c-423f-bccb-7f56ca7109bb)
![aiweb2](https://github.com/user-attachments/assets/6321ded7-3005-4924-8547-75bf97b04957)
![aiweb3](https://github.com/user-attachments/assets/769a70b9-9e6e-48ee-9d89-735fa0fa1458)

For more example queries, see the `samplequeries.txt` file.

---




## ⏳ Time Spent & Reflections

Most time was dedicated to implementing the core web search integration and ensuring robust multi-step reasoning for accurate info gathering. Handling noisy and unsafe web data required careful sanitization and moderation layers.

Security features—input filtering, content sanitization, toxicity moderation—were crucial to balancing safe and useful outputs but added complexity.

Future enhancements include improving UI feedback on reasoning steps, adding caching to speed responses, and integrating advanced moderation APIs to reduce false positives and handle nuanced content better.

---

