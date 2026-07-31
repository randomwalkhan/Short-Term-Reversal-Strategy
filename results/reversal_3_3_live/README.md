# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-31 14:45:22 EDT`
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

- Cash: `$16,667.25`
- Equity: `$34,512.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$1,290.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00050000       2026-07-30                   1     86     16555.0                 17845.0         1.92           2.08       50.11         50.47          bid_ask_mid                       2.08                bid_ask_mid                    True          1290.0                   7.79         92.31               13              1.24         25.34           25.71                  28.82                2759.0          136.0               0.03                      ok
```

## Today's Closed Trades (2026-07-31)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           87.88               33            0.79              0.32         57.51                60.55         0.628          pass              0.600             57.9                           0.514                1.12              0.314                                 ok            True                  False
  GEHC           90.00               10            2.36              1.15         69.45                56.76         0.582          pass              0.447             40.6                           0.677                8.34              1.227                                 ok            True                  False
  MDLZ           92.86               14            1.22              0.54         62.85                34.51         0.581          pass              0.528             33.6                           0.325                2.15              0.544                                 ok            True                  False
   KHC           90.91               11            1.61              0.30         26.25                32.41         0.580          pass              0.424             22.7                           0.287                0.29              0.394                                 ok            True                  False
  CTAS           93.10               29            0.77              1.11        206.31                40.09         0.560          pass              0.722             63.2                           0.592                0.37              0.469                                 ok            True                  False
   KDP           81.25               16            1.41              0.31         31.44                32.85         0.555          pass              0.233             34.6                           0.314                0.70              0.340                                 ok            True                  False
  MNST           88.89               18            0.98              0.67         97.36                23.72         0.543          pass              0.436             30.3                           0.542               -0.83              0.180                                 ok            True                  False
   TRI           87.18               39            0.81              0.56         98.59                65.88         0.518          pass              0.658             73.9                           0.708                1.90              1.072                                 ok            True                  False
  ALNY           86.67               30            1.18              1.70        204.75               124.46         0.763          pass              0.552             54.9                           0.366              -24.08             -1.960            downtrend_blocked_slope           False                  False
  TMUS           92.31               26            0.92              1.12        172.86                56.67         0.616          pass              0.666             56.3                           0.691              -10.75             -1.140            downtrend_blocked_slope           False                  False
  DRAM           79.31               29            2.15              0.79         52.00               113.92         0.584          pass              0.323             45.9                           0.333               -2.85             -1.364 downtrend_blocked_slope_and_streak           False                  False
  GILD           86.67               30            0.46              0.43        131.10                35.61         0.536          pass              0.608             81.2                           0.712               -2.69             -0.074                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-07-31T11:24:55.037257-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T11:01:50.323934-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T10:17:02.389266-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T00:00:05.700754-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-07-30T15:10:05.973012-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T15:05:01.482451-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T15:00:04.923980-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T14:55:06.025633-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T14:50:04.061730-04:00       entry_1500              entry {"allocated_cash": 16555.0, "asset_type": "option", "contract_symbol": "CSX260918C00050000", "contracts": 86, "early_entry_score": 0.509, "entry_mode": "regular", "entry_option_price": 1.925, "execution_mode": "option", "matched_signals": 13, "option_liquidity_status": "ok", "option_open_interest": 2759.0, "option_spread_pct": 2.6, "option_volume": 136.0, "success_rate": 92.31, "ticker": "CSX", "timing_score": 0.578}
2026-07-30T14:50:04.061730-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-30", "training_samples": 5504, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260731144522)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260731144522)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260731144522)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260731144522)

</details>
