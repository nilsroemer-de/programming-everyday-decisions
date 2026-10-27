---
title: 'Lecture VI: Computational Kindness'
subtitle: 'Programming: Everyday Decision-Making Algorithms'
format:
  revealjs:
    footer: ' {{< meta title >}} | Dr. Nils Roemer | [Home](lec_06_kindness.qmd)'
    output-file: lec_06_presentation.html
---


## Today in one sentence

<span class="statement">The best algorithms don't just solve a problem, they make life easier and fairer for the people affected.</span>

<span class="eyebrow">Why it matters</span>

"When works for you?" sounds polite but hands the work to the other person. Proposing two concrete slots is kinder. Companies face the same question at scale: how to design processes, products and automated decisions that are easy and fair for customers and colleagues.

## Roadmap

1.  <span class="roadmap-item future">Looking back: five ideas for better decisions</span>
2.  <span class="roadmap-item future">Computational kindness: easy and fair for others</span>
3.  <span class="roadmap-item future">Looking ahead: where to go from here</span>

# <span class="flow">Looking back: five ideas for better decisions</span>

## Five ideas from this course

- **Optimal stopping:** <span class="highlight">when to stop looking</span>
- **Explore and exploit:** <span class="highlight">balance</span> the new and the known
- **Caching:** keep what you use close, <span class="highlight">let go of the rest</span>
- **Scheduling:** your goal decides <span class="highlight">your order</span>
- **Randomness:** simulate what you <span class="highlight">can't calculate</span>

## Looking back: five ideas for better decisions

<span class="eyebrow">What we covered</span>

<span class="statement">Optimal stopping, explore and exploit, caching, scheduling and randomness give you a toolkit for everyday decisions.</span>

# <span class="flow">Computational kindness: easy and fair for others</span>

## Roadmap

1.  <span class="roadmap-item done">Looking back: five ideas for better decisions</span>
2.  <span class="roadmap-item current">Computational kindness: easy and fair for others</span>
3.  <span class="roadmap-item future">Looking ahead: where to go from here</span>

## <span class="invert-font">Computational Kindness</span>

<span class="invert-font"><span class="highlight">Question:</span> **An idea what that is?**</span>

- Idea of introducing <span class="highlight">empathy in algorithms</span>
- **Consider human cognitive load and limitations**
- Making choices that **reduce mental burden** for others
- Creating systems that are **easy to understand and interact**

## Propose two slots instead of asking "when are you free?"

- <span class="highlight">Propose specific times!</span>
- Don't ask "when are you free?"
- **Reduces** cognitive load for others
- **Transforms** an open-ended problem

> **Important**
>
> **Now a simple yes/no decision!**

## Say what you prefer

- <span class="highlight">Be explicit rather than implicit</span>
- Provide **clear** options instead
- **Avoid** open-ended questions
- State your **preferences**

> **Important**
>
> **Avoid** deferring → "I'm fine with <span class="highlight">whatever</span>"!

## "I'm free whenever" is not helpful

- "I'm free whenever" <span class="highlight">seems helpful</span>
- <span class="highlight">But it is not!</span>

<!-- -->

- Forces others to **consider all possibilities**
- **Increases** cognitive load
- Makes decision-making **more complex**

## Four principles of computational kindness

1.  **Reduce Options**: Fewer choices lead to <span class="highlight">better decisions</span>
2.  **Be Explicit**: Clear constraints <span class="highlight">help</span> others decide
3.  **Consider Cognitive Load**: Design interactions minimizing <span class="highlight">mental effort</span> for others
4.  **Make Decisions**: <span class="highlight">Taking responsibility</span> can be kind

## Biased data leads to biased decisions

- Algorithms increasingly decide **about people**: credit, job ads, CV screening
- They learn from **historical data**, including its <span class="highlight">biases</span>
- Amazon dropped a CV-screening tool that downgraded CVs mentioning "women's"[^1]

Kindness also means thinking about the **people affected** by our algorithms.

## Where bias comes from

- **Data:** some groups are missing (<span class="highlight">selection bias</span>, Lecture V)
- **Objective:** optimizing only speed or profit ignores who bears the errors
- **Feedback loops:** decisions shape the next data[^2]

Fairness is a design decision: **test** outcomes for groups, **explain** decisions, keep a **human** in the loop.

## Three questions before you deploy an algorithm

<span class="question">Question:</span> **Before you deploy an algorithm, ask:**

- Who is affected, and who is **missing** in the data?
- Can a person **understand and contest** the decision?
- Does it **reduce or add burden** for the people involved?

## Your turn: be kind in three situations

<span class="highlight">Think about it:</span> **How could you apply computational kindness here?**

- Planning a **group dinner** with friends
- Asking your professor for **thesis feedback**
- Coordinating a **team project** at work

