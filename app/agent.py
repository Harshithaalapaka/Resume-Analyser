import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage

load_dotenv()

SYSTEM_PROMPT= """ you are a resume screening assistant. Compare the given resume against a job description and respond with :
1. A match score out of 100
2. key matching skills/experience
3. Notable gaps
4. A brief recommendation
"""

agent = create_agent(
    model="google_genai:gemini-2.5-flash",
    system_prompt=SYSTEM_PROMPT,
)

def match_resume_to_job(resume_text:str, job_description: str) -> str:
    user_message = f"""RESUME : {resume_text}
                      JOB Descripton : {job_description}
                    """
    result =agent.invoke({"messages" : [HumanMessage(user_message)]})
    return result["messages"][-1].content

#Given prompt, the prompt will go to mode and model will retur response.