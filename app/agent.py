import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from app.tools import check_skill_in_resume , get_years_of_experience

load_dotenv()

SYSTEM_PROMPT = """You are a resume screening assistant. You have access to tools 
that let you verify specific skills and check the candidate's years of experience.

Given a resume and a job description:
1. Use get_years_of_experience once, early on, to understand the candidate's 
   overall experience level
2. Identify the key skills/requirements mentioned in the job description
3. Use check_skill_in_resume to verify each important skill individually
4. Based on your findings, provide:
   - A match score out of 100
   - Key matching skills/experience (based on your tool checks)
   - Notable gaps (skills you checked that were NOT found)
   - A brief recommendation
"""

agent = create_agent(
    model="google_genai:gemini-3.6-flash",
    system_prompt=SYSTEM_PROMPT,
    tools = [check_skill_in_resume, get_years_of_experience],
)

def match_resume_to_job(resume_text:str, job_description: str) -> str:
    user_message = f"""RESUME : {resume_text}
                      JOB Descripton : {job_description}
                    """
    result =agent.invoke({"messages" : [HumanMessage(user_message)]})
    final_content = result["messages"][-1].content
    if isinstance(final_content, list):
        return final_content[0]["text"]
    return final_content

#Given prompt, the prompt will go to mode and model will retur response.