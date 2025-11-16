from utils.parse_pdf import extract_text_from_pdf

def parse_resume(file_path):
    # currently handles PDF resumes
    return extract_text_from_pdf(file_path)
