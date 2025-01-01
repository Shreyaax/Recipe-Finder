from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "Welcome to Recipe Finder!"}

@app.post("/create-recipe")
async def create_recipe(request: Request):
    data = await request.json()
    ingredients = data.get("ingredients", "")
    if not ingredients:
        raise HTTPException(status_code=400, detail="Ingredients are required")

    prompt = f"Create a recipe using the following ingredients: {ingredients}."
    print("Prompt:", prompt)  # Log the prompt

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        
        
        # Format the recipe as HTML without "*"
        recipe_text = response.text if response.text else "No recipe generated"
        formatted_recipe = recipe_text.replace("\n", "<br>").replace("*", "•")

        return {"recipe": formatted_recipe}
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating recipe: {str(e)}")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level="info")
