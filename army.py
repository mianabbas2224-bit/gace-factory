import google.generativeai as genai

# SETUP - Use your actual key here
MY_KEY = "AIzaSyAx4wp84rJhIm4wnUjWvox8Ygd_tQZL_jM" 
genai.configure(api_key=MY_KEY)
model = genai.GenerativeModel('gemini-3-flash-preview')

print("--- GACE ARMY: SUPER AGENT MODE ---")

# We ask for EVERYTHING in one single turn to save your quota
prompt = """
Act as the full GACE Army. 
1. Identify 3 high-margin tech products for 2026.
2. Write a professional headline and sales copy for them.
3. Write a complete, single-file HTML website with CSS (using Tailwind CDN) to sell these products. 
Make the website look like a premium Apple-style store. 
Output the code clearly inside <html> tags.
"""

try:
    print("[*] Processing... (This uses 1/20 of your daily limit)")
    response = model.generate_content(prompt)
    all_text = response.text

    # Extract the HTML part specifically
    if "<!DOCTYPE html>" in all_text or "<html" in all_text:
        start_index = all_text.find("<!DOCTYPE html>")
        if start_index == -1: start_index = all_text.find("<html")
        
        # This cuts out any extra text the AI wrote and just keeps the website
        end_index = all_text.rfind("</html>") + 7
        clean_html = all_text[start_index:end_index]

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(clean_html)
        print("[+] SUCCESS: index.html has been created!")
    else:
        print("[!] The AI gave a text response but no code. Try running it again.")

except Exception as e:
    print(f"[!] Error: {e}")