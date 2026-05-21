# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 11:45:04 EDT`
Last processed slot: `early_entry_1145`

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
  SOXL           81.48               27            0.73              0.89        172.82               145.82         0.795          pass              0.464             77.2                           0.533               13.04             -0.475                      ok            True                  False
  INTC           95.83               24            1.95              1.62        118.26               113.85         0.724          pass              0.745             59.9                           0.719                6.40             -0.609                      ok            True                  False
  NXPI           81.82               11            3.46              7.50        306.93                91.65         0.670          pass              0.168             15.4                           0.250                3.17              0.184                      ok            True                  False
  FTNT          100.00               24            1.48              1.34        129.42                70.74         0.659          pass              0.651             30.5                           0.238               18.63              1.755                      ok            True                  False
  PAYX           93.33               15            0.85              0.57         94.68                29.35         0.568          pass              0.633             62.5                           0.343                1.13              0.242                      ok            True                  False
  AMAT           80.00               30            0.92              2.76        425.67                55.19         0.559          pass              0.304             38.2                           0.295                2.99             -0.250                      ok            True                  False
  MNST           81.48               27            0.94              0.57         86.63                49.77         0.557          pass              0.453             81.6                           0.645               13.28              0.658                      ok            True                  False
   ADP           93.75               32            0.66              1.02        220.25                38.26         0.532          pass              0.759             64.1                           0.520                2.40              0.449                      ok            True                  False
  FAST           94.44               18            1.16              0.35         43.53                21.35         0.529          pass              0.595             34.4                           0.209               -2.67             -0.129                      ok            True                  False
  NVDA           85.71               21            1.68              2.63        222.34                44.60         0.523          pass              0.374             32.1                           0.448                3.88              0.335                      ok            True                  False
  MDLZ           84.21               19            1.07              0.46         61.64                21.23         0.505          pass              0.312             29.8                           0.252               -0.21             -0.016                      ok            True                  False
  CHTR           90.00               40            0.54              0.55        144.38               113.96         0.770          pass              0.759             71.6                           0.584              -10.24             -0.941 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                    detail
2026-05-21T11:45:04.222670-04:00 early_entry_1145           entry_skipped                                                                                                                                                                                                                                {"reason": "no_candidate"}
2026-05-21T11:40:04.207622-04:00 early_entry_1140           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:40:04.207622-04:00 early_entry_1140 entry_candidate_skipped {"early_entry_score": 0.775, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 7.04, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.527}
2026-05-21T11:35:02.090762-04:00 early_entry_1135           entry_skipped                                                                                                                                                                                                                                {"reason": "no_candidate"}
2026-05-21T11:30:02.245220-04:00 early_entry_1130           entry_skipped                                                                                                                                                                                                                                {"reason": "no_candidate"}
2026-05-21T11:25:04.201711-04:00 early_entry_1125           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:25:04.201711-04:00 early_entry_1125 entry_candidate_skipped {"early_entry_score": 0.804, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 6.12, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.527}
2026-05-21T11:20:02.110689-04:00 early_entry_1120           entry_skipped                                                                                                                                                                                                                                {"reason": "no_candidate"}
2026-05-21T11:15:01.031462-04:00 early_entry_1115           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:15:01.031462-04:00 early_entry_1115 entry_candidate_skipped                 {"early_entry_score": 0.713, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 6.82, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.393}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521114504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521114504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521114504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521114504)

</details>
