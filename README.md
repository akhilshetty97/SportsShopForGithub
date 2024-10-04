Strive Sports Analytics Hub     
Strive Sports Analytics Hub is an intelligent, SQL-powered system designed to answer questions by querying a MySQL database.  
Built with Langchain, Google Generative AI, and HuggingFace embeddings, this application allows users to retrieve real-time answers by converting their questions into precise SQL queries and gives the final results.  

Key Features:  
LLM-Powered SQL Query Generation & Execution: The Large Language Model (LLM) not only converts user questions into SQL queries but also executes the SQL query to fetch the final answer.  
Database Integration: Directly connected to a MySQL database to run the queries and fetch accurate results.  
Custom Query Execution: The generated SQL queries are optimized and cleaned before execution to ensure smooth database interactions.  
Few-Shot Learning: Implements semantic similarity to select relevant examples using HuggingFace embeddings and Chroma vector store.  
Real-Time Answering: Instantly returns precise answers to sports-related questions such as inventory counts, pricing, and more.  

Technologies Used:  
Langchain: For building LLM-driven pipelines and generating/executing SQL queries.
ChatGoogleGenerativeAI: Integrated with Google Gemini Pro for generating and running SQL queries.
HuggingFace Embeddings: Uses sentence-transformers/all-MiniLM-L6-v2 for embedding-based similarity matching.
Chroma Vector Store: Stores vectorized few-shot examples for semantic similarity selection.
MySQL: Back-end database for storing sports-related data (e.g., products, stock, and prices).  

How It Works:  
Step 1: The user inputs a question related to the products of the company (e.g., "How many Adidas products are left in stock?").
Step 2: The LLM generates a SQL query using Langchain and Google Generative AI.
Step 3: The generated SQL query is then executed by the LLM, fetching the data directly from the MySQL database.
Step 4: The query results are processed, and the final answer is returned to the user.
Step 5: For enhanced performance, few-shot learning examples are used to select the most relevant examples from a vector store powered by Chroma and HuggingFace embeddings.  

![image](https://github.com/user-attachments/assets/8f6ed3e4-303b-4ccc-aeee-ec3e787f4267)


Information about the products at Strive Sports.  

<img width="797" alt="image" src="https://github.com/user-attachments/assets/0817b4ac-7b3d-441b-b8af-662b28a41e65">

Information about the product discounts.  
<img width="263" alt="image" src="https://github.com/user-attachments/assets/6abb640e-7be3-4ed6-82e6-0d79ffccb3d3">



