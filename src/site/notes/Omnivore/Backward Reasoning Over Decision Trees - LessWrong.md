---
{"dg-publish":true,"permalink":"/omnivore/backward-reasoning-over-decision-trees-less-wrong/","title":"Backward Reasoning Over Decision Trees - LessWrong","tags":["philosophy","readlater"],"created":"","updated":""}
---


# Backward Reasoning Over Decision Trees - LessWrong
#Omnivore


---

Game theory is the study of how rational actors interact to pursue incentives. It starts with the same questionable premises as economics: that everyone behaves rationally, that everyone is purely self-interested1, and that desires can be exactly quantified - and uses them to investigate situations of conflict and cooperation.

Here we will begin with some fairly obvious points about decision trees, but by the end we will have the tools necessary to explain a somewhat surprising finding: that giving a US president the additional power of line-item veto may in many cases make the president less able to enact her policies. Starting at the beginning:

The basic unit of game theory is the choice. Rational agents make choices in order to maximize their utility, which is sort of like a measure of how happy they are. In a one-person game, your choices affect yourself and maybe the natural environment, but nobody else. These are pretty simple to deal with:

![](https://proxy-prod.omnivore-image-cache.app/0x0,sC4kG4OuwlezAgl8ErVL7mcxPvAcYVnQbdzNrJnWGkA4/https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/8eab992eda83b71a2ed42ee27341b48fc1bb3821526c05ab.png)

Here we visualize a choice as a branching tree. At each branch, we choose the option with higher utility; in this case, going to the beach. Since each outcome leads to new choices, sometimes the decision trees can be longer than this:

![](https://proxy-prod.omnivore-image-cache.app/0x0,s4nwhQUNExTgql_friLH3TDQvy3vkWdoLfuM9uIQzyaA/https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/70770aafc9dd2bd768903386e5d2aee7457b293704178e9f.png)

Here's a slightly more difficult decision, denominated in money instead of utility. If you want to make as much money as possible, then your first choice - going to college or starting a minimum wage job right Now - seems to favor the more lucrative minimum wage job. But when you take Later into account, college opens up more lucrative future choices, as measured in the gray totals on the right-hand side. This illustrates the important principle of reasoning backward over decision trees. If you reason forward, taking the best option on the first choice and so on, you end up as a low-level manager. To get the real cash, you've got to start at the end - the total on the right - and then examine what choice at each branch will take you there.

This is all about as obvious as, well, not hitting yourself on the head with a hammer, so let's move on to where it really gets interesting: two-player games.

![](https://proxy-prod.omnivore-image-cache.app/0x0,sK3eJOu1WLhYFNL3WLQC6420ghhStmICPuComw5sg0Aw/https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/d1434a2583038eb0960b4cda201758f29b4b168a6261fa6d.png)

I'm playing White, and it's my move. For simplicity I consider only two options: queen takes knight and queen takes rook. The one chess book I've read values pieces in number of pawns: a knight is worth three pawns, a rook five, a queen nine. So at first glance, it looks like my best move is to take Black's rook. As for Black, I have arbitrarily singled out pawn takes pawn as her preferred move in the current position, but if I play queen takes rook, a new option opens up for her: bishop takes queen. Let's look at the decision tree:

![](https://proxy-prod.omnivore-image-cache.app/0x0,s2cUYhN3Db5aMcTITX93bL1WZKbNlmw1-HkGgXamD1jU/https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/06d27360cb931c681f795c4a175d094881507e3433ed6c6d.png)

If I foolishly play this two player game the same way I played the one-player go-to-college game, I note that the middle branch has the highest utility for White, so I take the choice that leads there: capture the rook. And then Black plays bishop takes queen, and I am left wailing and gnashing my teeth. What did I do wrong?

I should start by assuming Black will, whenever presented with a choice, take the option with the highest Black utility. Unless Black is stupid, I can cross out any branch that requires Black to play against her own interests. So now the tree looks like this:

![](https://proxy-prod.omnivore-image-cache.app/0x0,sr6xzabWgaX9RTuBrVn3P-Q7V02Npw45z1FiopQ1dS4U/https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/f978723ee9f27725b12b1296fbcee7e0753c33d35b6143af.png)

The two realistic options are me playing queen takes rook and ending up without a queen and -4 utility, or me playing queen takes knight and ending up with a modest gain of 2 utility.

(my apologies if I've missed some obvious strategic possibility on this particular chessboard; I'm not so good at chess but hopefully the point of the example is clear.)

This method of alternating moves in a branching tree matches both our intuitive thought processes during a chess game (“Okay, if I do this, then Black's going to do this, and then I'd do this, and then...”) and the foundation of some of the [algorithms](http://en.wikipedia.org/wiki/Alpha-beta%5Fpruning) chess computers like Deep Blue use. In fact, it may seem pretty obvious, or even unnecessary. But it can be used to analyze some more complicated games with counterintuitive results.

[Art of Strategy](http://www.amazon.com/The-Art-Strategy-Theorists-Business/dp/0393062430) describes a debate from 1990s US politics revolving around so-called [“line-item veto”](http://en.wikipedia.org/wiki/Line%5Fitem%5Fveto) power, the ability to veto only one part of a bill. For example, if Congress passed a bill declaring March to be National Game Theory Month and April to be National Branching Tree Awareness Month, the President could veto only the part about April and leave March intact (as politics currently works, the President could only veto or accept the whole bill). During the '90s, President Clinton fought pretty hard for this power, which seems reasonable as it expands his options when dealing with the hostile Republican Congress.

But Dixit and Nalebuff explain that gaining line-item veto powers might hurt a President. How? Branching trees can explain.

Imagine Clinton and the Republican Congress are fighting over a budget. We can think of this as a game of sequential moves, much like chess. On its turn, Congress proposes a budget. On Clinton's turn, he either accepts or rejects the budget. A player “wins” if the budget contains their pet projects. In this game, we start with low domestic and military budgets. Clinton really wants to raise domestic spending (utility +10), and has a minor distaste for raised military spending (utility -5). Congress really wants to raise military spending (utility +10), but has a minor distaste for raised domestic spending (utility -5). The status quo is zero utility for both parties; if neither party can come to an agreement, voters get angry at them and they both lose 2 utility. Here's the tree when Clinton lacks line-item veto:

![](https://proxy-prod.omnivore-image-cache.app/0x0,s-pFnyp1WW6D4S2mXvQwymOPdoMk-gqxgOcYPEeTpRCc/https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/dc5cd83eb332ac6c0852ded2c145309eb0b893b5105b6a7a.png)

For any particular Republican choice, Clinton will never respond in a way that does not maximize his utility, so the the Republicans reason backward and arrive at something like this:

![](https://proxy-prod.omnivore-image-cache.app/0x0,s9FzfygshsqUR_kWw8If3PNEovB5UjJllI_3SfFA96Lg/https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/c8e9a485b705fe92d3b2945477b45919363271d13ff415e0.png)

If Republicans are perfectly rational agents, they choose the second option, high domestic and high military spending, to give them their highest plausibly obtainable utility of 5.

But what if Clinton has the line-item veto? Now his options look like this:

![](https://proxy-prod.omnivore-image-cache.app/0x0,s5iV3cjPhskiYNj6bsut7IXNQzR4RmdLNZIna6kcoBkw/https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/3f5ab682447e557e25e13e4e6e9f0d85a82fef0d96dda2c1.png)

If the Republicans stick to their previous choice of “high domestic and high military spending”, Clinton line-item vetoes the military spending, and we end up with a situation identical to the first choice: Clinton sitting on a pile of utility, and the Republicans wailing and gnashing their teeth. The Republicans need to come up with a new strategy, and their thought processes, based on Clinton as a utility-maximizer, look like this:

![](https://proxy-prod.omnivore-image-cache.app/0x0,sBy7uQNvQdYFLimkjNwoYwYXbXT06SE5AWPprHiBJQBg/https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/ccf9b06d4bac441125575db2a56ca57194fa7090d8019181.png)

Here Congress's highest utility choice is to propose low domestic spending (it doesn't matter if they give more money to the military or not as this will get line-item vetoed). Let's say they propose low domestic and low military spending, and Clinton accepts. The utilities are (0, 0), and now there is much wailing and gnashing of teeth on both sides (game theorists call this a gnash equilibrium. Maybe you've heard of it.)

But now Clinton has a utility of 0, instead of a utility of 5\. Giving him extra options has cost him utility! Why should this happen, and shouldn't he be able to avoid it?

This happened because Clinton's new abilities affect not only his own choices, but those of his opponents (compare [Schelling: Strategies of Conflict](https://www.lesswrong.com/lw/14a/thomas%5Fschellings%5Fstrategy%5Fof%5Fconflict/)). He may be able to deal with this if he can make the Republicans trust him.

In summary, simple sequential games can often be explored by reasoning backwards over decision trees representing the choices of the players involved. The next post will discuss simultaneous games and the concept of a Nash equilibrium.

**Footnotes:**

**1:** Game theory requires self-interest in that all players' are driven solely by their desire to maximize their own payoff in the game currently being played without regard to the welfare of other players or any external standard of fairness. However, it can also be used to describe the behavior of altruistic agents so long as their altruistic concerns are represented in the evaluation of their payoff.

## 156

Very nice that you're doing this!

The line item example is a bit too complicated for my taste. Here's a simpler one: let's say Alice has the option of cooking a pie, but must share half of it with Bob. So Alice cooks the pie and everyone is happy. Now let's give Bob the option of stealing the whole pie and frustrating Alice. Then Alice won't cook the pie because she will anticipate that Bob's optimal decision would leave her without pie and frustrate her, so everyone is worse off.

Thank you very much for this simpler explanation, I couldn't quite grasp the concept 100%. This also gives me a very easy way to explain this concept less technically.

Suggestion: Republicans should use a wider paper, and write "high domestic spending" and "high military spending" _on the same line_. This gives them their 5 utility points back. :D

Well, yes. The precise definition of line-item is an essential issue for implementing a "line-item" veto. It's different in different jurisdictions, and I don't know what the federal definition was.

In Wisconsin, the veto was apparently letter by letter - so a patient governor (or staffer) could totally change a provision by hunting for the appropriate letters. Funding the arts via a bill intended to provide farm aid and suchlike. (How that complies with the concept of separation of powers boggles my mind, but that's policy, not letter of the law).

> a patient governor (or staffer) could totally change a provision by hunting for the appropriate letters

It gets worse (better?): in a computerized world, _patience_ is irrelevant. Suppose we have a letter-item veto on [Title I of the U. S. Code](https://raw.github.com/divegeek/uscode/9503c68514ca2d7d6d0344fc449a74abff69d32c/code/Title%5F01.txt), and we think it would be better if, instead of all those boring "general provisions" and "rules of construction", this document codified into law P. C. Hodgell's maxim that "That which can be destroyed by the truth, should be." Then, casting a spell like this---

```routeros
#!/usr/python3
title1 = open("Title_01.txt").read()
target = "That which can be destroyed by the truth, should be."
target = list(target)
target.reverse()
keep_chars = []
for i, c in enumerate(title1):
....try:
........if c == target[-1]:
............keep_chars.append(i)
............target.pop()
....except:
........break
print(keep_chars)
revised = ""
for i in keep_chars:
....revised += title1[i]
print(revised)

```

\---we learn that all we have to do is veto all characters except the fourth, 408th, 409th, 502nd, 510th, 705th, 894th, 895th, 936th, _(more numbers redacted ...)_, and 8786th.

> in a computerized world, patience is irrelevant.

And here's the generalized lesson =)

> In Wisconsin, the veto was apparently letter by letter - so a patient governor (or staffer) could totally change a provision by hunting for the appropriate letters. 

I...  
But that --  
You mean.... 

* whimpers and hides \*

"I try to be cynical, but it's hard to keep up."

I read the example and my first instinct was to check whether it was actually an article on The Onion. But apparently it is not. (Cries.)

Holy crap... This must be the most shocking thing I've seen in a while.

> H**o**ly cra**p**... This m**us**t **be** the mo**st** shocking th**i**ng I've seen in **a** whil**e.**
> 
> opus bestiae.

How poetic. Well said.

I was wondering how someone managed to end up as God-Emperor of Wisconsin.

Letter by... BWA?!?!

How, how did a line item veto law that allows _letter by letter_ editing get passed?

That couldn't possibly be "oh, we didn't imagine that'd be exploitable." If they knew they were passing the power to actually slice a passed bill letter by letter, then they had to know they were essentially giving the governor arbitrary power.

I wish I shared your confidence in the coherence of legislators. My guess is that someone wanted to turn a plural into a singular or something relatively innocuous like that, and genuinely didn't think of the "ransom note" use case.

But... even given them not being _that_ clever, you'd think they'd know that the ability to _arbitrarily_ slice and dice a bill would be too much. (I know I may be displaying hindsight bias, but... they're politicians! They have to have had experience with, say, people taking their (or colleagues') words out of context and making it sound like something else, or they themselves doing it to an opponent, right?

ie, the ability to slice and dice some communication into something entirely different would be something you'd think they'd already have personal experience with. At least, that's what I'd imagine. Though, still, Hanlon's Razor and all that.

Many many years ago, I was contacted by a coworker for an estimate of what it would take to modify our tax-calculation code to support a new law recently passed by the Texas legislature, which specified that the first $25 of Internet charges for Texas-residential subscribers was free of state taxes.

I asked "Well, that depends. What does 'first' mean? If they mean that on every bill we should reduce the taxable basis by $25, we can do that easily. If they mean that on every bill we should chronologically sort all the charges and then exclude _those charges_ from taxation, that's far more complicated, and if tax rates vary depending on the charge the result will be different. If they actually mean the first $25 _for each subscriber_ rather than on each bill, that's easier (but different from the first two options)."

The coworker said "Excellent question. I'll ask the client."

A week later, she forwarded me email from the client rep, saying "Excellent question. I've asked our lawyers."

A month later she forwarded me email from the client rep forwarded from the lawyers saying "Excellent question. We've asked the State Legislature."

Several months later, the consensus seemed to be that the State Legislature had never given any thought to what they meant by "first".

My confidence in politicians' taking care about what they mean is very low.

That depends. They could make the bills really, really short.

"I can make this code compile really fast!"

"Oh? How?"

"Well, all I have to do is just mark every line as being a comment...."

:)

FYI, according to wikipedia this was changed in 1990

> In 1990, a further amendment specified that the line-item veto does not give the governor power to veto individual letters of appropriations bills, thereby forming new words.\[2\]

But the governor could still veto individual words in order to create unrelated sentences?

You know, I'm not actually sure...

While I was looking for a specific [example](https://www.lesswrong.com/lw/dbj/backward%5Freasoning%5Fover%5Fdecision%5Ftrees/6x5o), I found references to its recent repeal. But my example is from \~2005, so there's some inconsistency somewhere.

I couldn't find the wikipedia article you are citing - are you sure it was about Wisconsin?

What was repealed seems to have been the ability to veto individual letters (creating new words). This was a laughably incomplete solution, as instead of vetoing individual letters to create whatever wording the governor liked (as it was before), he's now limited to vetoing lots and lots of words until he finds the exact wording he wanted. Hence why the example looks like lots and lots of words crossed out, instead of specific letters crossed out. The power involved is quite similar, but it's somewhat more tricky to use if you're restricted to whole words.

Good introduction, nothing new (but the "line-item veto" example is a nice one), but still good to have around.

One thing that made me "wail and gnash" a little :

> that everyone is purely self-interested

That's not really the case. Game theory usually consider that everyone is an utility maximizer, but nothing says that the utility function has to be selfish. Utility function can factor well-being and happiness of others in it.

You can apply game theory in cases like a parent-child relation, in which the parent and the child disagree, but the parent still is motivated with the interest of the child. Even in more classical cases, nothing forces the utility function to be selfish and not value the other well-being. Game theory only apply when the agents have different goals, but it can just be "I value my own well-being twice as much as the well-being of the other", which is not "purely self-interested".

It makes me "wail and gnash" because it's a very frequent cliché that rationalists and utility maximizer are necessarily selfish and don't care about others, and it's a cliché we should fight. That say, I understand the a whole part of game theory is about showing how even pure selfishness can, in some cases, lead to cooperation being the best solution. Your "line-item veto" is a good example of it, Clinton and Congress can still cooperate to get the previous 5-5 equilibrium, if they trust each others, and this is an IPD at the end.

> Game theory only apply when the agents have different goals

That is not quite true. It can also apply when they have identical goals but different information, for example, the Meet in New York game that is discussed in the next post. They should still end up at a Nash Equilibrium, and depending on the specifics of a cooperative game, backwards induction may be applicable.

See my [response to steven0461](https://www.lesswrong.com/lw/dbj/backward%5Freasoning%5Fover%5Fdecision%5Ftrees/6x6e) and my footnote. Yes, we will eventually be able to derive cooperation, but we will derive it by starting with selfish assumptions.

I don't think the math models motivation anyway. It's abstracted away, leaving each agent maximising a utility function. Neither is utility in the model (which is well defined) isomorphic to utility for a person making decisions in the real world (which is not). But our minds seem to learn things better when they are couched in terms of a story about people.

Hmm. Possibly one danger in this is assuming that your own internal story about what the equations mean is what they _actually_ mean, such that you end up overconfident that the results of a decision in the real world will be like the story in your head.

> This method of alternating moves in a branching tree matches both our intuitive thought processes during a chess game (“Okay, if I do this, then Black's going to do this, and then I'd do this, and then...”) and the foundation of the algorithms chess computers like Deep Blue use.

Could you include a reference to alpha-beta pruning, since that is precisely what you're describing? Some readers may be more familiar with that subject domain and appreciate explicitly linking game theory to an established search algorithm.

> game theorists call this a gnash equilibrium

Did you mean "Nash equilibrium"? If it was a deliberate pun, you might want to indicate it for those who are looking up new concepts, this being an introductory series.

> Could you include a reference to alpha-beta pruning, since that is precisely what you're describing? Some readers may be more familiar with that subject domain and appreciate explicitly linking game theory to an established search algorithm.

I think you mean minimax. Alpha-beta pruning is the optimization to minimax that prunes branches as soon as any max (min) node evaluates lower (higher) than the highest (lowest) opposite-colored node evaluated so far among the grandparents' children.

True that. I'm just not aware of many people using the original minimax version, while alpha-beta pruning might ring a bell and uses a similar - albeit, as you say, more complexity-cost optimized - methodology.

Pretty good so far. I personally felt like the line-item example was pretty illuminative, but using real political examples instead of sticking with the national game theory month approach is a bit iffy. In particular the line

> If Republicans are perfectly rational agents (a sentiment, I admit, open to doubt) 

Can easily be interpreted as an attack on republicans.

> but using real political examples instead of sticking with the national game theory month approach is a bit iffy

I actually thought it was better to have a real political example - made it feel less like an abstract toy example and more like something with actual real-world relevance.

Agreed. Removing the parenthetical would strictly improve this in my mind

Or better, adding “given that they are human” at the end of it. (OTOH, it's not _that_ implausible that in that context they would make the same choice that perfectly rational agents would.)

> It starts with the same questionable premises as economics: that everyone behaves rationally, that everyone is purely self-interested, and that desires can be easily and exactly quantified

I agree that it assumes that everyone behaves rationally and that desires can be _exactly_ quantified, but I don't see how it assumes that everyone is purely self-interested or that desires can be _easily_ quantified.

By "easily quantified", I meant that there is exactly one possible quantification system that is known by and agreed to by both players, as opposed to the mess going on in real life as is being discussed on Stuart\_Armstrong's thread. But I've deleted that part as unclear.

By "self-interested", I mean for example that the Nash equilibrium for Prisoners' Dilemma is (D,D) because we assume both are trying to minimize their sentence, and we don't have to worry about one of them trying to lessen the other's sentence at his own expense because the other prisoner has a wife and kids, or about them wanting to lengthen their own sentence to pay their debt to society. I agree that one could use the same math to analyze someone who is only playing a game to donate the payoff to charity, or something. I've added a footnote clarifying this further.

> game theorists call this a gnash equilibrium

Well played, sir.

I suggest adding a link at the bottom to the next post in the sequence.

This is a well-written, light, fun intro. I'll look forward to linking my friends [here](https://www.lesswrong.com/lw/dbe/introduction%5Fto%5Fgame%5Ftheory%5Fsequence%5Fguide/). You should add an attractive image to that post somewhere, so e.g. it shows up with a cool image thumbnail when people link it from Facebook. That's why I added the image [here](https://www.lesswrong.com/lw/cs6/how%5Fto%5Fpurchase%5Fai%5Frisk%5Freduction/).

Hopefully stuffy LWers won't fail to upvote this merely because it's stuff _they_ (mostly) know already.

> Go to the beach? (Utility +5) Hit yourself on the head with a hammer? (Utility -20)

Actually, I wouldn't be willing to hit my head with a hammer with probability 25% in order to go to the beach with probability 100% - epsilon, so the magnitude of the second utility ought to be much larger. YMMV.

ETA: Well, if you don't specify how hard I am supposed to hit myself, maybe I would. :-)

> Art of Strategy describes a debate from 1990s US politics revolving around so-called “line-item veto” power, the ability to veto only one part of a bill....During the '90s, President Clinton fought pretty hard for this power, which seems reasonable as it expands his options when dealing with the hostile Republican Congress.

Just for the benefit of those who don't know the history (and won't bother to click on the Wikipedia link), it should be noted that the Republican Congress _happily gave Clinton this power_ (perhaps not so surprising after reading this post!), but it was struck down by the Supreme Court (which [functions as](https://www.lesswrong.com/lw/mh/the%5Famerican%5Fsystem%5Fand%5Fmisleading%5Flabels/) America's House of Lords -- kind of a mirror image of how the actual House of Lords used to function as Britain's Supreme Court).

Not sure about the politics, but presumably:

A) Republicans thought that they were likely to benefit in future (with a Republican president)

B) They might have thought they'd benefit in the present too (e.g. By inserting clauses into bills that would be popular with supporters, but which they knew Clinton would line-item veto; so he gets the flack)

C) They calculated it would likely reduce government spend overall (by preventing "must-pass" bills being stuffed full of pork)

> C) They calculated it would likely reduce government spend overall (by preventing "must-pass" bills being stuffed full of pork)

That was the public goal of the line item veto, and I would imagine that both President Clinton and the vast majority of members of Congress wanted to decrease the amount of pork in the budget (even if those same members wanted to increase the amount of pork for their state or district).

This model of the line-item veto game makes a few faulty assumptions that make it a poor representation of reality:

* It represents the relationship between the Republican Congress and President Clinton as essentially zero-sum (given the possibility of a deadlock, it's not quite zero-sum, but very close), when in reality, they had some shared goals beyond just averting a government shut-down
* It models Congress as a single agent, when it is really 535 agents. _Note to non-Americans: the two parties that dominate American politics generally use primaries to select their candidates for Congress, and it is very rare for a member of Congress seeking re-election to change districts, which means that keeping voters in one's home district happy is typically more important to members of Congress than keeping party officials happy._
* It models the line-item veto as a much coarser instrument than it was. It would have given the President the ability to veto funding for particular projects, not just "increased domestic spending" or "increased military spending."

Because members of Congress answer more to their own districts than to party leadership, there is a tragedy of the commons problem where each member has a strong incentive to go after pork in their own district/state, and although they all want less pork, no one has much incentive to do anything about it. The line item veto would have given one person the ability and incentive to address the issue.

> it should be noted that the Republican Congress _happily gave Clinton this power_ (perhaps not so surprising after reading this post!)

Sorry, why is that not surprising? In Yvain's example, Congress ends up worse off as well.

True; I should have said "less" surprising rather than "not so". (The point being that it's not the lopsided pure transfer of power to Clinton that it naïvely seems to be at first.)

The line item veto is probably a bad choice to use as an example. In the current US political climate, there is a significant life to the meme of paralyzing washington on purpose to get spending down "at any expense." So the problem with your current example is the current American may look at it and think you are presenting lower over all spending as some kind of win, when int his example it is intended to show a loss to both sides. 

And indeed, it seems a president who wanted lower overall spending would support the line item veto. She could then get the credit for vetoing the things her constituents don't want and lay the blame for under funding the things her constituents do want on the opposite party. And of course take the credit for a lower overall budget irrespective of what she would have done running open loop. Is this an example of some more complex game theory, or do results like this come about relatively straightforwardly in simple game theory?

Fascinating, thanks. I already knew a lot of this in a vague manner, but it was nice to see it made concrete and clear.

This seems to have obvious evpsych implications regarding emotions such as love and friendship - if you love somebody enough that you can't take serious actions against them, even if it would otherwise be rational (for a purely selfish agent), then it's also more profitable for your partner to keep interacting with you. Of course, handicapping yourself is only a good idea if the other person isn't out to ruthlessly exploit you anyway, so love often demands a lot of reciprocity - unless, perhaps (getting into strong [armchair evpsych territory](https://www.lesswrong.com/lw/2l7/problems%5Fin%5Fevolutionary%5Fpsychology/) here), the status difference is so large that you have potentially more to gain than lose anyway. I expect somebody here can give a pointer to the standard papers about this?

This is a bit off-topic/already guarded against by your disclaimer, but if black takes the pawn after white takes the knight (the single move from that node of the given tree), black will lose the bishop and the rook immediately, and the game very soon.

Nice discussion of game theory in politics. Is there any theoretical basis for expecting the line-item veto generally to be more harmful than beneficial to the president?

(Not an attempt to belittle the above fascinating example, but genuine interest in any related, more general results of the theory.)

Is that Chess for Kindle?

I doubt that the line-item veto is a good example, because there are so many complications in any kind of real politics. For example, C&C might agree in advance that a certain line item will be included only if some other item is not vetoed. This improves everyone's utility without going all the way back to the "all-or-nothing" setup, in essence prioritizing the line items.

An example where workarounds are impossible or unlikely would illustrate the standard idea of working backwards better.

How about a hostage negotiation? If the negotiator has a gun, that gives him more options, but it also means the kidnapper has to take it into account. This may lead to a breakdown in communications. 

I think that expecting rationality from a kidnapper is pushing it a bit.

---

[Read on Omnivore](https://omnivore.app/me/backward-reasoning-over-decision-trees-less-wrong-1884f2b0a47)
[Read Original](https://www.lesswrong.com/posts/EhEZoTFzys9EDmEXn/backward-reasoning-over-decision-trees)