## Computational kindness: easy and fair for others

<span class="eyebrow">What we covered</span>

<span class="statement">Good algorithms reduce the burden for others and treat people fairly. Biased data leads to biased decisions.</span>

# <span class="flow">Looking ahead: where to go from here</span>

## Roadmap

1.  <span class="roadmap-item done">Looking back: five ideas for better decisions</span>
2.  <span class="roadmap-item done">Computational kindness: easy and fair for others</span>
3.  <span class="roadmap-item current">Looking ahead: where to go from here</span>

## <span class="invert-font">How to continue learning?</span>

- We have covered **a lot of topics**
- But there are **many more** to explore!

## Bayes' rule: update your beliefs with new evidence

- Fundamental theorem in probability theory
- Updates probability of hypothesis based on <span class="highlight">new evidence</span>
- Used in **statistics, machine learning, and decision-making**

> **Important**
>
> Helps make **informed predictions and decisions** under uncertainty in the real world!

## Overfitting: a model that learned the past too well

- Occurs when a model <span class="highlight">learns the training data too well</span>
- **Captures noise and outliers** rather than pattern
- Results in **poor generalization to new data**

> **Important**
>
> Several ways to counter overfitting, e.g. cross-validation.

## Game theory: decisions when others decide too

- Strategic interactions among <span class="highlight">rational decision-makers</span>
- Analyzes situations with **multiple agents** and their strategies

> **Important**
>
> **Many applications** in economics, politics, and biology!

## Networking: how information travels

- Study of **information exchange** over networks
- Includes <span class="highlight">understanding protocols and data transmission</span>
- Optimizes **network resources**

> **Important**
>
> **Important** in computer networks, the internet and social life!

## Relaxation: solve an easier version first

- Simplifies <span class="highlight">complex problems</span> to make them more tractable
- Involves **relaxing certain constraints**
- Provides insights or **approximate** solutions

## Keep programming

- The best way to keep learning is to <span class="highlight">keep programming</span>
- In your studies, in your thesis, in your job
- **There are many interesting topics to explore!**

## Advent of Code: a puzzle a day in December

- [Advent of Code](https://adventofcode.com/) is a fun way to keep programming
- Here you can solve programming puzzles during Advent
- It is **completely free** and ad-free and starts each year at 01.12.

<center>
<img src="../images/gif/lec06-first.gif" width="280" height="280" alt="">
</center>

## Looking ahead: where to go from here

<span class="eyebrow">What we covered</span>

<span class="statement">Many more ideas from computer science help in everyday life, and the best way to keep learning is to keep programming.</span>

## What we covered

<span class="eyebrow">Looking back: five ideas for better decisions</span>

Optimal stopping, explore and exploit, caching, scheduling and randomness give you a toolkit for everyday decisions.

<span class="eyebrow">Computational kindness: easy and fair for others</span>

Good algorithms reduce the burden for others and treat people fairly. Biased data leads to biased decisions.

<span class="eyebrow">Looking ahead: where to go from here</span>

Many more ideas from computer science help in everyday life, and the best way to keep learning is to keep programming.

## Why it matters

"When works for you?" sounds polite but hands the work to the other person. Proposing two concrete slots is kinder. Companies face the same question at scale: how to design processes, products and automated decisions that are easy and fair for customers and colleagues.

## 

Make it easy for others.

## That's it for the lecture series!

- We have covered the basics of Python and six ideas for better decisions
- If you have questions or feedback, <span class="highlight">please let me know!</span>
- All the best for your studies and your career!

## 

<center>
<img src="../images/gif/lec06-second.gif" width="480" height="355" alt="">
</center>

# <span class="flow">Literature</span>

## Interesting literature to start

- Christian, B., & Griffiths, T. (2016). Algorithms to live by: the computer science of human decisions. First international edition. New York, Henry Holt and Company.[^3]

## Books on Programming

- Downey, A. B. (2024). Think Python: How to think like a computer scientist (Third edition). O'Reilly. [Free online](https://greenteapress.com/wp/think-python-3rd-edition/)
- Elter, S. (2021). Schrödinger programmiert Python: Das etwas andere Fachbuch (1. Auflage). Rheinwerk Verlag.

> **Note**
>
> Think Python is free online and a great start. Schrödinger programmiert Python is a playful alternative in German.

## More Literature

For more interesting literature, take a look at the [literature list](../general/literature.qmd) of this course.

[^1]: Dastin, J. (2018). Amazon scraps secret AI recruiting tool that showed bias against women. Reuters, 10 October 2018.

[^2]: Ensign, D. et al. (2018). Runaway feedback loops in predictive policing. Proceedings of Machine Learning Research, 81, 160--171.

[^3]: The main inspiration for this lecture. We have read it and discussed it in depth, always wanting to translate it into a course.
