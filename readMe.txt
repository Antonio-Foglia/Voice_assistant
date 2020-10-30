*Chatbotter.ipynb is used to initiate the Chatbot in the current directory. The chatbot is then trained, and will use machine learning to speak to the user.

*Default sounds are stored in the sounds folder and used when needed

*Images of users are stored in the images folder 

*Main first calls on fr (__face_rec__.py) to take a picture of the user. If the users face is already present, the user will be welcomed, otherwise a new user will be initiated. If no face is found the program continues without a user. The names are saved in Json file (images.json).

*The inp function (__input__.py) records sound and converts it to an wav file.

*The recognise function (__recognise__.py) recognizes the text within the wav file using googles speech recognition library. It outputs a string of the text.

T*he what_is function (__what__.py) then tries to identify what the user wants. If none of the hardcoded preferred functions are identified, the chatbot is used through the chat function (__chat__.py).

*Outputs are managed by the say function (__output__.py) which converts strings to mp3 using the google text to speech library files and plays them. The function also takes in a  language parameter.

*The serie_a function (__seriea__.py) uses beautiful soup, pandas and requests to web-scrape for my teams result and return them to the player.

*The translate function (__translate__.py) uses google translate library to translate what the user wants. The text processing only translates what the user wants.

*The weather function (__weather__.py) uses a online weather API to provide the weather for the location specified by the user. It can provide really detailed info if needed. If no location is specified, the computer automatically looks at the computers IP dress to try to locate the users position and give the weather for that location.




