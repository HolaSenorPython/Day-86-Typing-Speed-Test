from tkinter import *
from tkinter import ttk
from prompts import prompt_list
from colors import rainbow_colors
import random
#---------------------------------CONSTANTS----------------------------------#
still_typing = None
MAROON = "#6D2323"
RED = "#A31D1D"
BEIGE = "#E5D0AC"
BROWN = "#c3923c"
LIGHT_YELLOW = "#FEF9E1"
WHITE = "white"
BYZANTIUM = "#702963"
FONT_NAME = "Comic Sans MS"
TIMER = 0 # Use this for timer count later
#------------------------------USEFUL FUNCTIONS------------------------------#
# Clears the home screen
def clear_home():
    frame.grid_forget()
    title_lbl.grid_forget()
    desc_label.grid_forget()
    canvas.grid_forget()
    start_btn.grid_forget()
    about_btn.grid_forget()
    canvas3.grid_forget()

# Returns home screen
def return_home():
    frame.grid(row=3, column=1, columnspan=2)
    title_lbl.grid(row=0, column=1)
    desc_label.grid(row=1, column=1)
    canvas.grid(row=2, column=1)
    start_btn.grid(row=3, column=1, padx=10)
    about_btn.grid(row=3, column=2, padx=10)
    canvas3.grid(row=4, column=1, pady=10)

# Returns all the home elements bg color to beige when they are brought back
def return_home_color():
    screen.config(bg=BEIGE)
    frame.config(style="TFrame")
    title_lbl.config(bg=BEIGE)
    desc_label.config(bg=BEIGE)
    canvas.config(bg=BEIGE)
    start_btn.config(bg=MAROON)
    about_btn.config(bg=MAROON)
    canvas3.config(bg=BEIGE)

def clear_current_ui(*args):
    # Delete every widget currently on page
    for arg in args:
        delete_widget(arg)

# Function to delete a widget
def delete_widget(widget):
    widget.destroy()

# Get a random prompt from the prompt data
def random_prompt():
    selected_prompt = random.choice(prompt_list)
    return selected_prompt

# ChatGPT helped with this part, but I broke it down so I can learn. 😣
def rainbow_text(text, colors, index=0):
    # Change the color
    text.config(fg=colors[index])
    # Get the next color in the list, but if you hit the end, loop back to the beginning
    # This works because if a list is 3 items long, and you're at index 2, (2 + 1) = 3, 3 % 3 is 0, and we are back
    next_one = (index + 1) % len(colors)
    # After 500 milliseconds, do this function again, with the same inputs as last time and the rainbow colors list
    text.after(100, rainbow_text, text, rainbow_colors, next_one)

# Count-up timer
def count_up(text):
    global TIMER
    if still_typing: # If still typing count
        TIMER += 1
        text.config(text=f"{TIMER}")
        screen.after(1000, count_up, text)

# Check if the user made an error in typing the prompt
def accuracy_check(prompt, users_input):
    clean_prompt = prompt.replace('\n', ' ').replace('"', '').strip() # Replace new line with space, quotes with nothing
    clean_user_input = users_input.strip()
    print(f"Raw prompt: {prompt}")
    print(f"Cleaned prompt: {clean_prompt}")
    print(f"Users input: {users_input}")
    if clean_user_input == clean_prompt:
        return True
    else:
        return False

# Calculate WPM
def wpm_calculator(seconds, users_input):
    words = (len(users_input) / 5)
    minutes = seconds / 60
    wpm = words / minutes
    return round(wpm)

# Figure out which image to show based on WPM
def which_image(wpm):
    if 0 <= wpm <= 20:
        return 'images/silva.png'
    elif 21 <= wpm <= 40:
        return 'images/giroud.png'
    elif 41 <= wpm <= 60:
        return 'images/henderson.png'
    elif 61 <= wpm <= 80:
        return 'images/saka2.png'
    elif wpm >= 81:
        return 'images/mbappe.png'

# Figure out which description to show based on WPM
def which_desc(wpm):
    if 0 <= wpm <= 20:
        return 'Very Slow'
    elif 21 <= wpm <= 40:
        return 'Slow'
    elif 41 <= wpm <= 60:
        return 'Average'
    elif 61 <= wpm <= 80:
        return 'Fast'
    elif wpm >= 81:
        return 'VERY FAST!'

