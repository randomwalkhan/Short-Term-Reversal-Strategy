# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 10:50:06 EDT`
Last processed slot: `manage_1100`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SOXL           80.77               26            1.54              1.87        172.40               145.82         0.762            pass              0.360             52.2                           0.476               12.12             -0.512                      ok            True                  False
  INTC           93.75               16            3.54              2.95        117.70               113.85         0.681            pass              0.557             27.3                           0.495                4.68             -0.683                      ok            True                  False
  FTNT          100.00               27            1.29              1.18        129.50                70.74         0.651            pass              0.696             39.2                           0.324               18.85              1.764                      ok            True                  False
  MNST           80.00               25            1.08              0.66         86.60                49.77         0.560            pass              0.393             78.9                           0.420               13.12              0.651                      ok            True                  False
  AMAT           80.00               30            0.97              2.89        425.61                55.19         0.556            pass              0.295             35.3                           0.281                2.94             -0.252                      ok            True                  False
  NVDA           82.35               17            2.05              3.21        222.09                44.60         0.521            pass              0.213             17.1                           0.255                3.49              0.318                      ok            True                  False
  ISRG           84.62               13            2.39              7.50        445.82                35.82         0.504            pass              0.259             21.8                           0.291               -3.35             -0.017                      ok            True                  False
    ZS           84.00               25            1.95              2.39        173.43                63.59         0.501            pass              0.366             36.3                           0.501               11.94              1.830                      ok            True                  False
  AVGO           91.67               36            0.68              1.99        416.91                40.33         0.500 below_threshold              0.653             39.6                           0.238                0.57             -0.168                      ok            True                  False
  INSM           78.57               42            0.31              0.23        107.81               110.82         0.748            pass              0.500             75.2                           0.528                2.45              0.214                      ok           False                  False
  CHTR           89.58               48            0.18              0.18        144.53               113.96         0.747            pass              0.802             90.5                           0.667               -9.92             -0.925 downtrend_blocked_slope           False                  False
  NXPI           75.00               20            2.03              4.41        308.26                91.65         0.704            pass              0.180             14.3                           0.155                4.70              0.250                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                    detail
2026-05-21T10:50:06.054603-04:00 early_entry_1050           entry_skipped                                                                                                                                                                                                                                {"reason": "no_candidate"}
2026-05-21T10:45:05.191060-04:00 early_entry_1045           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:45:05.191060-04:00 early_entry_1045 entry_candidate_skipped {"early_entry_score": 0.778, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 9.05, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.528}
2026-05-21T10:40:05.208680-04:00 early_entry_1040           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:40:05.208680-04:00 early_entry_1040 entry_candidate_skipped  {"early_entry_score": 0.75, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 9.42, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.528}
2026-05-21T10:35:05.061516-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:35:05.061516-04:00 early_entry_1035 entry_candidate_skipped     {"early_entry_score": 0.694, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 493.0, "option_spread_pct": 19.05, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MAR", "timing_score": 0.414}
2026-05-21T10:35:05.061516-04:00 early_entry_1035 entry_candidate_skipped {"early_entry_score": 0.784, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 13.9, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.531}
2026-05-21T10:30:05.185385-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:30:05.185385-04:00 early_entry_1030 entry_candidate_skipped     {"early_entry_score": 0.694, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 493.0, "option_spread_pct": 19.05, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MAR", "timing_score": 0.407}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521105006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521105006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521105006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521105006)

</details>
