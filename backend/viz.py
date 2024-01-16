from gradio import Interface
import gradio as gr
import pandas as pd

# Load the results dataset
data = pd.read_csv("results.csv").dropna()

def display_tweet_evaluation_data(index):
    if index is None or index < 0 or index >= len(data):
        return "Please enter a valid index (between 0 and {}).".format(len(data) - 1)
    
    entry = data.iloc[int(index)]

    # return {
    #     "User": entry['User'],
    #     "Tweet": entry['Tweet'],
    #     "Reasoning": entry['Reasoning'],
    #     "Answer": entry['Answer']
    # }
    return {
        "Prompt": entry['Prompt'],
        "Link": entry['Link'],
        "Reasoning": entry['Reasoning'],
        "Answer": entry['Answer']
    }

demo = gr.Interface(
    fn=display_tweet_evaluation_data,
    inputs=gr.Number(label="Tweet Index"),
    outputs=gr.JSON(label="Tweet Evaluation Data"),
    live=True,  # Updates the output live as the input changes
    title="Tweet Evaluation Data Viewer"
)

# Launch the interface
demo.launch()