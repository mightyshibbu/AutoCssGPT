from django.http import JsonResponse
from django.shortcuts import render
from ml_model.model import process_input

def chat_view(request):
    output = ""
    output_type = "CSS"  # Default output type
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        output_type = request.POST.get("output_type", "CSS")
        output = process_input(user_input, output_type)
    
    return render(request, 'chatapp/index.html', {
        'output': output,
        'output_type': output_type,
    })

def generate_code(request):
    if request.method == 'POST':
        print("DEBUG: Received a POST request")  # Debugging the request type
        
        user_input = request.POST.get('user_input')
        output_type = request.POST.get('output_type', 'CSS')  # Default to 'CSS'
        
        print(f"DEBUG: User input received: {user_input}")  # Log user input
        print(f"DEBUG: Output type selected: {output_type}")  # Log output type
        
        # Call the model function with the input
        try:
            model_output = process_input(user_input, output_type)
            print(f"DEBUG: Model output generated: {model_output}")  # Log model output
        except Exception as e:
            print(f"ERROR: Exception occurred during processing: {e}")  # Log any errors
            return JsonResponse({'error': 'Processing failed'}, status=500)
        
        # Return the generated output as a JSON response
        return JsonResponse({'output': model_output})

    print("ERROR: Invalid request method")  # Log invalid request types
    return JsonResponse({'error': 'Invalid request'}, status=400)
