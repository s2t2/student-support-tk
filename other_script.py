# from TH on 4/16

from dotenv import load_dotenv
import requests
import json
import os
import tkinter

load_dotenv()

app_key = os.environ.get("my_app_key", "OOPS")
app_id = os.environ.get("my_app_id", "OOPS")

selected_recipes = []

#recipe_select_label = tkinter.Label(text="Select a recipe you would like to add from the dropdown:")
#recipe_select = tkinter.Listbox()
# nah, these show up way too early if defined up here...

def search_button_click():
    ##code to run search
    #search_value = entry_value.get()
    #request_url = f"https://api.edamam.com/search?q={search_value}&app_id={app_id}&app_key={app_key}"
    #response = requests.get(request_url)
    #parsed_response = json.loads(response.text)
    #
    #recipe_list = []
    #recipes = parsed_response["hits"]
    #for recipe in recipes:
    #    recipe_list.append(recipe["recipe"]["label"])
    #
    #add recipes to ListBox
    recipe_select_label = tkinter.Label(text="Select a recipe you would like to add from the dropdown:")
    recipe_select = tkinter.Listbox()

    recipe_list = ["Salad", "Sandwich", "Soup"]
    i = 1
    for recipe in recipe_list:
        recipe_select.insert(i, recipe)
        i = i + 1

    recipe_select_label.pack()
    recipe_select.pack()

def add_recipe_click(my_recipe_select):
    selection = my_recipe_select.curselection()
    print("ADDING RECIPE:", type(selection), selection)
    breakpoint()
    selected_recipes.append(my_recipe_select.get(selection)) #> tkinter.TclError: bad listbox index "": must be active, anchor, end, @x,y, or a number

#Initialize GUI

window = tkinter.Tk()

search_label = tkinter.Label(text="Enter recipe name or key words here:")

entry_value = tkinter.StringVar()

search = tkinter.Entry(textvariable=entry_value)

search_button = tkinter.Button(text="Search", command=search_button_click)

#add_button = tkinter.Button(text="Add Recipe", command=add_recipe_click)
recipe_select_label = tkinter.Label(text="Select a recipe you would like to add from the dropdown:")
recipe_select = tkinter.Listbox()
add_button = tkinter.Button(text="Add Recipe", command= lambda: add_recipe_click(recipe_select))
# https://stackoverflow.com/a/6921225/670433

print(selected_recipes)

search_label.pack()
search.pack()
search_button.pack()
add_button.pack()

#recipe_select_label = tkinter.Label(text="Select a recipe you would like to add from the dropdown:")
#recipe_select = tkinter.Listbox()

window.mainloop()

print("THE WINDOW HAS BEEN CLOSED")
