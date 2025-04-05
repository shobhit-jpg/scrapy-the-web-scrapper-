# Import required libraries


import os
import asyncio
from crawl4ai import (
    AsyncWebCrawler,
    CrawlerRunConfig,
    DefaultMarkdownGenerator,
    LLMConfig,
    LLMContentFilter
)
from langchain_groq import ChatGroq
from langchain.schema import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore

# Load environment variables
URL = os.environ.get("url_RKG")
Fire_crawl = os.environ.get("FIRE_CRAWL")
Pine_cone = os.environ.get("PINE_CONE")
Groq_key = os.environ.get("GROQ_API_KEY")
print(URL)

# Main async function for crawling and markdown generation
async def main():
    gemini_config = LLMConfig(
        provider="groq/llama3-70b-8192",
        api_token="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"
    )

    filter = LLMContentFilter(
        llm_config=gemini_config,
        instruction="""
        Focus on extracting the core educational content.
        Include:
        - Key concepts and explanations
        - Essential technical details
        Exclude:
        - Navigation elements
        - Sidebars
        - Footer content
        Format the output as clean markdown with proper code blocks and headers.
        """,
        chunk_token_threshold=500,
        verbose=True
    )

    md_generator = DefaultMarkdownGenerator(content_filter=filter, options={"ignore_links": True})
    run_conf = CrawlerRunConfig(markdown_generator=md_generator)

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=URL, config=run_conf)
        return result.markdown

# Run the main coroutine
if __name__ == "__main__":
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        task = asyncio.create_task(main())
        loop.run_until_complete(task)
    else:
        crawl_result = asyncio.run(main())

# Initialize LLM
llm = ChatGroq(
    groq_api_key=Groq_key,
    model="llama3-8b-8192",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

# Define prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Your name is SCRAPY. You are a powerful AI assistant which analyzes the data stored in the variable {MD_DATA}. Return answer available only in the variable. If not, return the source URL in the variable."
    ),
    ("human", "{user_input}")
])

# Function to query the LLM using the extracted markdown data
def ask_llm(query, data=crawl_result):
    chain = prompt | llm
    res = chain.invoke({"MD_DATA": crawl_result, "user_input": query})
    return res.content

# Interactive prompt loop
while True:
    ques = input("")
    if ques == "Break":
        break
    print(ask_llm(query=ques))
