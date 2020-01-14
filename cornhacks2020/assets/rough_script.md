Before we begin the talk in full I just want to do a very brief history lesson.
Let's imagine for a moment that the year is 2020. Javascript had been the most popular
language for the past 6 consecutive years prior to and including 2020. As of January of
that year NPM had 1.1 million packages. The most popular frameworks at the time were
things like React, Angular, Vue, and Ember.

Jumping ahead to 2025 we make it to the javascript renaissance. Javascript became the only
language used by a majority of developers. This was mainly due to a surge in popularity of
ionic & electron. Servers were written using Node, mobile apps using ionic, desktop apps using electron,
and front-ends using one of 150 or so frameworks available at that time. Google released it's highly
anticipated 3rd rewrite of Angular *pause* Angular 2. The last bastions of hope for programming were
kernels still written in C/C++, but that would soon change.

By the time that 2030 hit, javascript was the only language run on most machines. This is primarily
due to the fact that NodeOS became the most popular operating system. With low level operations
being done directly in js, there was no need to use any language at any point. All code written and
run was javascript. Of course that's still true today, but most people don't ever stop and wonder,
How did things end up like this? Well, today we'll be talking about the history of javascript
and why javascript sucks.

Briefly, some stuff about me. I graduated UNL in 2017 with a double major in computer science and
mathematics. I moved to Mountain View CA where I worked for Google as a Software Engineer for two
years. I just moved back in the summer of last year, and currently working for Travefy, a startup
in the haymarket. Here are links to my github and linkedin. Alright boring stuff over.

I'm going to start by convincing you that javascript is a terrible language. We're going to do
that by looking at some real code examples and you're going to tell me what you think they
evaluate to. Then I want to talk about the history of javascript a little bit, and how it managed
to become so popular despite being so terrible.

So the rules are simple I'll show you some code, you shout out what you think the result is. Should
be noted that all of these I ran in a node console, so if you run inside different browsers you
**may** get different results. It's also a little hard to tell by these are double equals signs,
The css smushes them together for some reason.

JS STUFF

So as demonstrated, there are a lot of times when the language doesn't behave in ways that you
expect. Sure the language has some quirks, but does that necessarily make the language bad? Well
if you're asking me I'm gonna say yeah, it sucks.

I'm not alone in my opinion though, the language is almost universally hated. Despite being
disliked, it's still the most popular language in the world. I've always wondered how? It seems
like new languages pop up like crazy, so why hasn't javascript had a real competitor in the past
25 years? The answer is unfortunately not that satisfying, but nonetheless let's go back
in time to where it all began.

The year is 1995. Netscape Communicator is the most popular browser currently, and the founder of
Netscape, Mark Andreesan had a big idea for what the future of the internet should be. He
envisioned something much more dynamic. Netscape was already making a deal with Sun to
include Java in their browser, but the leadership at Netscape wanted a second language that
would work in browser, one that was more portable, easier to use, and directed more at
designers and scripters than at full on software engineers.

It was for this reason that Mocha was born, created by Brendan Eich in 10 days it was quickly
integrated into the next version of Netscape Communicator. Eventually the name changed from Mocha
to LiveScript, and from LiveScript to JavaScript as part of the closing deal between Netscape and
Sun. Honestly, the defining moment of success for javascript was right then in December of 1995.
It had been integrated into the most popular browser at the time, so there was no real way to
challenge it.

Other browsers had no choice but to follow suit, and make an implementation of Javascript.
Developers at microsoft painstakingly reverse engineered Javascript, including all the bugs
that were present at launch, and made an implementation
they called JScript to avoid legal trouble from Sun. The first version of JScript was included in
IE 3.0 release in August of 1996. Naturally JScript was not a perfect clone of Javascript, and so
there were implementation differences that would shape the future of the language.

Netscape was worried that it would lose control over its own language, so they involved the
European Computer Manufacturers Association. Not only did they lose control of the language
standards process within 1 day, but many of the original quirks of the javascript language
were required by the standard to be kept for backwards compatability reasons. Netscape
didn't want Javascript to become the standard name, so eventually it was named ECMAScript.

This set the stage for the first browser war. The JScript engine & mcirosofts
Internet Explorer vs. the Spider Monkey engine & Netscape. The only problem was
that Netscape had no business sense. Their idea was to get everyone hooked on
their free browser and then start charging for it. Microsoft was already
seelling OS's so they didn't need to charge for ie, and even started bundling
it with their OS. Overtime this led to the downfall of Netscape.

The browser war was over, and microsoft had won. A few interesting things
happened at the end of the war though. Netscape open sourced it's browser and
gave it over to this non-profit organization Mozilla. The bundling of browser
with OS actually got Microsoft trust busted. There was a large anti-trust suit
against them starting in 1998, and they lost. In June of 2000 a court ordered
a breakup of Microsoft. Which obviously didn't happen, they appealed and won
but still pretty interesting. Finally, Microsoft didn't think that the
internet was a technology that had longevity, and with no need to compete
against other browsers that focused on other things besides IE.

Javascript survived because of Microsoft. The JScript engine was still in IE
the most popular browser at the time. A standard was created for the language
because of the competition threat that microsoft posed to Netscape. Eventually
some 5 years later when Jesse James Garrett came up with this thing called AJAX
javacsript surged in popularity again.

How is a language so bad so successful? The answer is simple, no real competition.

Javascript's success is almost accidental, it's a side effect of the first
browser war. It didn't make sense at the time to invent a whole new language
for Microsoft. Why not use the same standard to help fight for market share?
The closest competitor to javascript was probably Flash & Actionscript, but even
that had to be embedded, it couldn't manipulate the DOM directly in the same way
that javascript could. Now at the point we are at, javascript is too big to fail.
It's integrated into ALL browsers and is the accepted standard for dynamic web
development.
