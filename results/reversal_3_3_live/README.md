# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-01 10:50:06 EDT`
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

- Cash: `$81,364.30`
- Equity: `$81,364.30`
- Realized PnL: `$71,364.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  META     option         option META261120C00735000      8          2026-09-30         2026-10-01       48.425     43.5825 -3874.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           86.84               38            0.64              0.54        120.00                73.63         0.592            pass              0.648             73.2                           0.708                9.80              0.545                                 ok            True                  False
  AMGN           78.57               14            1.38              4.07        419.76                46.02         0.613            pass              0.202             38.0                           0.279                9.46              0.991                                 ok           False                  False
  DRAM           80.56               36            0.10              0.04         60.34                53.77         0.577            pass              0.528             94.1                           0.770                4.36              0.111                                 ok           False                  False
   WBD           95.56               45            0.02              0.00         30.95                37.62         0.557            pass              0.881             75.0                           0.415                9.58              0.818                                 ok           False                  False
  CRWD           89.13               46            0.05              0.10        264.71                63.45         0.550            pass              0.790             97.3                           0.599                7.69              0.901                                 ok           False                  False
  ASML           83.33               36            0.41              5.16       1809.46                42.37         0.534            pass              0.477             53.8                           0.422               10.72              0.951                                 ok           False                  False
  QCOM           92.68               41            0.07              0.09        184.00                56.29         0.528            pass              0.863             90.7                           0.629               -2.54             -0.216           downtrend_blocked_streak           False                  False
   XEL           82.35               17            0.74              0.37         70.32                18.32         0.519            pass              0.301             46.4                           0.547               -4.99             -0.450            downtrend_blocked_slope           False                  False
   EXC           81.25               16            0.79              0.22         40.30                14.97         0.500 below_threshold              0.261             45.8                           0.559               -6.00             -0.590 downtrend_blocked_slope_and_streak           False                  False
  NXPI           85.71               35            0.43              0.71        237.22                38.88         0.498 below_threshold              0.525             52.0                           0.483                3.76              0.364                                 ok           False                  False
  NFLX           68.75               16            1.85              0.90         69.19                37.25         0.498 below_threshold              0.131             13.8                           0.313               -9.31             -0.752            downtrend_blocked_slope           False                  False
    MU           89.66               29            1.52             11.30       1060.27                49.56         0.494 below_threshold              0.619             61.7                           0.822                7.31              0.485                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-10-01T10:50:06.456306-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:45:05.877463-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:40:06.481988-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:35:05.852380-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "INTC261030C00119000", "current_drop_pct": 0.72, "early_entry_score": 0.681, "early_reclaim_pct": 70.0, "entry_ask": 9.65, "entry_bid": 9.45, "entry_mode": "early", "entry_option_price": 9.55, "hypothetical_budget": 40682.15, "hypothetical_contracts": 42, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 353.0, "option_spread_pct": 2.09, "option_volume": 30.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.664, "shadow_only": true, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.601, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.681, "early_reclaim_pct": 70.0, "matched_signals": 36, "recovery_stability_score": 0.664, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.601, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-01T10:30:06.297873-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:25:05.417104-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:20:05.454377-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:20:05.454377-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "META261120C00735000", "fill_price": 43.5825, "pnl": -3874.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "META"}
2026-10-01T10:15:02.462190-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:10:05.306830-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261001105006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261001105006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261001105006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261001105006)

</details>
