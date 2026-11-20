# Reflection

**English** · [Dansk](Reflection-da) · [Bahasa Malaysia](Reflection-ms)

## How we approached the project

We started with a list of the things the game must do and cut it into seven steps that can each be run and looked at: window and paddle, ball, paddle bounce, bricks, collisions and score, lives and end, speed-up. Before any code we wrote down who the project is for, what it must deliver and in which order. Then each step was built, tested, reviewed and photographed before the next one began.

## What was hard

- **Collision sides.** Deciding whether a ball hit the side or the top of a brick took the most thought. Comparing how deep the ball reaches on each axis was the answer, and corner hits needed one more rule.
- **Tunnelling.** A fast ball can jump over a thin object. We had to prove that the maximum speed is smaller than the smallest thing the ball must hit.
- **Screenshots without touching the desktop.** Running a window in a container with a virtual display took some set-up, but it gave us repeatable pictures from the exact code of each step.
- **Small tool problems.** Line endings that differ between Windows and Linux made the shell-script checks fail in the pipeline until we fixed them.

## What was easy

- Turtle is quick to start with: a window and a moving shape need only a few lines.
- Because the rules do not depend on Turtle, tests were short and fast.

## The biggest learning

Keep the rules and the drawing apart. Once the game rules were plain Python functions on small immutable values, almost every bug could be caught by a test in milliseconds, and we could play a whole game without a window.

## What we would do differently

- Write the collision tests before the collision code, to find the corner-hit case earlier.
- Choose the frame loop with `ontimer` from the start instead of `time.sleep`.
- Add sound, levels and a high-score list. These were out of scope for this assignment.

[Back to Home]({link('Home', L)})
