<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img src="assets/banner-light.svg" alt="Mayeen's Curiosity Den. Curiosity lives here. Come for the code. Stay for the questions." width="100%">
</picture>

<h1 align="center">Hey, I'm Mayeen. Welcome to my den.</h1>

<p align="center">
  <strong>Senior Software QA Engineer · Builder · Bug detective</strong><br>
  Turning “works on my machine” into “here's the evidence.”
</p>

<p align="center">
  <a href="https://mayeensajid.netlify.app">↗ Portfolio</a> &nbsp; · &nbsp;
  <a href="https://www.linkedin.com/in/mayeen-abedin-sajid-50b4a0194/">↗ Say hello</a> &nbsp; · &nbsp;
  <a href="#inside-the-den">↓ Wander around</a>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/desk-notes-dark.svg">
  <img src="assets/desk-notes-light.svg" alt="A passing test answers a question. Curiosity asks a better one. Read all three desk notes below." width="100%">
</picture>

<details>
<summary><sub>📓 Pause here. Borrow a thought.</sub></summary>

> A passing test answers a question. Curiosity asks a better one.
>
> Make room for the strange idea. Then build a way to test it.
>
> Leave the code clearer, the product kinder, and the next person a clue.

</details>

## Professional Snapshot

**Senior Software QA Engineer (L1) · Enosis Solutions · Dhaka**<br>
Nearly 4 years of asking “what could go wrong?” — and coming back with evidence.

- **Own the release.** QA POC for an enterprise platform migration, from test strategy through staging acceptance and release sign-off.
- **Engineer the checks.** Playwright + C#/NUnit at work; TypeScript UI and API automation in my portfolio.
- **Show the receipts.** GroceryMate audit: **9 defects · 4 viewports · every High/Medium fix independently re-verified.**

## Inside the Den

*Six little rabbit holes. Click a card. Peek inside. Stay curious.*

<details>
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-museum-dark.svg"><img src="assets/card-museum-light.svg" width="520" alt="Open Bug Museum — small bugs, plot twists. Case closed?"></picture></summary>

**I collect bugs with backstories.** Real failure patterns, root causes, and ways to catch them.

First exhibit: a refresh-token race hiding behind “random logouts.”

[Enter the museum →](https://github.com/Mayeen4536/bug-museum)

</details>

<details>
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-playwright-dark.svg"><img src="assets/card-playwright-light.svg" width="520" alt="Open the test kitchen — Playwright SauceDemo automation."></picture></summary>

**Tests with receipts.** Playwright + TypeScript, reusable auth, UI journeys, and API contracts. Failures leave traces.

[Lift the lid →](https://github.com/Mayeen4536/playwright-saucedemo-automation) · [Check the real CI →](https://github.com/Mayeen4536/playwright-saucedemo-automation/actions)

</details>

<details>
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-grocery-dark.svg"><img src="assets/card-grocery-light.svg" width="520" alt="Open GroceryMate — split the bill, keep the friendship."></picture></summary>

**Fair shares. Unfairly thorough testing.** A household-expense app audited across **88 interaction steps · 4 viewports · 9 defects found**.

Every High and Medium issue fixed and independently re-verified in that audit.

[See the fieldwork →](https://github.com/Mayeen4536/GroceryMate)

</details>

<details>
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-toolkit-dark.svg"><img src="assets/card-toolkit-light.svg" width="520" alt="Open the gadget drawer — tools and testing instincts."></picture></summary>

**At work:** Playwright · C# · NUnit<br>
**In the den:** TypeScript · API testing · SQL · GitHub Actions

My favorite tool? **A suspiciously specific question.**

</details>

<details>
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-now-dark.svg"><img src="assets/card-now-light.svg" width="520" alt="Open On my mind — current experiments and open source."></picture></summary>

**More museum exhibits. Smarter test design. A path toward SDET.**

Exploring AI-assisted QA, with a human checking the answers. Leaving small improvements upstream, too: [a merged fix in Python's icalendar →](https://github.com/collective/icalendar/pull/1736)

</details>

<details>
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-play-dark.svg"><img src="assets/card-play-light.svg" width="520" alt="Open one tiny mystery — one cookie, two confirmed orders."></picture></summary>

**🍪 The case of the impossible cookie**

One cookie left. Mina and Rafi each click **Buy** once. Both get an order confirmation. Stock now says **0**.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/cookie-case-dark.svg">
  <img src="assets/cookie-case-light.svg" width="520" alt="Illustrated puzzle: Mina and Rafi both order the last cookie at almost the same time. Both orders are confirmed, despite stock starting at one.">
</picture>

**How did one cookie sell twice?** Tap your theory.

<details>
<summary>🖱️ Someone double-clicked Buy.</summary>

Good first suspect. But the clue says **two different shoppers, one click each**. This bug doesn't need a double-click. Try another theory.

</details>

<details>
<summary>🧾 One order printed two receipts.</summary>

That would explain duplicate paper. The order log shows **two different order IDs**, though. Something happened before the receipts.

</details>

<details>
<summary>⚡ Both shoppers claimed the same last cookie.</summary>

**Caught it. A race condition wearing a cookie costume.**

Both checkouts read “1 left” before either reserved it. Each accepted an order and wrote “0 left.” Two promises. One cookie.

**My next move:** reserve stock atomically, then run two checkouts together. Expect **one confirmation and one sold-out response**.

`Case cracked. Cookie custody: still disputed.`

[More bugs with backstories →](https://github.com/Mayeen4536/bug-museum)

</details>

</details>

---

<p align="center">
  <strong>A strange idea? A tricky bug? Pull up a chair.</strong><br>
  Open to Senior QA, QA Automation, and SDET roles.<br><br>
  <a href="https://www.linkedin.com/in/mayeen-abedin-sajid-50b4a0194/">Let's talk ↗</a> &nbsp; · &nbsp;
  <a href="https://mayeensajid.netlify.app">Visit my portfolio ↗</a><br><br>
  <sub>Leave with a question. Come back with an idea.</sub>
</p>
