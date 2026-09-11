# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-11 10:50:05 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$76,116.10`
- Equity: `$76,116.10`
- Realized PnL: `$66,116.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-11)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  MSTR     option         option MSTR261016C00130000     30          2026-09-10         2026-09-11       11.525       13.65 6375.0   18.438178 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           84.85               33            1.78              2.60        207.75                89.85         0.637            pass              0.369              7.7                           0.115              -10.01             -0.931            downtrend_blocked_slope           False                  False
  AMGN          100.00               20            0.85              2.29        381.49                44.93         0.631            pass              0.602             24.0                           0.305              -13.22             -1.556 downtrend_blocked_slope_and_streak           False                  False
   PEP           90.48               21            0.14              0.13        136.59                17.04         0.560            pass              0.536             42.4                           0.273               -1.29             -0.186                                 ok           False                  False
    ZS           97.78               45            0.02              0.02        163.47                64.41         0.553            pass              0.952             98.9                           0.500              -12.73             -1.588            downtrend_blocked_slope           False                  False
    MU           87.18               39            0.29              1.98        976.56                56.22         0.549            pass              0.655             71.8                           0.416                4.19              0.727                                 ok           False                  False
   EXC           94.44               18            0.32              0.10         43.35                15.10         0.546            pass              0.683             63.2                           0.306               -0.68              0.007                                 ok           False                  False
  TEAM           94.12               34            1.20              1.51        178.92                63.98         0.541            pass              0.659             22.9                           0.378               -4.42             -0.751            downtrend_blocked_slope           False                  False
  PANW           66.67               24            2.43              5.77        336.02                67.54         0.527            pass              0.175              9.7                           0.178              -13.74             -1.487            downtrend_blocked_slope           False                  False
  REGN          100.00               22            1.10              6.12        790.64                28.70         0.503            pass              0.615             28.4                           0.339               -2.87             -0.164           downtrend_blocked_streak           False                  False
   ROP          100.00               30            0.67              1.83        387.80                26.95         0.498 below_threshold              0.722             46.4                           0.510               -8.69             -1.099 downtrend_blocked_slope_and_streak           False                  False
  FTNT           87.10               31            1.68              1.87        158.05                53.57         0.486 below_threshold              0.469             30.3                           0.173               -9.61             -0.887            downtrend_blocked_slope           False                  False
  VRTX           97.50               40            0.32              1.16        514.06                30.09         0.484 below_threshold              0.735             28.9                           0.246               -6.33             -0.685 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                  detail
2026-09-11T10:50:05.808094-04:00 early_entry_1050 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:45:04.814010-04:00 early_entry_1045 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:40:06.630614-04:00 early_entry_1040 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:35:04.843069-04:00 early_entry_1035 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:30:01.845613-04:00 early_entry_1030 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:25:04.822765-04:00 early_entry_1025 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:20:04.731608-04:00 early_entry_1020 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:15:01.602754-04:00 early_entry_1015 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:10:01.770369-04:00 early_entry_1010 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:05:03.681403-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "MSTR261016C00130000", "fill_price": 13.65, "pnl": 6375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.44, "ticker": "MSTR"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260911105005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260911105005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260911105005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260911105005)

</details>
