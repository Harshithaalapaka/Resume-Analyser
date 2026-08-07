import streamlit as st
import requests
st.title("Resume Analyser")
st.write("Upload a resume and paste a job description to see how well they match")
uploaded_file= st.file_uploader("Upload your resume", type=["pdf",'docx'])
job_description=st.text_area("Enter the job description here", height=200)
if st.button("Analyse"):
    if uploaded_file is None:
        st.warning("please upload a resume file first")
    elif not job_description.strip():
        st.warning("please paste a job description")
    else:
        with st.spinner("Analysing...this may take a few seconds"):
            files={"file":(uploaded_file.name, uploaded_file.getvalue())}
            data={"job_description": job_description}
            response=requests.post(
                "http://127.0.0.1:8000/analyse",
                files=files,
                data=data
            )
            if response.status_code==200:
                result=response.json()
                st.success("Analysis complete!")
                st.markdown(result["analysis"])
            else:
                st.error(f"something went wrong:{response.status_code}")
                st.text(response.text)
 