#--------------------------------------BUTTON COMMANDS---------------------------------#
# Show about page UI
def about_ui():
    # Clear home screen
    clear_home()

    # Make about page UI
    about_title_lbl = Label(text="About page!", bg=BEIGE, fg=RED, font=(FONT_NAME, 32, "bold"))
    about_title_lbl.grid(row=0, column=1)

    about_desc = Label(text="My name is Elisha N. (HolaSenorPython on Github), and the\n"
                            " idea for this app came as part of Angela Yu's Python course.\n"
                            "This is our assignment, unaided by her, for Day 86 out of 100. I\n"
                            "hope you enjoy, and that this app is a helpful way for you to gage\n"
                            "typing speed.", bg=BEIGE, fg=RED, font=(FONT_NAME, 16))
    about_desc.grid(row=1, column=1, pady=10)

    canvas2 = Canvas(width=256, height=256, highlightthickness=0, bg=BEIGE)
    saka_path = 'images/saka.png'
    canvas2.saka_img = PhotoImage(file=saka_path) # Make an attribute so tkinter doesnt lose it
    canvas2.create_image((128, 128), image=canvas2.saka_img)
    canvas2.grid(row=2, column=1, pady=10)

    done_reading = Button(text="I'm done reading!", bg=MAROON, fg=WHITE, relief="flat", highlightthickness=0,
                          font=(FONT_NAME, 20), command=lambda: [clear_current_ui(about_title_lbl, about_desc, done_reading, canvas2), return_home()])
    done_reading.grid(row=3, column=1, columnspan=2, pady=10)

# Show start typing UI
def start_typing_ui():
    # Clear home page
    clear_home()
    # Get a random prompt
    prompt = random_prompt()
    # Make the UI like buttons and stuff
    frame2 = ttk.Frame(screen, padding=10)
    frame2.grid(row=3, column=1, columnspan=3)

    ur_prompt_lbl = Label(text="Your prompt:", bg=BEIGE, fg=RED, font=(FONT_NAME, 32, "bold"))
    ur_prompt_lbl.grid(row=0, column=1)

    prompt_lbl = Label(text=f'"{prompt}"', bg=BEIGE, fg=BYZANTIUM, font=(FONT_NAME, 14))
    prompt_lbl.grid(row=1, column=1)

    ready_or_not = Label(text="Are you ready?", bg=BEIGE, fg=RED, font=(FONT_NAME, 16, "bold"))
    ready_or_not.grid(row=2, column=1)

    yes_btn = Button(frame2, text="Yes", bg=MAROON, fg=WHITE, relief="flat",
                     highlightthickness=0, font=(FONT_NAME, 14), command=lambda: yes_ready(ready_or_not, frame2, ur_prompt_lbl, prompt_lbl, prompt))
    yes_btn.grid(row=3, column=1, padx=10)

    no_btn = Button(frame2, text="No", bg=MAROON, fg=WHITE, relief="flat",
                    highlightthickness=0, font=(FONT_NAME, 14), command=not_ready)
    no_btn.grid(row=3, column=2, padx=10)

    return_home_btn = Button(frame2, text="Return Home", bg=BYZANTIUM, fg=WHITE, relief="flat",
                             highlightthickness=0, font=(FONT_NAME, 14), command=lambda: [clear_current_ui(frame2, ur_prompt_lbl, prompt_lbl,
                                                                                                           ready_or_not, yes_btn, no_btn, return_home_btn), return_home()])
    return_home_btn.grid(row=3, column=3, padx=10)

# Show ill wait message if user clicks no
def not_ready():
    ill_wait = Label(text="Ok. Take 3 seconds to read your\nprompt and"
                          " let me know.", bg=BEIGE, fg=BYZANTIUM, font=(FONT_NAME, 16, "bold"))
    ill_wait.grid(row=4, column=1)
    ill_wait.after(3000, delete_widget, ill_wait) # After 3 seconds delete the widget

def yes_ready(ready_lbl, the_frame, ur_prompt_lbl, the_prompt, real_prompt):
    global still_typing
    still_typing = True # Boolean to check against to stop rainbow text, and change label
    # Delete the 3 buttons on screen
    delete_widget(the_frame)
    # Make new brown frame to place timer in later
    frame2 = ttk.Frame(screen, padding=10, style="Brown.TFrame")
    frame2.grid(row=5, column=1, columnspan=3)
    # Make the entry for user to type in, duh
    users_input = Entry(width=50)
    users_input.grid(row=3, column=1, columnspan=2, pady=10)
    users_input.focus_set()
    # Make the 'I'm Done' button
    done_typing_btn = Button(text="I'm done typing!", bg=MAROON, fg=WHITE, highlightthickness=0,
                         relief="flat", font=(FONT_NAME, 16), command=lambda: done_typing(TIMER, users_input.get(), real_prompt,
                                                                                          frame2, users_input, timer_lbl, actual_time, seconds_lbl, ur_prompt_lbl, the_prompt, done_typing_btn, ready_lbl))
    done_typing_btn.grid(row=4, column=1, pady=10)
    # Make timer label and actual time, and seconds label
    timer_lbl = Label(frame2, text="Timer:", bg=BROWN, fg="black", font=(FONT_NAME, 22))
    timer_lbl.grid(row=5, column=1)
    actual_time = Label(frame2, text=f"{TIMER}", bg=BROWN, fg="black", font=(FONT_NAME, 32, "bold"))
    actual_time.grid(row=5, column=2, padx=30)
    seconds_lbl = Label(frame2, text="sec", bg=BROWN, fg="black", font=(FONT_NAME, 14))
    seconds_lbl.grid(row=5, column=3)
    # Make start button rainbow, make all bgs match screen
    ready_lbl.config(text="Start Typing.", bg=BROWN)
    ur_prompt_lbl.config(bg=BROWN)
    the_prompt.config(bg=BROWN)
    if still_typing: # If we are still typing...
        screen.config(bg=BROWN) # make bg a little darker
        rainbow_text(ready_lbl, rainbow_colors)
        screen.after(1000, count_up,actual_time) # START THE COUNTER!

