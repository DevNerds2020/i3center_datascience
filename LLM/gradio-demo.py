import gradio as gr

def greet(name, intensity):
    return "Hello, "

demo = gr.Interface(
    fn=greet,
    inputs=["text"],
    outputs=["text"],
)

demo.launch(share=True)
