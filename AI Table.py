from prettytable import PrettyTable

# Create the AI table
ai_table = PrettyTable()
ai_table.field_names = ["Name", "Type", "Description"]
ai_table.add_row(["Alexa", "Voice Assistant", "Developed by Amazon, used for voice-based interaction with devices"])
ai_table.add_row(["Siri", "Voice Assistant", "Developed by Apple, used for voice-based interaction with devices"])
ai_table.add_row(["Google Assistant", "Voice Assistant", "Developed by Google, used for voice-based interaction with devices"])
ai_table.add_row(["IBM Watson", "AI Platform", "Developed by IBM, used for natural language processing, speech recognition, and computer vision"])
ai_table.add_row(["OpenAI", "AI Research", "A research organization focused on developing safe artificial intelligence"])

# Print the AI table
print(ai_table)
