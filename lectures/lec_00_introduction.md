---
title: Introduction
subtitle: 'Programming: Everyday Decision-Making Algorithms'
format:
  revealjs:
    footer: ' {{< meta title >}} | Dr. Nils Roemer | [Home](lec_00_introduction.qmd)'
    output-file: lec_00_presentation.html
---


## Today in one sentence

<span class="statement">In this course you learn how computer scientists approach everyday decisions, and how to turn these ideas into Python code.</span>

<span class="eyebrow">Why it matters</span>

More and more business decisions rely on data and algorithms. You don't need to become a programmer, but understanding how algorithms think, and writing a few lines of code yourself, makes you a better decision maker. No prior knowledge required.

## Roadmap

1.  <span class="roadmap-item future">About this course: topics, format and how you pass</span>
2.  <span class="roadmap-item future">How to learn programming</span>
3.  <span class="roadmap-item future">Setting up Python</span>

# <span class="flow">About this course: topics, format and how you pass</span>

## Six topics, one per session

- **I:** Optimal Stopping
- **II:** Explore & Exploit
- **III:** Caching
- **IV:** Scheduling
- **V:** Randomness
- **VI:** Computational Kindness

## Take part, it pays off

- **Participate actively**: it makes the course easier and more fun
- Inspired by the book <span class="highlight">Algorithms to Live By</span>[^1]
- All material is online: [courses.nilsroemer.com](https://courses.nilsroemer.com)

## Each session: lecture, then tutorial

- **Lecture:** we discuss an algorithm for everyday decisions
- **Tutorial:** step-by-step assignments, solved together in groups
- **Difficulty:** depends on your programming experience

> **Tip**
>
> No worries, we will help you out if you have any questions!

## How you pass

- **Pass/fail course** without exams
- <span class="highlight">75% attendance</span> required
- **Two assignments** on algorithmic problems from the course
- **Short final presentation** of your prototype in the last lecture
- You can work in groups of **up to three students**

## How to hand in assignments

- Each group submits **one solution** per assignment
- Hand in your **working notebooks**
- Due by the **end of the quarter**, earlier is better
- At least **50%** of the solutions have to be correct

## You learn Python in the tutorials

We will mostly **not cover Python during the lectures!**

<span class="question">Question:</span> Does anybody know why?

- The best way to learn is by **doing**
- Lectures focus on the decision-making algorithms
- You learn Python by <span class="highlight">doing the tutorials</span>

## Programming is like a new language

- At first it might be <span class="highlight">a little bit overwhelming</span>
- First you get used to it and learn words
- Later you apply it and see results
- Important: *Practice, practice, practice!*

## What you take home

- The <span class="highlight">basics of programming</span>
- **Algorithmic thinking**: how computer scientists approach a problem
- Methods you can **apply** to practical problems

## Why Python?

- **Simple syntax**: easy to read and to learn
- **Versatile**: web, data analysis, artificial intelligence
- **Big community**: help and documentation everywhere

## Learn first, then use AI

- In the tutorials, <span class="highlight">write the code yourself</span>: that's how you learn
- At the end of the course, you build a small project **with AI support**
- Until then: if you use AI, ask it to **explain**, not to solve

# <span class="flow">How to learn programming</span>

## Roadmap

1.  <span class="roadmap-item done">About this course: topics, format and how you pass</span>
2.  <span class="roadmap-item current">How to learn programming</span>
3.  <span class="roadmap-item future">Setting up Python</span>

## Three habits that work

1.  <span class="highlight">Be present</span>: attend the lecture and solve the tutorials
2.  <span class="highlight">Put in some work</span>: repeat code and try to understand it
3.  <span class="highlight">Do coding</span>: run code, play around, modify, and solve

## Don't give up!

- Programming is <span class="highlight">problem solving</span>, errors are normal
- Expect to **stretch** your comfort zone

<center>

<img src="../images/gif/lec00-intro.gif" width="480" height="360" alt="">

</center>

# <span class="flow">Setting up Python</span>

## Roadmap

1.  <span class="roadmap-item done">About this course: topics, format and how you pass</span>
2.  <span class="roadmap-item done">How to learn programming</span>
3.  <span class="roadmap-item current">Setting up Python</span>

## VS Code is where you write code

- Like **Word for text**, but for code: an app to **write, run and find mistakes** in code
- Apps like this are called <span class="highlight">IDEs</span> (Integrated Development Environments)
- We use VS Code for the **whole course**

## The terminal: typing instead of clicking

- A window where you **type a command**, press Enter, and the computer **answers with text**
- No menus, no buttons: the computer does exactly what you typed
- We need it only for the **setup**: a handful of commands, all in the guide to copy

## `uv` installs Python for us

- `uv` is a small **helper tool**: it installs Python and everything Python needs
- Everyone gets the **same Python version**, so code works the same on every laptop
- You install `uv` **once**, then it does the rest for you

## Notebooks mix text and code

- A notebook is a document with **text cells** and **code cells**
- You run a code cell, and the result appears **right below it**
- All tutorials are notebooks: **read, run, change, try again**

## Now we install together

Every step, every command, every click is in the guide:

<a href="../general/uv.qmd" class="guide-link"><strong>courses.nilsroemer.com/general/uv.html</strong></a>

Also linked on the course website, under Installation Guide.

- Follow the steps **in order**, don't skip any
- After each step: a small **check**
- We stop at four **checkpoints** and compare

## Checkpoint 1: VS Code is open with both extensions

- VS Code shows its **welcome page**
- Under **Extensions**, both **Python** and **Jupyter** say "Installed"

<a href="../general/uv.qmd#step-1-install-vs-code" class="guide-ref">Guide: Steps 1 and 2</a>

## Checkpoint 2: The terminal shows a version number for `uv`

- Your folder `programming-course` is open in VS Code
- A terminal is open at the bottom, and it answers to `uv` with a line like `uv 0.11.26`

<a href="../general/uv.qmd#step-3-create-your-course-folder" class="guide-ref">Guide: Steps 3 to 5</a>

## Checkpoint 3: You see Hello from programming-course!

- Python 3.13 is installed
- Your folder is a Python project, and the example program prints `Hello from programming-course!`

<a href="../general/uv.qmd#step-6-install-python" class="guide-ref">Guide: Steps 6 and 7</a>

## Checkpoint 4: Your first notebook shows Hello

- The notebook uses the **.venv** kernel with **Python 3.13**
- Below the cell with `print("Hello")`, you see `Hello`

<a href="../general/uv.qmd#step-8-add-notebook-support" class="guide-ref">Guide: Steps 8 and 9</a>

> **Tip**
>
> That was the hardest part today! Step 10 of the guide: open a tutorial as a notebook.

## What we covered

<span class="eyebrow">About this course: topics, format and how you pass</span>

Six topics, each with a lecture and a Python session. You pass with 75% attendance, two assignments and a final presentation.

<span class="eyebrow">How to learn programming</span>

Programming is learned by doing: small steps, regular practice, and don't give up.

<span class="eyebrow">Setting up Python</span>

Your laptop is ready: VS Code, Python installed with uv, and notebooks. Every step is in the Installation Guide.

## Why it matters

More and more business decisions rely on data and algorithms. You don't need to become a programmer, but understanding how algorithms think, and writing a few lines of code yourself, makes you a better decision maker.

## 

Learn by doing.

## 

Any questions

so far?

## After the break: Optimal Stopping

- The "Secretary Problem" and the 37% rule
- When to stop searching and make a decision
- Testing the rule ourselves with a small simulation

> **Note**
>
> **That's it for our introduction!**  
> Let's have a short break and then continue with our first topic.

# <span class="flow">Literature</span>

## Interesting literature to start

- Christian, B., & Griffiths, T. (2016). Algorithms to live by: the computer science of human decisions. First international edition. New York, Henry Holt and Company.[^2]

## Books on Programming

- Downey, A. B. (2024). Think Python: How to think like a computer scientist (Third edition). O'Reilly. [Free online](https://greenteapress.com/wp/think-python-3rd-edition/)
- Elter, S. (2021). Schrödinger programmiert Python: Das etwas andere Fachbuch (1. Auflage). Rheinwerk Verlag.

> **Note**
>
> Think Python is free online and a great start. Schrödinger programmiert Python is a playful alternative in German.

## More Literature

For more interesting literature, take a look at the [literature list](../general/literature.qmd) of this course.

[^1]: Christian, B., & Griffiths, T. (2016). Algorithms to live by: the computer science of human decisions. First international edition. New York, Henry Holt and Company.

[^2]: The main inspiration for this lecture. We have read it and discussed it in depth, always wanting to translate it into a course.
