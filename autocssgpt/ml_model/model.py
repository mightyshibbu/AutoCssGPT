from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM, logging

# ml_model/model.py
def process_input(user_input, output_type):
    """
    Process input and generate code in the desired format.
    """
    # Ignore warnings from the transformers library
    logging.set_verbosity(logging.CRITICAL)

    # Load the fine-tuned model and tokenizer
    new_model_path = "./ml_model/mymodel"  # Path to your fine-tuned model
    tokenizer = AutoTokenizer.from_pretrained(new_model_path)
    model = AutoModelForCausalLM.from_pretrained(new_model_path)

    # Define the input prompt
    input_prompt = user_input

    # Create the text-generation pipeline with the fine-tuned model
    pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=1024)

    # Generate text based on the input prompt
    result = pipe(f"<s>[INST] {input_prompt} [/INST]")
    temp = result[0]['generated_text']

    # Step 1: Remove newline characters
    temp = temp.replace("\n", "").replace("\r", "")  # Remove newlines and carriage returns

    # Step 2: Trim output from the first <!DOCTYPE html> to the first </html>
    start_index = temp.find("<!DOCTYPE html>")
    end_index = temp.find("</html>")

    if start_index != -1 and end_index != -1:
        # Extract the relevant part
        temp = temp[start_index:end_index + len("</html>")]

    # Return the cleaned output
    return temp
