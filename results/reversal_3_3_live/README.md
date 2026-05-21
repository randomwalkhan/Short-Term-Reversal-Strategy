# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 11:30:02 EDT`
Last processed slot: `manage_1130`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$28,317.75`
- Equity: `$28,317.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SOXL           80.77               26            1.58              1.92        172.38               145.82         0.760          pass              0.356             51.0                           0.455               12.07             -0.514                      ok            True                  False
  INTC           95.65               23            2.16              1.80        118.19               113.85         0.718          pass              0.725             55.6                           0.786                6.17             -0.619                      ok            True                  False
  NXPI           81.82               11            3.46              7.51        306.93                91.65         0.675          pass              0.135              4.2                           0.091                3.17              0.184                      ok            True                  False
  FTNT          100.00               24            1.42              1.29        129.45                70.74         0.662          pass              0.660             33.4                           0.268               18.70              1.758                      ok            True                  False
  PAYX           93.75               16            0.84              0.56         94.68                29.35         0.563          pass              0.652             63.0                           0.364                1.14              0.243                      ok            True                  False
  MNST           81.48               27            0.93              0.56         86.64                49.77         0.558          pass              0.455             81.9                           0.668               13.30              0.658                      ok            True                  False
  AMAT           82.86               35            0.72              2.15        425.93                55.19         0.543          pass              0.453             51.9                           0.443                3.20             -0.241                      ok            True                  False
  NVDA           81.25               16            2.12              3.32        222.05                44.60         0.522          pass              0.169             14.4                           0.268                3.42              0.315                      ok            True                  False
  ISRG           90.00               10            2.66              8.37        445.44                35.82         0.515          pass              0.356             12.7                           0.247               -3.62             -0.030                      ok            True                  False
    ZS           82.35               17            2.78              3.39        173.00                63.59         0.502          pass              0.188              9.4                           0.111               11.00              1.791                      ok            True                  False
  FAST           91.30               23            0.98              0.30         43.55                21.35         0.501          pass              0.571             44.2                           0.278               -2.50             -0.121                      ok            True                  False
  CHTR           89.47               38            0.79              0.80        144.27               113.96         0.767          pass              0.692             58.5                           0.333              -10.47             -0.953 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                    detail
2026-05-21T11:30:02.245220-04:00 early_entry_1130           entry_skipped                                                                                                                                                                                                                                {"reason": "no_candidate"}
2026-05-21T11:25:04.201711-04:00 early_entry_1125           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:25:04.201711-04:00 early_entry_1125 entry_candidate_skipped {"early_entry_score": 0.804, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 6.12, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.527}
2026-05-21T11:20:02.110689-04:00 early_entry_1120           entry_skipped                                                                                                                                                                                                                                {"reason": "no_candidate"}
2026-05-21T11:15:01.031462-04:00 early_entry_1115           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:15:01.031462-04:00 early_entry_1115 entry_candidate_skipped                 {"early_entry_score": 0.713, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 6.82, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.393}
2026-05-21T11:10:05.158469-04:00 early_entry_1110           entry_skipped                                                                                                                                                                                                                                {"reason": "no_candidate"}
2026-05-21T11:05:03.180136-04:00 early_entry_1105           entry_skipped                                                                                                                                                                                                                                {"reason": "no_candidate"}
2026-05-21T11:00:05.229849-04:00 early_entry_1100           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:00:05.229849-04:00 early_entry_1100 entry_candidate_skipped                 {"early_entry_score": 0.714, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 5.21, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.393}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521113002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521113002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521113002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521113002)

</details>
