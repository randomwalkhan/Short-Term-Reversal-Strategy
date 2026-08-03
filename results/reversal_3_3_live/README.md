# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-03 10:30:03 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$35,229.75`
- Equity: `$35,229.75`
- Realized PnL: `$25,229.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-03)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  PYPL     option         option PYPL260918C00057500     66          2026-07-31         2026-08-03        2.500      3.0550  3663.0        22.2 take_profit_day1_hit_at_scan
   CSX     option         option  CSX260918C00050000     86          2026-07-30         2026-08-03        1.925      1.7325 -1655.5       -10.0        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           83.33               24            0.51              0.11         31.07                33.11         0.556          pass              0.238              0.0                           0.150                1.71              0.454                                 ok            True                  False
  MNST           80.00               10            1.76              1.19         95.87                24.15         0.550          pass              0.055              0.0                           0.157               -0.81              0.203                                 ok            True                  False
  BKNG           91.18               34            0.60              0.81        192.56                45.18         0.521          pass              0.622             37.3                           0.270                6.85              1.174                                 ok            True                  False
  MRVL           81.08               37            0.17              0.22        187.47                91.71         0.615          pass              0.561             96.9                           0.973               -3.94             -1.490 downtrend_blocked_slope_and_streak           False                  False
  DRAM           75.76               33            1.25              0.44         50.18               111.30         0.607          pass              0.444             76.6                           0.896               -6.26             -1.703 downtrend_blocked_slope_and_streak           False                  False
  AAPL           95.00               20            1.10              2.38        307.89                37.33         0.593          pass              0.603             25.7                           0.320               -6.45             -0.346 downtrend_blocked_slope_and_streak           False                  False
  LRCX           86.67               30            1.04              2.13        292.11                90.68         0.592          pass              0.614             81.2                           0.924               -5.47             -1.333 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           93.33               30            0.18              0.08         62.28                33.81         0.571          pass              0.677             43.8                           0.191                3.19              0.559                                 ok           False                  False
  SOXL           80.65               31            3.24              2.60        113.60               178.56         0.547          pass              0.424             70.6                           0.898              -18.86             -4.231 downtrend_blocked_slope_and_streak           False                  False
   CSX           96.67               30            0.35              0.12         50.35                27.78         0.546          pass              0.783             65.0                           0.707                0.23             -0.053                                 ok           False                  False
    MU           78.79               33            1.44              8.31        819.47               109.24         0.544          pass              0.440             77.6                           0.908               -6.27             -1.784 downtrend_blocked_slope_and_streak           False                  False
  GILD           87.10               31            0.38              0.34        130.06                32.59         0.542          pass              0.539             52.0                           0.330               -2.62             -0.043           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-08-03T10:30:03.009484-04:00 early_entry_1030 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:25:02.838853-04:00 early_entry_1025 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:20:02.187581-04:00 early_entry_1020 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:15:04.011672-04:00 early_entry_1015 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:10:03.982772-04:00 early_entry_1010 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:05:02.768000-04:00 early_entry_1005 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:05:02.768000-04:00      manage_1000               exit       {"asset_type": "option", "contract_symbol": "CSX260918C00050000", "fill_price": 1.7325, "pnl": -1655.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSX"}
2026-08-03T10:00:05.013413-04:00 early_entry_1000 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:00:05.013413-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.055, "pnl": 3663.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 22.2, "ticker": "PYPL"}
2026-08-03T03:00:01.318857-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260803103003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260803103003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260803103003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260803103003)

</details>
