from db import *


def main():
    while True:
        print("\n🍽️  Welcome to the Recipe Manager! 📝")
        print("1. Add recipe")
        print("2. Get recipes")
        print("3. Get recipe")
        print("4. Delete recipe")
        print("5. Add recipe from API")
        print("6. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\n📝 Adding a New Recipe 🍲")
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ")
            instructions = input("Enter instructions: ")
            add_recipe(name, ingredients, instructions)
            print("✅ Recipe added successfully!")
        elif choice == "2":
            print("\n📋 Available Recipes 🍴")
            recipes = get_recipes()
            if recipes:
                for recipe in recipes:
                    print(f"{recipe.name}: {recipe.ingredients}")
            else:
                print("No recipes found.")
        elif choice == "3":
            print("\n🔍 Get Recipe Details 📖")
            name = input("Enter recipe name: ")
            recipe = get_recipe(name)
            if recipe:
                print(f"\n📌 {recipe.name} Recipe 🍽️")
                print(f"Ingredients: {recipe.ingredients}")
                print(f"Instructions: {recipe.instructions}")
            else:
                print("Recipe not found.")
        elif choice == "4":
            print("\n🗑️  Delete a Recipe 🚫")
            name = input("Enter recipe name to delete: ")
            if delete_recipe(name):
                print("✅ Recipe deleted successfully!")
            else:
                print("Recipe not found.")
        elif choice == "5":
            print("\n🔍 Adding Recipe from API 📡")
            name = input("Enter recipe name: ")
            recipe = add_recipe_api(name)
            if recipe:
                print(f"✅ Recipe '{recipe['strMeal']}' added from API.")
            else:
                print("Recipe not found in the API.")
        elif choice == "6":
            print("\n👋 Exiting Recipe Manager. Goodbye! 🍽️")
            break
        else:
            print("\n❌ Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
