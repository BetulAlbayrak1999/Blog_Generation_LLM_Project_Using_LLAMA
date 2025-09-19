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

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    dtype= torch.float16 if torch.cuda.is_available() else torch.float32

    pipe = pipeline(
        "text-generation",
        model="openai-community/gpt2",
        device=0,
        dtype=dtype,
        pad_token_id=50256
    )

    # Create the pormpt string
    prompt = f"""Write a professional blog post about "{input_text}" for a {blog_style} audience.

            The blog should be approximately {no_words} words and include:
            - An engaging introduction
            - Key points and insights
            - A compelling conclusion

            Blog Post:
            """

    no_words = int(no_words) if no_words.isdigit() else 500
    # Generate the response
    response = pipe(
        prompt,
        do_sample=True,
        max_new_tokens=no_words + 50,
        temperature=0.7,
        top_p=0.9,
        truncation=True,
        pad_token_id=50256,
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