# If user is done typing (presses button) do this
def done_typing(seconds, user_input, prompt, frame2, le_entry, timer_lbl, time, sec_lbl, the_prompt_lbl, real_prompt, done_typing_btn, ready_lbl):
    global still_typing
    is_accurate = accuracy_check(prompt, user_input)
    if not is_accurate:
        show_error()
        still_typing = True
    else:
        still_typing = False
        users_wpm = wpm_calculator(seconds, user_input) # Get user WPM
        frame3 = ttk.Frame(screen, padding=15, style="Brown.TFrame")
        frame3.grid(row=6, column=1, columnspan=2)
        your_wpm_is = Label(frame3, text="Your WPM is...", bg=BROWN, fg="black", font=(FONT_NAME, 26, "bold"))
        your_wpm_is.grid(row=6, column=1)
        wpm = Label(frame3, text=f"{users_wpm}", bg=BROWN, fg="black", font=(FONT_NAME, 36, "bold"))
        wpm.grid(row=6, column=2, padx=30)
        canvas4 = Canvas(highlightthickness=0, width=256, height=256, bg=BROWN)
        image_path = which_image(users_wpm) # Image path depends on their speed
        speed_desc = which_desc(users_wpm) # Desc depends on speed
        canvas4.ready_img = PhotoImage(file=image_path)
        canvas4.create_image(128, 128, image=canvas4.ready_img)
        canvas4.grid(row=7, column=1, pady=10)
        speed_desc_lbl = Label(text=f"Your speed was: {speed_desc}", bg=BROWN, fg=BYZANTIUM, font=(FONT_NAME, 20, "bold"))
        speed_desc_lbl.grid(row=8, column=1)
        return_home_btn = Button(text="Return Home!", bg=BYZANTIUM, fg=WHITE, font=(FONT_NAME, 14), relief="flat",
                                 highlightthickness=0, command=lambda: [clear_current_ui(frame3, canvas4, speed_desc_lbl,
                                                                                         your_wpm_is, wpm, frame2, le_entry,
                                                                                         timer_lbl, time, sec_lbl, the_prompt_lbl, real_prompt,
                                                                                         done_typing_btn, return_home_btn, ready_lbl), return_home_color(), return_home()])
        return_home_btn.grid(row=9, column=1, pady=10)

# If a user makes a mistake in typing the prompt
def show_error():
    error_lbl = Label(text="Error: You mistyped something. Your input\n"
                           "doesn't match the prompt.", bg=BROWN, fg=RED, font=(FONT_NAME, 16))
    error_lbl.grid(row=6, column=1, pady=10)
    error_lbl.after(1000, delete_widget, error_lbl)

#-----------------------------HOME SCREEN and UI SETUP-----------------------#
screen = Tk()
screen.title("Typing Speed Test App")
screen.minsize(width=610, height=700)
screen.config(bg=BEIGE, padx=50, pady=50)

style = ttk.Style()
# Default frame bg color
style.configure("TFrame", background=BEIGE)
style.configure("Brown.TFrame", background=BROWN) # Brown Frame color
# Make the labels, buttons frames, etc.
frame = ttk.Frame(screen, padding=15)
frame.grid(row=3, column=1, columnspan=2)

title_lbl = Label(text="Typing Speed Test App", bg=BEIGE,
                  fg=RED, font=(FONT_NAME, 32, "bold"))
title_lbl.grid(row=0, column=1)

desc_label = Label(text="This app is meant for you to gage your\n"
                        "typing speed given a prompt.", bg=BEIGE, fg=RED, font=(FONT_NAME, 16))
desc_label.grid(row=1, column=1)

canvas = Canvas(width=128, height=128, bg=BEIGE, highlightthickness=0)
emoji_img_path = 'images/typing_emoji.png'
typing_emoji_img = PhotoImage(file=emoji_img_path)
canvas.create_image((64, 64), image=typing_emoji_img)
canvas.grid(row=2, column=1)

start_btn = Button(frame, text="Start Typing!", bg=MAROON, fg=WHITE, font=(FONT_NAME, 20),
                   relief="flat", highlightthickness=0, command=start_typing_ui)
start_btn.grid(row=3, column=1, padx=10)

about_btn = Button(frame, text="About Page", bg=MAROON, fg=WHITE, font=(FONT_NAME, 20),
                   relief="flat", highlightthickness=0, command=about_ui)
about_btn.grid(row=3, column=2, padx=10)

canvas3 = Canvas(width=256, height=256, bg=BEIGE, highlightthickness=0)
mbappe_glasses_path = 'images/mbappe_glasses.png'
mbappe_glasses_img = PhotoImage(file=mbappe_glasses_path)
canvas3.create_image((128, 128), image=mbappe_glasses_img)
canvas3.grid(row=4, column=1, pady=10)


screen.mainloop()