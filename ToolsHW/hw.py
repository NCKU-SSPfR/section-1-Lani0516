import webbrowser, sys

video_url: str = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def input_math():
    while True:
        user_input = input("1 times 1 = ? ")

        if int(user_input) == 1:
            open_video()
            break
        elif user_input == "exit":
            sys.exit()
        else:
            print("Wrong! Try again.")

def open_video():
    webbrowser.open(video_url)
    return

input_math()