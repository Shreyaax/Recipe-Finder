async function findRecipe() {
    const ingredients = document.getElementById("ingredients").value;
    const recipeDiv = document.getElementById("recipe");

    if (!ingredients) {
        recipeDiv.innerHTML = "Please enter some ingredients.";
        return;
    }

    recipeDiv.innerHTML = "Finding recipe...";

    try {
        const response = await fetch("http://127.0.0.1:8000/create-recipe", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ ingredients })
        });

        const data = await response.json();

        if (response.ok) {
            recipeDiv.innerHTML = `<strong>Recipe:</strong> <br> ${data.recipe}`;
        } else {
            recipeDiv.innerHTML = `<strong>Error:</strong> ${data.detail}`;
        }
    } catch (error) {
        recipeDiv.innerHTML = `<strong>Network Error:</strong> Unable to fetch recipe.`;
    }
}
