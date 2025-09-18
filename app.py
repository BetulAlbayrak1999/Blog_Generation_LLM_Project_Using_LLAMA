import streamlit as st
import torch
from transformers import pipeline


def get_llama_response(input_text, no_words, blog_style):
    """
    Generates a blog post using the Llama-3.2-1B model from Hugging Face.

    Args:
        input_text (str): The topic or title for the blog post.
        no_words (int): The desired length of the blog post in words.
        blog_style (str): The style or tone of the blog post.
    Returns:
        str: The generated blog post.

    """

    pipe = pipeline(
        "text-generation",
        model="mistralai/Mistral-7B-Instruct-v0.3",
        device_map="auto",
        torch_dtype=torch.float16,
    )
    
    # Create the pormpt string
    prompt = f"Write a blog for a {blog_style} job profile for the topic '{input_text}' within {no_words} words."

    # Generate the response
    response = pipe(
        prompt,
        do_sample=True,
        max_new_tokens=no_words + 50,
        truncation=True,
        eos_token_id=pipe.tokenizer.eos_token_id,
    )

    # Extract the generation text from the pipeline output and remove the prompt
    generate_text = response[0]["generated_text"]

    # Clean the output after remove the prompt part

    cleaned_output = generate_text.replace(prompt, "").strip()

    print(cleaned_output)
    return cleaned_output


st.set_page_config(
    page_title="Blog Post Generator",
    page_icon=":robot:",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.header("Blog Post Generator 🤖")

input_text = st.text_input(
    "Enter the topic or title for the blog post",
    placeholder="e.g., The Future of AI in Healthcare",
)

## creating 2 more columns for aditional fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input(
        "Enter the length of the blog post (in words)", placeholder="e.g., 500"
    )

with col2:
    blog_style = st.selectbox(
        "Writing the blog for",
        ("Researcher", "Student", "Professional", "Hobbyist", "General Audience"),
        index=0,
    )


submit = st.button("Generate Blog Post")

## Final response

if submit:
    st.write(get_llama_response(input_text, no_words, blog_style))
