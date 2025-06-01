# johnshajan_repelloassignement
AI Research Assistant with Web Browsing
🔍 Overview
I developed an intelligent AI Research Assistant designed to answer complex user questions by actively researching information from the web. The assistant breaks down queries, performs live web searches, extracts key insights, and delivers concise, well-structured responses with proper citations.

Core capabilities:

Decompose complex queries into manageable sub-tasks

Perform real-time web searches via an external API

Extract and parse relevant content from multiple sources

Synthesize information using a language model for clear, informative answers

Provide source attributions for transparency and credibility

Security & Safety:
The agent includes robust safety mechanisms to detect and block malicious or inappropriate queries, sanitize unsafe content retrieved from the web, and apply moderation filters to ensure policy compliance in the final output.

This project demonstrates how AI can reason with live information responsibly and securely.

⚙️ Technical Approach
🧠 Reasoning Pipeline
User Query Input

The user submits a complex question through a React frontend, which is forwarded to the Flask backend for processing.

Input Safety Filtering

Implements keyword-based filtering to block unsafe or malicious prompts (e.g., keywords like “hack”, “porn”, “attack”).

Unsafe inputs trigger a safe rejection response.

Query Decomposition

Splits multi-part queries (detected by commas or conjunctions like “and”) into sub-queries to enable targeted, stepwise searching.

Web Search via SerpAPI + Google

Executes real-time web searches using the SerpAPI integration with Google Search.

Enables the assistant to fetch the latest information from multiple reliable sources.

Dynamic Content Extraction

Uses Playwright (headless Chromium) to render each web page fully, including JavaScript content.

Extracts the rendered HTML with page.content().

Parses articles from HTML using newspaper3k for clean text extraction.

Applies a custom sanitize_text() function to clean and remove harmful or injected instructions.

Answer Synthesis with LLM (cohere)

Combines cleaned texts from multiple sources as input to the cohere large language model.

Generates a synthesized, clear, and structured final answer.

Includes citations referencing source titles or URLs.

Content Moderation

The final output passes through a moderation filter to detect and remove any hate speech, explicit content, or policy violations, ensuring safe and compliant responses.

🛠️ Key Tools & Libraries
Purpose	Tool / Library
Real-time Web Search	SerpAPI (Google)
Dynamic Webpage Rendering	Playwright (Python)
Article Parsing	newspaper3k
Text Sanitization	bleach, custom functions
Language Model for Synthesis	cohere LLM
Backend API	Flask
Frontend UI	React.js


Security Measures
To ensure the AI Research Assistant operates safely and responsibly, I implemented several security and guardrail features:

Content Sanitization:
All web content retrieved by the agent is sanitized using the bleach library to strip out HTML tags and scripts, preventing any embedded malicious code or prompt injection attempts. Additionally, I applied custom keyword filtering to remove or redact phrases that could encourage unsafe behavior or reveal sensitive information (e.g., “ignore previous instructions,” “confidential,” or adult content keywords).

Toxicity and Content Moderation:
Before returning any response to the user, the agent runs the generated text through a toxicity classifier model that predicts whether the content is safe. If the toxicity score exceeds a predefined threshold, the output is blocked or flagged, preventing harmful, hateful, or inappropriate content from being delivered.

Query Filtering:
User input queries are checked against a list of banned or sensitive keywords related to illegal activities, explicit content, or violence. Queries containing these terms are rejected or handled with safe fallback responses, ensuring the agent does not perform web searches or generate answers related to disallowed topics.

Multi-step Reasoning with Safety Checks:
The agent decomposes complex queries into sub-queries and performs iterative web searches. At each step, the retrieved data is sanitized and checked to avoid propagation of unsafe or misleading content during synthesis.

Limitations & Future Improvements
While keyword-based filtering helps prevent many unsafe inputs, it can produce false positives or miss cleverly disguised queries. Incorporating more advanced natural language understanding could improve detection accuracy.

The toxicity classifier relies on pre-trained models and may not catch all harmful content or context nuances. Fine-tuning on domain-specific data and including additional moderation layers (such as human-in-the-loop review) could strengthen safety.

Web content changes dynamically; some malicious or misleading information might still bypass filters. Adding real-time heuristic analysis and blacklisting untrusted domains could further reduce risk.

Currently, sanitization focuses on text; multimedia content (images, videos) is not filtered and could be a vector for unsafe content.



Setup & Running Instructions
Create and activate a virtual environment
You can use venv, conda, or any environment manager of your choice.
For example, with Conda:

conda create -n ai-agent python=3.9 -y
conda activate ai-agent
Install dependencies
Navigate to the backend folder and install the required Python packages:


cd backend
pip install -r requirements.txt
Set up environment variables
Create a .env file in the backend folder and add your API keys and other configurations.
For example:

env

SEARCH_API_KEY=your_google_search_api_key_here
OTHER_CONFIG=value
Run the backend
From the backend folder, start the Python server:


python run.py
Run the frontend
Open a new terminal, navigate to the frontend folder, and start the React app:


cd ../frontend
npm install        # if not already installed
npm start
Access the application
Once both backend and frontend are running, open your browser and go to:

Edit
http://localhost:3000



Usage Guide
Open the app
After running both backend and frontend, open your browser at http://localhost:3000.

Input your query

Type your question or task into the search/input box on the main page.

Queries can be complex, such as:
“Compare the latest electric vehicle models and summarize their safety features.”
or multiple sub-queries separated by commas or “and”.

Submit the query

Click the Generate (or similar) button to start the research process.

The agent will perform live web searches, extract and sanitize information, then synthesize a clear, concise answer.

View the response

The answer will appear below the input box.

It includes summarized insights and citations/reference links to sources for credibility.

Security measures

If your query contains unsafe or banned keywords, the agent will politely refuse to answer and prompt you to modify the input.

The output is filtered to avoid harmful or disallowed content, ensuring a safe interaction.



Example scenarios
-----------------



Time Spent & Reflections
I allocated most of my time to implementing the core web search integration and ensuring reliable multi-step reasoning for accurate information gathering. Extracting and sanitizing web content posed challenges, especially handling noisy or unsafe data, which required careful filtering and use of a moderation model.

Building the security features, such as input sanitization and content moderation, was crucial and took additional effort to strike a balance between safety and useful output. The reasoning pipeline design, where the agent breaks down complex queries into sub-questions, helped improve answer quality but added complexity.

If given more time, I would enhance the UI for better user feedback on the agent’s step-by-step reasoning and add caching to improve response speed. I’d also explore integrating more advanced moderation APIs to further reduce false positives and better handle nuanced content.
