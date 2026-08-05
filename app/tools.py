from langchain_core.tools import tool
@tool
def check_skill_in_resume(resume_text:str, skill:str)->str :
    """ Check whether a specific skill/keyword appears in the resume text.
    use this to verify individual skills mentioned in job description,
    one at a time, before giving your final assessment.
    
    Args : 
        resume_text : the full text of candidate's resume.
        skill : the specific skill/keyword to search for(eg : "docker","python")

    """
    if skill.lower() in resume_text.lower():
        return f"'{skill}' was found in resume."
    return f"'{skill}' was not found in resume."

@tool
def get_years_of_experience(resume_text:str)->str:
    """find mentioned years of experience in resume text.
    
    Args : 
        resume_text: The full text of candidate's resume.
    """
    words=resume_text.split()
    found_numbers=[]
    for i,word in enumerate(words):
        if "year" in word.lower() and i>0 :
            possible_number = words[i-1].replace("+","")
            if possible_number.isdigit():
                found_numbers.append(int(possible_number))

    if not found_numbers:
        return "no years of experience is mentioned"

    return f"years of experience mentioned :{found_numbers}"
    