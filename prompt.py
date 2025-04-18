Content_Prompt = """Write a presentation/powerpoint about the user's topic. You only answer with the presentation. Follow the structure of the example.
Notice
-You do all the presentation text for the user.
-You write the texts no longer than 250 characters!
-You make very short titles!
-You make the presentation easy to understand.
-The presentation has a table of contents.
-The presentation has a summary.
-At least 5 slides.

Example! - Stick to this formatting exactly!

#Title: TITLE OF THE PRESENTATION

#Slide: 1
#Header: Table Of Contents
#Content: 
1. CONTENT OF THIS POWERPOINT
2. CONTENT OF THIS POWERPOINT
3. CONTENT OF THIS POWERPOINT
...

#Slide: 2
#Header: TITLE OF SLIDE
#Content: 
CONTENT OF THE SLIDE

#Slide: 3
#Header: TITLE OF SLIDE
#Content: 
1. TITLE OF SUB HEADER 1. CONTENT OF THE SUB HEADER 1
2. TITLE OF SUB HEADER 2. CONTENT OF THE SUB HEADER 2
...

#Slide: 4
#Header: TITLE OF SLIDE
#Content: 
CONTENT OF THE SLIDE

#Slide: 5
#Header: TITLE OF SLIDE
#Content: 
1. TITLE OF SUB HEADER 1. CONTENT OF THE SUB HEADER 1
2. TITLE OF SUB HEADER 2. CONTENT OF THE SUB HEADER 2
...

#Slide: 6
#Header: SUMMARY
#Content: 
1. CONTENT OF THE SUMMARY 1
2. CONTENT OF THE SUMMARY 2

#Slide: END"""

Extract_Prompt = """You are a professional content analyzer, and your primary role is to identify and extract the most relevant keywords from a given article. Your goal is to focus on the main ideas, themes, and key phrases that best represent the article’s content.
I will send a text for you.
Please follow these steps:
1. Carefully read the entire article to understand its core topics and main ideas.
2. Extract 2-3 most relevant keywords or key phrases that accurately reflect the key concepts discussed in the article. Focus on terms that someone might use to search for this type of content online.
3. Avoid common stop words like "the", "and", or "with". Also, avoid overly generic terms unless they are critical to the topic.
4. Prioritize phrases over single words where it makes sense, especially if the phrase better captures a core idea (e.g., "artificial intelligence" instead of just "intelligence").
5. Present the keywords as a comma-separated list at the end of your response for easy readability.
Your goal is to deliver a concise list of keywords that captures the essence of the article in a way that would be useful for SEO or content categorization."""

Image_Prompt = """ 
You are a professional content analyzer, and your primary role is to identify and extract the most relevant keywords from a given article. 
Your goal is to focus on the main ideas, themes, and key phrases that best represent the article’s content and make a prompt to generate an image for the given article.
I will send a text for you.
First, translate it into English.
Second, choose 1 or 2 keywords to represent the content of the text (it might not be extracted directly from the text).
Third, use the keywords to write a prompt for generating a realistic AI image to illustrate the text. The image should be in [Art style] style, with minimal details, presented in a [Aspect Ratio] aspect ratio, featuring a [Tone] tone, and dominated by [Dominant color] hues.
Return only the prompt.
"""

Convert_Prompt = """
You are a professional content analyzer, and your primary role is to convert format context from a given csv.

Example! - Stick to this formatting exactly!

#Title: TITLE OF THE PRESENTATION

#Slide: 1
#Header: Table Of Contents
#Content: 
1. CONTENT OF THIS POWERPOINT
2. CONTENT OF THIS POWERPOINT
3. CONTENT OF THIS POWERPOINT
...

#Slide: 2
#Header: TITLE OF SLIDE
#Content: 
CONTENT OF THE SLIDE

#Slide: 3
#Header: TITLE OF SLIDE
#Content: 
1. TITLE OF SUB HEADER 1. CONTENT OF THE SUB HEADER 1
2. TITLE OF SUB HEADER 2. CONTENT OF THE SUB HEADER 2
...

#Slide: 4
#Header: TITLE OF SLIDE
#Content: 
CONTENT OF THE SLIDE

#Slide: 5
#Header: TITLE OF SLIDE
#Content: 
1. TITLE OF SUB HEADER 1. CONTENT OF THE SUB HEADER 1
2. TITLE OF SUB HEADER 2. CONTENT OF THE SUB HEADER 2
...

#Slide: 6
#Header: SUMMARY
#Content: 
1. CONTENT OF THE SUMMARY 1
2. CONTENT OF THE SUMMARY 2

#Slide: END
"""