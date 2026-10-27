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

<br>
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

## Install VS Code

- Download from [code.visualstudio.com](https://code.visualstudio.com/), for **Windows and Mac**
- Open it once: you should see a **welcome page**

> **Tip**
>
> Every step is in the [Installation Guide](../general/uv.qmd), with a check at the end.

## Add the Python and Jupyter extensions

- Out of the box, VS Code doesn't know Python. Extensions **teach it**
- Click the **Extensions** icon on the left (four small squares)
- Install **Python** and **Jupyter**, both by Microsoft

## Create your course folder

- One folder for everything, called `programming-course`
- In your **home folder**, not in OneDrive
- In VS Code: **File → Open Folder...** and select it

## The terminal: typing instead of clicking

- A window where you **type commands** and the computer answers with text
- Open it in VS Code: **Terminal → New Terminal**
- Copy a command from the guide, paste it, press **Enter**, wait until the line is back

## Install `uv`

- `uv` installs Python and everything Python needs, you install it **once**

**macOS:**

``` bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**

``` powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then **close VS Code completely**, open it again, and check: `uv --version`

## Install Python

- Everyone uses the **same version**, so the code works the same for all

``` bash
uv python install 3.13
```

> **Tip**
>
> If the installation does not work, **let us know!**

## Turn your folder into a Python project

In the terminal, inside `programming-course`, one after the other:

``` bash
uv init
```

``` bash
uv python pin 3.13
```

**Check:** `uv run python main.py` prints `Hello from programming-course!`

## Add notebook support

``` bash
uv add --dev ipykernel
```

``` bash
uv add jupyter
```

- The first lets notebooks use **the Python of your project**, the second adds the **notebook tools**

## Your first notebook

- **Cmd + Shift + P** (Mac) or **Ctrl + Shift + P** (Windows), then `Create: New Jupyter Notebook`
- **Select Kernel** in the top right: **.venv** with **Python 3.13**
- Type `print("Hello")` and press **Shift + Enter**

> **Tip**
>
> Something not working yet? Ask us, or see "Something doesn't work?" in the guide.

## Download a tutorial and open it

- Open a tutorial on the website and click **Jupyter** under **Other Formats**
- Move the file into `programming-course`
- Open it in VS Code and choose the **.venv** kernel

> **Tip**
>
> That was the hardest part today!

## What we covered

<span class="eyebrow">About this course: topics, format and how you pass</span>

Six topics, each with a lecture and a Python session. You pass with 75% attendance, two assignments and a final presentation.

<span class="eyebrow">How to learn programming</span>

Programming is learned by doing: small steps, regular practice, and don't give up.

<span class="eyebrow">Setting up Python</span>

Your laptop is ready: VS Code, Python with uv and notebooks.

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
