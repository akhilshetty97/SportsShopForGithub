from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
import os
from dotenv import load_dotenv
from few_shot_learning_chain import get_few_shot_chain
from sql_chain import create_prompt_ans_chain

load_dotenv()
my_api_key = os.getenv('GEMINI_API_KEY')
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_name = os.getenv("db_name")

llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=my_api_key, temperature=0.3)

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info=3)

# Method 1: Single query execution
def execute_single_query(question: str):
    chain = create_prompt_ans_chain(llm, db)
    output = chain.invoke({"question": question})
    return output

# Method 2: Few-shot learning based query
def execute_few_shot_query(question: str):
    few_shot_chain = get_few_shot_chain(llm, db)
    return few_shot_chain


