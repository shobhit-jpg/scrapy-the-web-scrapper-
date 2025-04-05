# 🔍 Scrapy: Smart Web Crawler Powered by LLMs

**Scrapy** is an intelligent web crawler that extracts clean, structured educational content from websites using AI. It combines `crawl4ai` with powerful large language models (LLMs) like **Groq's LLaMA3** to filter, format, and analyze raw HTML into usable markdown. The scraped content is then used to answer user queries through a natural language interface.

---

## 🚀 Features

- 🌐 **Asynchronous Web Crawling** with `crawl4ai`
- 🧠 **LLM-Powered Content Filtering** using `groq/llama3`
- 📝 **Clean Markdown Generation** from raw web content
- 💬 **Ask Questions from Extracted Data** using `LangChain` & `Groq`
- 🧪 **Integrated CLI** for real-time querying
- 🔐 **API Key Management** via `.env` for security

---

## 🛠️ Tech Stack

- Python 3.10+
- Crawl4AI
- LangChain
- Groq LLaMA3 via `langchain-groq`
- Firecrawl
- Gradio *(UI in progress)*

---

## 📁 Example Use Case

Scrapy crawls the [RKGIT Official Website](https://rkgit.edu.in) (You can add your desired website in the .env file ) and extracts only educational content like:

- ✅ Course Information  
- ✅ Faculty Details  
- ✅ Research Highlights  
- ❌ Skips navigation bars, sidebars, footers, etc.

---

## 📌 Coming Soon

- 🖥️ Gradio-based GUI
- 📄 Multi-page Crawling
- 💾 Pinecone Integration for Persistent Storages 


