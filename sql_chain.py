from langchain_core.prompts import PromptTemplate
from langchain.chains import create_sql_query_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from operator import itemgetter
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool

# Custom query tool that handles query execution
class CustomQuerySQLDataBaseTool(QuerySQLDataBaseTool):
    def _run(self, query: str):
        # Clean up the query by removing backticks and newlines
        cleaned_query = query.strip("```sql\n").strip("\n```")
        return self.db.run_no_throw(cleaned_query)

# Chain to write SQL queries and execute them
def create_prompt_ans_chain(llm, db):
    prompt_ans = PromptTemplate.from_template(
        """Given the user question, corresponding SQL query, and SQL result, answer the user question.

        Question: {question}
        SQL Query: {query}
        SQL Result: {result}
        Answer: """
    )

    write_query = create_sql_query_chain(llm, db)
    execute_query = CustomQuerySQLDataBaseTool(db=db)
    
    ans = prompt_ans | llm | StrOutputParser()

    chain = (
        RunnablePassthrough.assign(query=write_query).assign(
            result=itemgetter("query") | execute_query
        ) | ans
    )
    return chain
