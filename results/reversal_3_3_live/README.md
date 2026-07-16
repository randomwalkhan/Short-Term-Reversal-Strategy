# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-16 15:45:02 EDT`
Last processed slot: `manual`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
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

- Cash: `$29,224.25`
- Equity: `$29,224.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-16)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   ADI     option         option ADI260821C00380000      4          2026-07-15         2026-07-16        35.15      31.635 -1406.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           81.25               16            4.41             41.76       1334.76                84.79         0.571          pass              0.169             12.8                           0.196               -6.46             -0.052                                 ok            True                  False
  UPRO           90.00               10            2.48              2.53        144.79                41.96         0.566          pass              0.334              3.6                           0.174                0.33              0.204                                 ok            True                  False
  AMZN           80.00               15            1.84              3.29        253.55                34.26         0.527          pass              0.086              0.0                           0.229                5.00              0.424                                 ok            True                  False
  FTNT           92.86               14            2.36              2.71        163.35                41.65         0.523          pass              0.508             28.6                           0.340                4.57              0.488                                 ok            True                  False
  CRWD           80.00               20            2.18              3.16        205.42                56.35         0.522          pass              0.217             32.7                           0.308                4.70              0.664                                 ok            True                  False
  KLAC           80.95               21            2.75              4.32        222.65               109.33         0.694          pass              0.269             33.7                           0.233              -27.64             -2.153 downtrend_blocked_slope_and_streak           False                  False
  AMAT           80.00               15            3.44             13.95        573.45                98.89         0.643          pass              0.167             23.0                           0.321              -22.61             -1.536 downtrend_blocked_slope_and_streak           False                  False
  ASML           93.10               29            1.46             18.54       1807.32                66.00         0.599          pass              0.664             42.7                           0.351              -10.09             -0.675            downtrend_blocked_slope           False                  False
  MSTR           67.74               31            3.10              2.11         96.56               100.18         0.583          pass              0.273             24.9                           0.175                8.65              0.292                                 ok           False                  False
   TXN           85.71                7            3.85              8.12        297.71                65.52         0.578          pass              0.236              8.5                           0.161               -2.85              0.105                                 ok           False                  False
  CSCO           88.89                9            2.05              1.61        111.08                36.51         0.575          pass              0.432             45.7                           0.570               -6.45             -0.004                                 ok           False                  False
   ADI           72.73               11            3.06              8.36        387.38                55.85         0.573          pass              0.095             10.2                           0.218               -4.57             -0.028                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et       slot              event_type                                                                                                                                                                                                                                                                 detail
2026-07-16T15:10:05.118265-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T15:05:04.145038-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T15:00:06.149748-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T14:55:06.750715-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T14:50:02.142710-04:00 entry_1500           entry_skipped                                                                                                                                                                                                                 {"reason": "no_trade_after_option_and_timing_filters"}
2026-07-16T14:50:02.142710-04:00 entry_1500 entry_candidate_skipped                              {"early_entry_score": 0.671, "option_liquidity_status": "low_volume", "option_open_interest": 761.0, "option_spread_pct": 4.13, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.508}
2026-07-16T14:50:02.142710-04:00 entry_1500 entry_candidate_skipped                          {"early_entry_score": 0.521, "option_liquidity_status": "wide_spread", "option_open_interest": 3043.0, "option_spread_pct": 25.76, "option_volume": 343.0, "reason": "no_trade_low_option_liquidity", "ticker": "WBD", "timing_score": 0.531}
2026-07-16T14:50:02.142710-04:00 entry_1500 entry_candidate_skipped {"early_entry_score": 0.428, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 19.61, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.572}
2026-07-16T14:50:02.142710-04:00 entry_1500 entry_candidate_skipped              {"early_entry_score": 0.267, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 84.0, "option_spread_pct": 8.5, "option_volume": 4.0, "reason": "no_trade_low_option_liquidity", "ticker": "MPWR", "timing_score": 0.577}
2026-07-16T14:50:02.142710-04:00 entry_1500 entry_candidate_skipped                            {"early_entry_score": 0.287, "option_liquidity_status": "low_volume", "option_open_interest": 859.0, "option_spread_pct": 12.05, "option_volume": 16.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTSH", "timing_score": 0.591}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260716154502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260716154502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260716154502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260716154502)

</details>
