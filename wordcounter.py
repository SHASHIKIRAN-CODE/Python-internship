# WORD COUNTER

#INPUT OF THE USER
def get_user_input():
 user=input("ENTER A SENTENCE OR A PARAGRAPH : ")
 return user 

# LOGIC OF COUNTING WORDS 
def count_words(count):
 words=count.split()
 return  len(words)

# ERROR HANDLING 
try:
        # GET USER INPUT
        user_text = get_user_input()
        
        # CHECK FOR EMPTY INPUT
        if not user_text.strip():
            print("Error: Input cannot be empty. Please try again.")
         
        
        # COUNT THE WORDS
        word_count = count_words(user_text)
        
        # DISPLAY THE WORD COUNT 
        print(f"Word Count: {word_count}")
    
except Exception as e:
        # CATCH ANY UNEXPECTED ERRORS AND DISPLAY A FRIENDLY MESSAGE 
        print("An unexpected error occurred. Please try again later.")
        print(f"Error Details: {str(e)}")
        