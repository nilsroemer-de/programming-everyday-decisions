---
title: Tutorial V.I - Programming with AI
subtitle: 'Programming: Everyday Decision-Making Algorithms'
author: Dr. Nils Roemer
format:
  revealjs:
    footer: ' {{< meta title >}} | {{< meta author >}} | [Home](tut_05_01_llm.qmd)'
    output-file: tut_05_01_presentation.html
---


# <span class="flow">Programming with AI</span>

## Using AI to generate code

- Coding by hand is <span class="highlight">not the only way to generate code</span>
- Most likely, a lot of you have already used **ChatGPT**

. . .

<center>
<img src="../images/gif/tut05-llm.gif" width="400" height="400" alt="">
</p>
</center>

## 

How do

Large Language

Models work?

<span class="white">Photo by <a href="https://unsplash.com/@tvick">Taylor Vick</a> on Unsplash</span>

## Large Language Models (LLMs)

- Think of them like <span class="highlight">advanced pattern recognition systems</span>
- They have "read" **massive amounts of text**
- Books, websites, articles, code, and more
- Text is broken into **tokens**, parts of words or punctuation
- Based on patterns, they can **generate new text**

## Training LLMs

- Imagine learning a language by <span class="highlight">reading millions of books</span>
- Learns patterns in **how words and ideas connect** via tokens
- Interconnected nodes with **weights representing patterns**
- During training, these **weights are adjusted**
- Once trained, **applying** them takes much less ressources

. . .

> **Tip**
>
> Using a trained model is called **inference**.

## Pattern Recognition

- <span class="highlight">Not like a search engine!</span>
- When asked, it looks for **relevant patterns** it learned
- Like having a **huge library** in its "memory" to draw from
- It can find **patterns between concepts** and your question
- Knows only limited text at once (**context window**)

. . .

> **Warning**
>
> Managing **context windows** is crucial!

## Probability based responses

- After each written token, it predicts <span class="highlight">"what should come next?"</span>
- Like a advanced version of the **word prediction** on your phone
- Chooses the **most likely next token** based on training
- <span class="highlight">But can't actually "think" or "understand" like humans</span>

## Limitations

- **No true understanding** of cause and effect[^1]
- Sometimes **makes mistakes or "hallucinates"**
- Mostly only knows what it **was trained on**[^2] and can **reflect biases**
- No emotional understanding (but <span class="highlight">can simulate responses!</span>)[^3]

## Impact on Jobs

- <span class="question">Question</span>: What do you think about their impact on jobs?
- <span class="question">Question</span>: What are the implications for us?
- <span class="question">Question</span>: Can we use them to our advantage?

. . .

> **Warning**
>
> If you use free models, be aware that your prompts are going to be used by the providers and are not private. But for learning and experimenting, this should be no issue.

## A Great Overview by 3Blue1Brown

- **Greg Sanderson provides an excellent explanation of LLMs**
- Great starting point to understand LLMs
- Check out his [YouTube channel, 3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw) for more

<iframe src="https://www.youtube-nocookie.com/embed/LPZh9BOjkQs" title="But what is a GPT? Visual intro to transformers (3Blue1Brown)" width="560" height="315" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>

# <span class="flow">AI Coding Partner</span>

## What is GitHub Copilot?

<span class="highlight">GitHub Copilot</span> is an *AI pair programmer* that helps you write code faster and with less effort.

. . .

**Think of it as:**

- An autocomplete for entire lines or blocks of code
- A coding assistant that understands context
- A learning tool that shows you coding patterns

. . .

> **Note**
>
> Copilot uses AI trained on billions of lines of public code to suggest completions.

. . .

> **Tip**
>
> There are alternative like Zed or Cursor, but you can use Copilot for free as student.

## Used autocomplete before?

. . .

When you type on your phone, it suggests the next word.

. . .

**GitHub Copilot does the same for code:**

- You write a comment describing what you want
- Copilot suggests the code to do it
- You accept, modify, or reject the suggestion

. . .

<span class="highlight">It's autocomplete but much better then what you are used to</span>

## Why Use Copilot?

<span class="highlight">Benefits you while learning and working with Python:</span>

- **Faster coding:** Less time typing boilerplate code
- **Learn patterns:** See how experienced programmers code
- **Understand syntax:** Get correct syntax without memorizing
- **Stay in flow:** Focus on logic, not syntax errors

. . .

> **Tip**
>
> Especially helpful when you know **WHAT** you want to do but forget **HOW** to do it.

## When should you use Copilot?

. . .

<span class="highlight">Good uses of Copilot</span>

- Understanding Python syntax you forgot
- Writing repetitive or boilerplate code
- Getting unstuck on simple problems
- Exploring different approaches

## What shouldn't you do with Copilot?

. . .

<span class="highlight">Not so good uses of Copilot</span>

- Replacing learning fundamentals
- Accepting code you don't understand
- Skipping practice exercises
- Copy-pasting without reading

. . .

<span class="highlight">Always understand what Copilot suggests before accepting!</span>

. . .

**But of course I know you will not do that ;)**

## Accept without reading?

. . .

<span class="highlight">Copilot might suggest code that:</span>

- Works but uses concepts you haven't learned yet
- Contains subtle bugs or edge cases
- Doesn't match your specific requirements
- Uses inefficient approaches
- Introduce dangerous code in your project

. . .

> **Warning**
>
> Dangerous code can lead to security vulnerabilities, data loss, or other issues. In the context of this lecture it should be no issue, but in companies it can be one!

## My take: Just be careful, ok?

<span class="highlight">Your code, your responsibility:</span>

1.  **Read** the suggestion carefully
2.  **Understand** what it does
3.  **Test** it with examples
4.  **Modify** if needed

. . .

> **Warning**
>
> Don't accept code blindly, especially later if things are more complicated.

# <span class="flow">Getting Started with Copilot</span>

## Get Free Access

**GitHub Student Developer Pack** gives you free Copilot access!

. . .

1.  Go to [education.github.com/pack](https://education.github.com/pack)
2.  Sign up with your university email
3.  Verify your student status
4.  Wait for approval (usually 1-2 days)
5.  Login into your account in VS Code

. . .

> **Note**
>
> You'll need a GitHub account. Create one at [github.com](https://github.com) if you don't have one.

## Verifying Copilot is Working

1.  Create a new Python file (`.py`) and type something
2.  Wait 1-2 seconds

. . .

**If working, you'll see:**

- Gray "ghost text" suggesting code
- Press `Tab` to accept
- Press `Esc` to reject

. . .

> **Tip**
>
> Try to get copilot running on your own until next session.

# <span class="flow">Summary</span>

## Key Takeaways

1.  **GitHub Copilot is a tool:** You still need to learn fundamentals
2.  **Understand before accepting:** Read every suggestion carefully
3.  **Use it strategically:** Syntax help yes, thinking replacement no
4.  **Get free access:** GitHub Student Developer Pack
5.  **Practice:** The more you use it, the more helpful it becomes

[^1]: <https://www.anthropic.com/research/tracing-thoughts-language-model>

[^2]: This can partially be improved by using context from the internet.

[^3]: [User can get attached to talking to models](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/)
