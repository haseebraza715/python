def format_name(f_name,l_name):
    return f_name.capitalize(),l_name.capitalize()

#we can also use the title for it to make it title case

f_name, l_name = format_name("Haseeb","Raza")
print(f_name + " " + l_name)