#!/usr/bin/env python3
# This is a shebang line which tells the system to run this file with Python 3

"""
Life Success Evaluator
A program that determines success through meaningful life questions
"""

line_seperator = "="*60

# Import the 'os' module - provides functions to interact with the operating system
import os
# Import the 'time' module - provides time-related functions like sleep and delays
import time

# Class defined for the LifeSuccessEvaluator which is the blueprint for the evaluator object
class LifeSuccessEvaluator:
    # The __init__ method is a constructor & runs automatically when we create an instance
    def __init__(self):
        # Initialize score to 0 at the start and is used to track how many points the user has earned
        self.score = 0
        # Initialize max_score to 0 at the start and is used to track the maximum possible points
        self.max_score = 0
        # Create an empty dictionary to store all question responses (key: question, value: yes/no)
        self.responses = {}
    
    #OPTIONAL 
    # Method defined to clear the terminal screen/command prompt screen otherwise I would end up with 
    # a massive command screen at the end after all the questions
    def clear_screen(self):
        # Check if the operating system is NOT Windows (name != 'nt')
        # If true, use 'clear' command (Unix/Mac), otherwise use 'cls' (Windows)
        os.system('clear' if os.name != 'nt' else 'cls')
    
    # Method to print text with color and a typewriter effect (character by character)
    def print_styled(self, text, color='green', delay=0.03):
        # Dictionary mapping color names to ANSI escape codes for terminal colors
        colors = {
            # Green color code for terminal text
            'green': '\033[92m',
            # Red color code for terminal text
            'red': '\033[91m',
            # Cyan (light blue) color code for terminal text
            'cyan': '\033[96m',
            # Yellow color code for terminal text
            'yellow': '\033[93m',
            # Magenta (purple) color code for terminal text
            'magenta': '\033[95m',
            # Reset code to return text to default terminal color
            'reset': '\033[0m'
        }
        
        # Loop through each character in the text string
        for char in text:
            # Print the character with the specified color, end='' means no newline
            # flush=True forces immediate output instead of buffering
            print(colors.get(color, '') + char + colors['reset'], end='', flush=True)
            # Pause for the specified delay time to create typewriter effect
            time.sleep(delay)
        # Print a newline at the end after all characters are displayed
        print()
    
    # Method to ask a yes/no question and record the response
    def ask_question(self, category, question, weight=1):
        # Docstring explaining what this method does
        """Ask a yes/no question and track the response"""
        # Add the question's weight to the maximum possible score
        self.max_score += weight
        
        # Print the category name in uppercase
        print(f"\n{category.upper()}")
        # Print a horizontal line of 60 dashes for visual separation
        print(line_seperator)
        # Print the question with spacing
        print(f"\n{question}")
        
        # Start an infinite loop that continues until valid input is received
        while True:
            # Get user input, remove whitespace, and convert to uppercase
            response = input("\n[Y]es / [N]o: ").strip().upper()
            # Check if response is one of the valid options
            if response in ['Y', 'YES', 'N', 'NO']:
                # Check if the response indicates "yes"
                is_yes = response in ['Y', 'YES']
                # If the answer is yes, add the weight to the user's score
                if is_yes:
                    self.score += weight
                # Store the response (True/False) in the responses dictionary
                self.responses[question] = is_yes
                # Return the boolean value and exit the function
                return is_yes
            # If input was invalid, prompt the user to enter Y or N
            print("Please enter Y or N")
    
    # Method to evaluate health and physical wellbeing
    def evaluate_health(self):

        """Health & Physical Wellbeing"""
        
        print("\n" + line_seperator)
        # Print the section title with cyan color and typewriter effect
        self.print_styled("💪 HEALTH & PHYSICAL WELLBEING", 'cyan', 0.02)
        print(line_seperator)
        
        # Ask a question about physical health and energy
        self.ask_question(
            "Physical Health",  # Category label
            "Do you feel physically healthy and energetic most days?" )
        # Ask a question about mental health
        self.ask_question(
            "Mental Health",  # Category label
            "Are you generally free from chronic stress or anxiety?" )
        # Ask a question about self-care habits
        self.ask_question(
            "Self-Care",  # Category label
            "Do you take time to care for your physical and mental health?")
        # Ask a question about sleep quality
        self.ask_question(
            "Sleep",  # Category label
            "Do you get enough quality sleep regularly?"  # The question
        )
    
    # Method to evaluate relationships and social connections
    def evaluate_relationships(self):
    
        """Relationships & Social Connection"""
        
        print("\n" + line_seperator)
        # Print the section title with magenta color and typewriter effect
        self.print_styled("❤️  RELATIONSHIPS & CONNECTION", 'magenta', 0.02)
        print(line_seperator)
        
        # Ask a question about meaningful relationships
        self.ask_question(
            "Close Relationships",  # Category label
            "Do you have meaningful relationships with people who care about you?" )
        # Ask a question about social support during difficult times
        self.ask_question(
            "Social Support",  # Category label
            "Do you feel supported when going through difficult times?" )
        # Ask a question about a regular connection with others'
        self.ask_question(
            "Connection",  # Category label
            "Do you regularly connect with friends or loved ones?" )
        # Ask a question about communication effectiveness
        self.ask_question(
            "Communication",  # Category label
            "Can you express your feelings and needs to others effectively?"  )
    
    # Method to evaluate purpose and personal growth
    def evaluate_purpose(self):
        """Purpose & Personal Growth"""
        
        print("\n" + line_seperator)
        # Print the section title with yellow colour and typewriter effect
        self.print_styled("🎯 PURPOSE & PERSONAL GROWTH", 'yellow', 0.02)
        print(line_seperator)
        
        # Ask a question about life's meaning and purpose with a higher weight (2 points)
        self.ask_question(
            "Life Purpose",  # Category label
            "Do you feel your life has meaning and purpose?",  
            weight=2  # This question is worth 2 points instead of 1
        )
        # Ask a question about working toward goals
        self.ask_question(
            "Goals",  # Category label
            "Are you working towards goals that matter to you?"  )
        # Ask a question about personal learning and growth
        self.ask_question(
            "Learning",  # Category label
            "Do you actively seek to learn and grow as a person?"  # The question
        )
        # Ask a question about living by personal values
        self.ask_question(
            "Values",  # Category label
            "Are you living in alignment with your core values?" )
    
    # Method to evaluate financial wellbeing and stability
    def evaluate_financial(self):
        """Financial Stability"""
        
        print("\n" + line_seperator)
        # Print the section title with green colour and typewriter effect
        self.print_styled("💰 FINANCIAL WELLBEING", 'green', 0.02)
        print(line_seperator)
        
        # Ask a question about affording basic needs
        self.ask_question(
            "Basic Needs",  # Category label
            "Can you comfortably afford your basic needs (food, shelter, healthcare)?" )
        # Ask a question about financial stress levels
        self.ask_question(
            "Financial Stress",  # Category label
            "Are you generally free from constant financial worry?" )
        # Ask a question about the ability to save and plan ahead
        self.ask_question(
            "Future Planning",  # Category label
            "Are you able to save or plan for your future?"  # The question
        )
    
    # Method to evaluate happiness and fulfilment
    def evaluate_happiness(self):
        """Happiness & Fulfillment"""
        
        print("\n" + line_seperator)
        # Print the section title with cyan colour and typewriter effect
        self.print_styled("😊 HAPPINESS & FULFILLMENT", 'cyan', 0.02)
        print(line_seperator)
        
        # Ask a question about experiencing joy with a higher weight (2 points)
        self.ask_question(
            "Daily Joy",  # Category label
            "Do you experience moments of joy or contentment regularly?", 
            weight=2  # This question is worth 2 points - happiness is a key indicator
        )
        # Ask a question about gratitude
        self.ask_question(
            "Gratitude",  # Category label
            "Do you feel grateful for aspects of your life?")
        # Ask a question about being present and mindful
        self.ask_question(
            "Present Moment",  # Category label
            "Can you enjoy the present moment without constant worry?")
        # Ask a question about optimism and hope
        self.ask_question(
            "Optimism",  # Category label
            "Do you generally feel hopeful about your future?")
    
    # Method to evaluate contribution and impact on others
    def evaluate_contribution(self):
        """Contribution & Impact"""
    
        print("\n" + line_seperator)
        # Print the section title with magenta colour and typewriter effect
        self.print_styled("🌟 CONTRIBUTION & IMPACT", 'magenta', 0.02)
        print(line_seperator)
        
        # Ask a question about making a positive impact
        self.ask_question(
            "Positive Impact",  # Category label
            "Do you feel you make a positive difference in others' lives?" )
        # Ask a question about community involvement
        self.ask_question(
            "Community",  # Category label
            "Are you part of a community or cause you care about?")
        # Ask a question about helping others
        self.ask_question(
            "Helping Others",  # Category label
            "Do you regularly help or support others in some way?" )
    
    # This is the SUCCESS CRITERION function 
    def Success(self):
        """Determines if the criteria for success have been met"""
        
        # Calculate the percentage: (points earned ÷ total possible points) × 100
        percentage = (self.score / self.max_score) * 100
        
        # Success criteria: 70% or higher across all dimensions
        # Returns True if percentage is 70 or above, False otherwise
        return percentage >= 70
    
    # This is the celebrate() function from your image - runs when Success() is True
    def celebrate(self):
        """Celebration for success, only displays if 
        they have scored 70 and above"""
                
        # Clear the terminal screen for a fresh display
        self.clear_screen()
        
        print("\n" + line_seperator)
        self.print_styled("🎉 SUCCESS ACHIEVED! 🎉", 'green', 0.05)
        print(line_seperator)
        
        # Calculate the user's percentage score
        percentage = (self.score / self.max_score) * 100
        
        # Display the score: earned points / total points (percentage)
        print(f"\n✨ You scored: {self.score}/{self.max_score} ({percentage:.1f}%)")
        print("\n" + line_seperator)
        
        # Print a congratulatory message in green colour
        self.print_styled("\nYou're living a successful life!", 'green', 0.02)
        print("""\nYou've cultivated strong foundations across multiple\ndimensions of wellbeing. 
        Keep nurturing these areas\nand continue to grow!""")
        
        print("\n" + line_seperator)
        # Print motivational bullet points
        motivation_message="""
        \n💪 Keep being awesome!
        \n🌟 Continue pursuing your goals!
        \n❤️ Cherish your relationships!
        \n🎯 Live with purpose!\n"""

        print(motivation_message)
        
    
    # This is the Try_Again() function which runs when Success() is False
    def Try_Again(self):
        """Encouragement to improve - if the user scored below 70"""

        self.clear_screen()
        print("\n" + line_seperator)
        # Print section title with yellow colour and slower typewriter effect
        self.print_styled("📈 ROOM FOR GROWTH", 'yellow', 0.05)
        print(line_seperator)
        
        # Calculate the user's percentage score
        percentage = (self.score / self.max_score) * 100
        
        # Display the score: earned points / total points (percentage)
        print(f"\n✨ You scored: {self.score}/{self.max_score} ({percentage:.1f}%)")
        print("\n" + line_seperator)
        
        # Print an encouraging message with cyan colour
        self.print_styled("\nEvery journey has its challenges.", 'cyan', 0.02)
        
        # Message to explain that success is about progress, not perfection
        encouraging_message = "\nSuccess isn't about being perfect—it's about progress.\nLet's identify areas where you can grow..."
        print(encouraging_message)
        
        # Show areas needing attention to help the user identify areas for improvement opportunities
        print("\n" + line_seperator + "\n💡 AREAS TO FOCUS ON:\n" + line_seperator)
        
        # Creates an empty list to store questions that were answered "no"
        improvement_areas = []
        # Loop through all stored responses (question and yes/no answer)
        for question, response in self.responses.items():
            # If the response was False (answered "no")
            if not response:
                # Add this question to the improvement areas list
                improvement_areas.append(question)
        
        # Loop through the first 5 improvement areas (or fewer if less than 5)
        # enumerate() adds a counter (i) starting at 1
        for i, area in enumerate(improvement_areas[:5], 1):
            # Print each improvement area with its number
            print(f"\n{i}. {area}")
        
        # If there are more than 5 improvement areas
        if len(improvement_areas) > 5:
            # Calculate how many additional areas weren't displayed
            # Print a message showing there are more areas to work on
            print(f"\n... and {len(improvement_areas) - 5} more areas")
    
    # Be_Awesome() function defined with a final motivational message
    def Be_Awesome(self):
        """Motivational closing"""

        print("\n" + line_seperator)
        # Print section title with magenta colour and slower typewriter effect
        self.print_styled("✨ REMEMBER ✨", 'magenta', 0.05)
        print(line_seperator)
        
        # Print motivational bullet points about growth and self-improvement
        final_message = """
        \n🌱 Growth takes time
        \n💪 Small steps lead to big changes
        \n🎯 Your worth isn't defined by a score
        \n❤️  You have the power to improve your life
        \n🌟 Every day is a new opportunity\n"""
        print(final_message+ line_seperator)
        # Print final encouraging message with green colour
        self.print_styled("\n🚀 You've got this! Keep going!", 'green', 0.03)
        print(line_seperator + "\n")
    
    # ===================================================================
    # Main method that runs the entire program - orchestrates everything
    # ===================================================================

    def run(self):
        """Main program flow """
        
        # Clear the terminal screen for a fresh start
        self.clear_screen()
        
        # Title Screen section
        print("\n" + line_seperator)
        # Print the program title with cyan colour and a  slower typewriter effect
        self.print_styled("LIFE SUCCESS EVALUATOR", 'cyan', 0.05)
        print(line_seperator)

        # Print instructions for the user
        instructions = """\nAnswer honestly to evaluate your success across
        \nthe key dimensions of a fulfilling life.\n"""
 
        print(instructions + line_seperator)
        
        # Wait for user to press ENTER before starting - pauses execution
        input("\nPress ENTER to begin...")
        
        # Evaluate all dimensions & call each evaluation method in sequence
        self.evaluate_health()  # Ask all health questions
        self.evaluate_relationships()  # Ask all relationship questions
        self.evaluate_purpose()  # Ask all purpose questions
        self.evaluate_financial()  # Ask all financial questions
        self.evaluate_happiness()  # Ask all happiness questions
        self.evaluate_contribution()  # Ask all contribution questions
        
        # Calculate results section
        print("\n" + line_seperator)
        # Print "calculating" message with yellow color
        self.print_styled("Calculating your results...", 'yellow', 0.05)
        # Pause for 1.5 seconds to build anticipation
        time.sleep(1.5)
        
        # If Success() returns True (user scored 70% or higher)
        if self.Success() == True:
            # Run the celebration function
            self.celebrate()
        # If Success() returns False (user scored below 70%)
        else:
            # Run the improvement suggestions function
            self.Try_Again()
            # Run the motivational closing function
            self.Be_Awesome()


#This is where the program executes on run
if __name__ == "__main__":
    # Create an instance of the LifeSuccessEvaluator class
    evaluator = LifeSuccessEvaluator()
    # Call the run() method to start the program
    evaluator.run()
