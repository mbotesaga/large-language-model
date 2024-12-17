from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transformers import pipeline

# Load the Hugging Face model pipeline
model_pipeline = pipeline("text-generation", model="gpt2")

class GenerateTextView(APIView):
    """
    API endpoint for text generation using a Hugging Face model.
    """

    http_method_names = ['post']  # Restrict to POST requests

    def post(self, request, *args, **kwargs):
        prompt = request.data.get("prompt", "")

        if not prompt:
            return Response(
                {"error": "Prompt is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Generate text using the model
            result = model_pipeline(prompt, max_length=50, num_return_sequences=1)
            generated_text = result[0]["generated_text"]
            return Response({"generated_text": generated_text}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
