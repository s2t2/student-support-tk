
import tkinter

selected_recipes = []

#def search2(my_dropdown, my_dropdown_label):
#    my_dropdown_label.pack()
#    my_dropdown.insert(1, "Salad")
#    my_dropdown.insert(2, "Sandwich")
#    my_dropdown.insert(3, "Soup")
#    my_dropdown.pack()

def search():
    recipe_select.insert(1, "Salad")
    recipe_select.insert(2, "Sandwich")
    recipe_select.insert(3, "Soup")
    recipe_select_lbl.pack()
    recipe_select.pack()
    recipe_select_btn.pack()
    print("SEARCHING AND POPULATING DROPDOWN OPTIONS...")

def add_recipe_click():
    #selected_recipes.append(recipe_select.get(recipe_select.curselection())) #> tkinter.TclError: bad listbox index "": must be active, anchor, end, @x,y, or a number
    selected_recipes.append("MY RECIPE")

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
    recipe_select_btn = tkinter.Button(text="Add Recipe", command=add_recipe_click)
    print("DROPDOWN ELEMENTS HAVE BEEN INITIALIZED")

    #recipe_select_btn.pack()

    window.mainloop()
    print("THE WINDOW HAS BEEN CLOSED")
