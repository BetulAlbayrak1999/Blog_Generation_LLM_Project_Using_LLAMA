# Blog Post Generator 🤖

A powerful AI-powered blog post generator built with Streamlit and Hugging Face Transformers. Generate professional blog posts tailored to different audiences using GPT-2 language model with GPU acceleration support.

## Features

AI-Powered Generation: Uses OpenAI's GPT-2 model for high-quality text generation
Customizable Output: Specify word count and target audience
Multiple Writing Styles: Generate content for researchers, students, professionals, hobbyists, or general audiences
GPU Acceleration: Automatic GPU detection and usage for faster generation
User-Friendly Interface: Clean and intuitive Streamlit web interface

## Demo
1. The app provides a simple interface where you can:
2. Enter your blog topic or title
3. Specify the desired word count
4. Select your target audience
5. Generate a professional blog post instantly


## Installation
### Prerequisites

- Python 3.8 or higher
- NVIDIA GPU (optional, for faster generation)
- CUDA toolkit (if using GPU)

#### Step 1: Clone the Repository
```bash 
git clone <your-repository-url>
cd BLOG_GENERATION
```

Step 2: Create Virtual Environment
Using conda (recommended):
```bash
conda create -n blog_generation python=3.11
conda activate blog_generation
```

Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```


## Running the Application

Step 1. Navigate to the project directory:
```bash 
cd BLOG_GENERATION
```

Step 2. Activate your virtual environment:
```bash
conda activate blog_generation
```     

Step 3. Run the Streamlit app:
```bash
streamlit run app.py
``` 

Step 4. Open your browser and go to:
```bash
http://localhost:8501
```


## Contributing

1. Fork the repository
2. Create a feature branch: git checkout -b feature-name
3. Make your changes and commit: git commit -am 'Add new feature'
4. Push to the branch: git push origin feature-name
5. Submit a pull request