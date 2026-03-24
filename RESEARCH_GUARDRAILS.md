# Research Guardrails

This document defines the default research discipline for the Reversal project.
The goal is to prevent the project from drifting into "curve sculpting" or
LLM-assisted overfitting.

## Core Principle

We do not treat a good-looking backtest as sufficient evidence.

Every promoted change should be defensible on three layers:

1. Mechanism
2. Implementation
3. Execution realism

If a change only improves the equity curve but cannot be explained on those
three layers, it should remain an experiment rather than becoming part of the
official strategy.

## Required Questions Before Promoting Any New Filter

Before a new signal, factor, rule, or threshold is promoted into an official
version, answer these questions explicitly:

1. Why should this opportunity exist?
2. Who is on the other side of the trade and why are they losing?
3. Why can this effect persist instead of being arbitraged away?
4. Does the edge survive transaction costs, slippage, and realistic execution?
5. Is the result stable out of sample, or is it just improving the historical fit?

If these questions cannot be answered coherently, the change should not be
treated as core strategy logic.

## What LLMs Are Allowed To Do

LLMs are useful here as amplifiers, not as edge generators.

Allowed uses:

- speed up data cleaning and feature engineering
- implement research code and notebook workflow faster
- summarize experiment results
- propose structured experiment checklists
- help compare variants once the hypothesis is already defined

Not allowed as a sole basis for promotion:

- "find a profitable strategy" from public internet summaries
- blindly combine indicators because the backtest improves
- generate many parameter variants and pick the prettiest curve
- replace mechanism reasoning with polished narrative explanations

## Anti-Overfitting Rules

These rules apply by default:

1. Do not add a filter only because Sharpe or return improves.
2. Separate hypothesis formation from parameter tuning.
3. Prefer fewer rules with clearer mechanism over many small cosmetic filters.
4. Keep a distinction between exploratory tests and official results.
5. When a filter is added, document what failure mode it is supposed to remove.

Examples of suspicious upgrades:

- changing RSI or lookback settings repeatedly until the curve smooths out
- stacking volume, stop-loss, and timing filters without a market-structure reason
- promoting a rule because it helps one subperiod while weakening generality

## Required Realism Checks

A strategy idea is not complete until these are discussed:

- transaction cost
- slippage
- execution delay
- liquidity
- option spread quality
- position sizing
- capital concentration
- capacity limits

For options research, also ask:

- Is the selected contract realistically tradable?
- Is the option price assumption based on real chain quality or only model price?
- Is current implied volatility rich or cheap relative to recent realized sigma?

## Required Validation Structure

Every serious upgrade should distinguish between:

- in-sample improvement
- out-of-sample behavior
- robustness under nearby parameter changes
- regime sensitivity

Preferred validation tools:

- walk-forward tests
- holdout windows
- threshold sensitivity analysis
- side-by-side comparisons against the previous official version

## Drawdown Discipline

When a live or paper strategy enters drawdown, do not jump straight to
"replace the strategy."

First ask:

1. Is the market regime different from the regime the strategy depends on?
2. Is the drawdown still within historical expectations?
3. Did execution conditions deteriorate?
4. Is the edge broken, or is this normal variance?

If these cannot be evaluated, the problem is not just the strategy. It is a
lack of research understanding.

## Promotion Standard For Official Versions

An experiment can become an official version only if:

- the mechanism is explainable
- the implementation is reproducible
- the execution assumptions are explicit
- the results are stronger than the current official version for a defensible reason
- the new version improves the project without hiding new fragility

If not, keep it as an article variant, side experiment, or notebook note.

## Reversal-Specific Interpretation

For this project, the working hypothesis is not simply:

"large intraday drop -> rebound."

The useful question is narrower:

- Is the drop linked to forced intraday pressure, inventory imbalance, or
  temporary liquidity dislocation?
- Or is it just noise that looks attractive in hindsight?

That distinction matters more than whether the backtest curve improves by a few
extra points of Sharpe.

## Operating Rule Going Forward

For future Reversal upgrades, every official version note should state:

1. what changed
2. why the change may work
3. what risk or fragility it is intended to reduce
4. whether the improvement looks structural or merely statistical
