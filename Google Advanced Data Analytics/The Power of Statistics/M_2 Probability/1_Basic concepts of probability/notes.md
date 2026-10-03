# Fundamental Concepts of Probability

## Probability

- **Probability** quantifies uncertainty and describes the likelihood of an event occurring.
- Probability ranges from **0 to 1**, or **0% to 100%**:
  - `0` = impossible event
  - `1` = certain event
  - Near `0` = unlikely
  - Near `1` = likely
  - `0.5` = equally likely to occur or not occur

## Random Experiment

- A **random experiment** is a process whose outcome cannot be predicted with certainty.
- Every random experiment:
  - Has more than one possible outcome.
  - Has all possible outcomes identifiable in advance.
  - Has an outcome determined by chance.

- Examples: tossing a coin, rolling a die.

## Outcome

- An **outcome** is the result of a random experiment.
- Example: A die roll has six possible outcomes: `1, 2, 3, 4, 5, 6`.

## Event

- An **event** is a set of one or more outcomes.
- Example: When rolling a die:
  - Even-number event = `{2, 4, 6}`
  - Odd-number event = `{1, 3, 5}`

## Probability of an Event

- For equally likely outcomes:

**Probability = Number of desired outcomes ÷ Total number of possible outcomes**

- Probability can be represented as a decimal or percentage.
- Example: `0.5 = 50%`.

## Examples

### Coin Toss

- A fair coin has two possible outcomes: **Heads** and **Tails**.
- `P(Heads) = 1/2 = 0.5 = 50%`
- A coin with heads on both sides:
  - `P(Heads) = 1 = 100%`
  - `P(Tails) = 0 = 0%`

- A 50% probability does not mean every short sequence will contain exactly 50% heads. Over many tosses, the long-run frequency is expected to approach 50%.

### Die Roll

- A fair six-sided die has six possible outcomes: `1, 2, 3, 4, 5, 6`.
- Probability of rolling a `3`:

`P(3) = 1/6 ≈ 0.1667 ≈ 16.7%`

## Probability Notation

- `P(A)` = probability of event **A**.
- `P(B)` = probability of event **B**.
- For any event `A`:

`0 ≤ P(A) ≤ 1`

- `P(A) > P(B)` → Event A is more likely than Event B.
- `P(A) = P(B)` → Events A and B are equally likely.

## Key Takeaway

- Probability helps data professionals quantify uncertainty and make informed decisions.
- **Random experiment → outcome → event → probability** are fundamental building blocks for more advanced probability calculations.

# The Probability of Multiple Events

## Types of Events

### Mutually Exclusive Events

- Two events are **mutually exclusive** if they **cannot occur at the same time**.
- Examples:
  - A coin toss cannot be both heads and tails.
  - A single die roll cannot be both 2 and 4.

### Independent Events

- Two events are **independent** if the occurrence of one event **does not affect the probability of the other**.
- Examples:
  - Consecutive coin tosses.
  - Consecutive die rolls.

- Getting a particular result on the first trial does not change the probabilities of the next trial.

## Three Basic Rules of Probability

### 1. Complement Rule

- The **complement** of an event is the event **not occurring**.
- The probability of an event and its complement always add up to `1`.

**Formula:**

`P(A') = 1 - P(A)`

- `A'` means **not A**.
- Example: If `P(snow) = 0.4`:

`P(no snow) = 1 - 0.4 = 0.6 = 60%`

### 2. Addition Rule — Mutually Exclusive Events

- Used when events **cannot occur at the same time**.
- The probability of **A or B** is the sum of their probabilities.

**Formula:**

`P(A or B) = P(A) + P(B)`

**Example: Rolling a 2 or 4**

- `P(2) = 1/6`
- `P(4) = 1/6`

`P(2 or 4) = 1/6 + 1/6 = 1/3 ≈ 33%`

### 3. Multiplication Rule — Independent Events

- Used when events are **independent**.
- The probability of **A and B** is the product of their probabilities.

**Formula:**

`P(A and B) = P(A) × P(B)`

**Example: Rolling a 1 and then a 6**

- `P(1) = 1/6`
- `P(6) = 1/6`

`P(1 and 6) = 1/6 × 1/6 = 1/36 ≈ 2.8%`

## Key Takeaways

- **Mutually exclusive** → events cannot happen together.
- **Independent** → one event does not affect the other.
- **Complement rule:** `P(A') = 1 - P(A)`
- **Addition rule:** `P(A or B) = P(A) + P(B)` for mutually exclusive events.
- **Multiplication rule:** `P(A and B) = P(A) × P(B)` for independent events.
- These rules provide a foundation for more complex probability analysis.

# Conditional Probability for Dependent Events

## Dependent Events

- Two events are **dependent** if the occurrence of one event **changes the probability of the other**.
- The second event is **dependent on** or **conditional on** the first event.
- Examples:
  - Getting a good grade depends on studying.
  - Avoiding a restaurant wait depends on arriving early.
  - Drawing cards without replacement: the first draw changes the probability of the second draw.

## Conditional Probability

- **Conditional probability** is the probability of an event occurring **given that another event has already occurred**.
- It is used to describe relationships between dependent events.

### Conditional Probability Formula

`P(A and B) = P(A) × P(B|A)`

- `P(B|A)` means **the probability of B given A**.
- The `|` symbol indicates that B is conditional on A.

The formula can also be rearranged as:

`P(B|A) = P(A and B) / P(A)`

- Use the form that matches the information provided.

## Independent Events and Conditional Probability

- The conditional probability formula also applies to independent events.
- For independent events:

`P(B|A) = P(B)`

Therefore:

`P(A and B) = P(A) × P(B)`

This is the multiplication rule for independent events.

## Example: Drawing Two Hearts

A standard deck has **52 cards**, including **13 hearts**.

- First heart:

`P(A) = 13/52 = 25%`

- After drawing a heart, **12 hearts remain out of 51 cards**:

`P(B|A) = 12/51 ≈ 23.5%`

- Probability of drawing two hearts in a row:

`P(A and B) = (13/52) × (12/51) = 1/17 ≈ 5.9%`

The events are dependent because the first draw changes the probability of the second draw.

## Example: Online Purchases

- `20%` of customers spend **$100 or more**.
- `10%` of those customers receive a gift card.
- Probability of both events:

`P($100 and gift card) = 0.20 × 0.10 = 0.02 = 2%`

Therefore, there is a **2% probability** that a customer spends $100 or more and receives a gift card.

## Key Takeaways

- **Dependent events:** One event changes the probability of another.
- **Conditional probability:** Probability of an event given that another event has occurred.
- `P(A and B) = P(A) × P(B|A)`
- `P(B|A) = P(A and B) / P(A)`
- `P(B|A)` is read as **“probability of B given A.”**
- Conditional probability is useful for analyzing relationships between events and making data-driven predictions.
