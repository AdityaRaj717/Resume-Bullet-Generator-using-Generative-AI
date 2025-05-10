# Resume Bullet Generator using Generative AI

## Overview

**Resume Bullet Generator** is an AI-powered tool that helps users transform informal, task-based descriptions into professional, concise, and impactful resume bullet points. Leveraging state-of-the-art NLP models (GPT-2), this project streamlines the resume writing process and helps users articulate their achievements more effectively.

---

## Features

- **AI-Powered Generation:** Converts casual descriptions into professional resume bullets.
- **User-Friendly Interface:** Simple input/output workflow using Streamlit (or Jupyter Notebook).
- **Customizable:** Easily adaptable for different industries or roles.
- **Open Source:** Freely available for learning and extension.

---

## Demo
![Screenshot 2025-05-10 225615](https://github.com/user-attachments/assets/b658d5fc-4716-425e-aebf-e408cf909e06)
![Screenshot 2025-05-10 225822](https://github.com/user-attachments/assets/d63c2dbd-7f75-481f-ad76-069233c3d647)

---

## Installation

### Prerequisites

- Python 3.7+
- pip

### Required Libraries

Install dependencies using pip:
pip install transformers streamlit torch

---

## Usage

### Streamlit App

1. **Save the code as `app.py`** (see [Code Example](#code-example) below).
2. **Run the app:**
    streamlit run app.py
3. **Open the provided local URL** in your browser to use the app.

### Jupyter Notebook

If you prefer Jupyter, you can use the core logic in a notebook cell without the Streamlit interface.

---

## Code Example

from transformers import pipeline, set_seed

#### Load the GPT-2 text generation pipeline
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

#### Example input
input_text = "I helped organize files in the office."

#### Prepare the prompt
prompt = f"Rewrite the following as a professional resume bullet: {input_text}"

#### Generate the bullet point
output = generator(prompt, max_length=40, num_return_sequences=1)
print(output['generated_text'])

---

## Sample Inputs

- I helped organize files in the office.
- Fixed bugs in the company website.
- Talked to customers and answered their questions.
- Made PowerPoint slides for meetings.
- Worked with a team to finish a project before the deadline.

---

## Sample Outputs

- Organized and maintained office filing systems to improve efficiency.
- Identified and resolved bugs on the company website, enhancing user experience.
- Provided prompt and accurate responses to customer inquiries.
- Developed engaging PowerPoint presentations for team meetings.
- Collaborated with team members to complete projects ahead of deadlines.

---

## Future Improvements

- Fine-tune the AI model on a dataset of resume bullets for improved relevance.
- Add industry/job role selection for tailored outputs.
- Implement a feedback system for continuous improvement.
- Support for multiple languages.
