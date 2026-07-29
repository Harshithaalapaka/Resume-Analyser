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
    job_description : str = Form(...)
):
    file_bytes = await file.read()
    resume_text = extract_text(file_bytes, file.filename)
    result = match_resume_to_job(resume_text, job_description)
    return { "analysis " : result}

    
