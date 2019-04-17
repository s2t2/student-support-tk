
import tkinter

selected_recipes = []

def search():
    print("SEARCH TERM:", search_box.get())

    # TODO: clear previous options
    recipe_select.insert(1, "Salad")
    recipe_select.insert(2, "Sandwich")
    recipe_select.insert(3, "Soup")
    print("DROPDOWN OPTIONS HAVE BEEN POPULATED...")

    recipe_select_lbl.pack()
    recipe_select.pack()
    recipe_select_btn.pack()
    print("DROPDOWN ELEMENTS HAVE BEEN PACKED")

def add_recipe():
    #selected_recipes.append(recipe_select.get(recipe_select.curselection())) #> tkinter.TclError: bad listbox index "": must be active, anchor, end, @x,y, or a number
    #print("CUR SEL:", recipe_select.curselection())
    #recipe = recipe_select.get(recipe_select.curselection())
    recipe = "MY RECIPE"

    selected_recipes.append(recipe)
    print("ADDED RECIPE. COUNT:", len(selected_recipes))

if __name__ == "__main__":

    window = tkinter.Tk()
    print("THE WINDOW HAS BEEN OPENED")

    search_lbl = tkinter.Label(text="Enter recipe name or key words here:")
    search_box = tkinter.Entry(textvariable=tkinter.StringVar())
    search_btn = tkinter.Button(text="Search", command=search)
    print("THE SEARCH ELEMENTS HAVE BEEN INITIALIZED")

    search_lbl.pack()
    search_box.pack()
    search_btn.pack()
    print("THE SEARCH ELEMENTS HAVE BEEN ADDED TO THE WINDOW")

    recipe_select_lbl = tkinter.Label(text="Select a recipe you would like to add from the dropdown:")
    recipe_select = tkinter.Listbox()
    recipe_select_btn = tkinter.Button(text="Add Recipe", command=add_recipe)
    print("DROPDOWN ELEMENTS HAVE BEEN INITIALIZED")

    window.mainloop()
    print("THE WINDOW HAS BEEN CLOSED")
