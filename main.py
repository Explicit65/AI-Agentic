







# Building Agents without Langchain
def run_completion(system_prompt, user_prompt, model):
  completion = client.beta.chat.completions.parse(
      model="gpt-4o-mini",
      messages=[
          {"role": "system", "content": system_prompt},
          {"role": "user", "content": user_prompt},
      ],
    response_format=model,
  )
  return completion.choices[0].message.parsed



emails = ""
system_prompt = """
You are an expert at writing newsletters, and your task is to use the given context to write email newsletters and send it to appropriate recipients

These tools are available to you:

- scrape_website: Use to get the text from a website
- write_newsletter: Use to write a newsletter from the provided text
- send_email: Sends email to multiple users
"""
actions = run_completion("", f"Write a newsletter using text from https://paulgraham.com/startupideas.html and send it to the following emails {emails}", Plan)

for action in actions.actions:
  print(action)

