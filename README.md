# Dynamic Course Scheduler

My project is a more powerful version of the BYU Schedule Builder. The user specifies what courses they want to take and
gives a ranked list of preferences, such as which professors they'd like or what times are better than others. The
algorithm them finds a non-conflicting schedule with the highest possible score.

This is barely a proof of concept as it is--most of the time for this project went into planning and designing things
that haven't even been implemented yet. But I do plan on making this a real application!

## System diagram

- A diagram modeling the different parts of your system and the where the scaling bottlenecks are and what the
  anticipated limits would be. An explanation of why you expect those limits - either from documentation or from
  empirical data.

Sequence diagrams can be found in the `diagrams/` directory. As you can see, it is designed so that clients don't need
to communicate with the server very often, reducing bottlenecks. In fact the only significant data the server needs to
store are saved preference lists and schedules, which can be easily queried once and cached locally for an entire
session. The main database bottleneck will likely be when thousands of students all ping the database at once during the
first week of school, and even then, much of that data will be the same and therefore cached.

## Key learnings from the project

1. Often, the hardest part of data modeling is everything else! The way I solved most of the database problems for this
   project was by changing the structure to not need much database access at all, like offloading to the client and
   caching redundant data.
2. Which database type you use really matters. I ended up spending way more time than I expected researching the
   differences between Mongo and Dynamo, because every time I had a decision I realized I had forgotten something.
3. It pays to plan things out, **and** scale them down. I have a big text document with all my future ideas planned out,
   and that helped a ton with design decisions. On the other hand, even though very little of the code I have now will
   probably be part of the final project, I learned a ton as I went. Because I gave myself permission to think big, and
   then gave myself permission to only work on the core essentials when prototyping, I got the best of both worlds.

### Proof of Concept Recording

A short video with a simple proof of concept
is [here](https://drive.google.com/file/d/15_Mh8gpSXzokYSxr1b7rKkefJLr_nPZ9/view?usp=sharing).

### Why is this important and interesting?

It's an interesting intersection of several things I've been learning about recently: databases, optimization
algorithms, server architectures. Plus, it solves a problem I actually have--I had the idea because I've wished BYU's
schedule builder could do this, and it can't. I imagine the underlying algorithm can be made way more general than just
class scheduling, as well.
