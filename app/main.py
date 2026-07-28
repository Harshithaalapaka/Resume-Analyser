from fastapi import FastAPI, UploadFile, File, Form
from app.extractor import extract_text
from app.agent import match_resume_to_job

app = FastAPI(title="Resume Analyser")

@app.get("/")
def root():
    return {"status" : "Resume_Analyser API is running"}

@app.post("/analyse")
async def analyse_resume(
    file : UploadFile = File(...),
    Job_description : str = Form(...)
):

    
