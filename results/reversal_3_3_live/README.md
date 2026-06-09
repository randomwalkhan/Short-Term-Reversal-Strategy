# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 12:35:06 EDT`
Last processed slot: `manage_1230`

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

- Cash: `$30,222.25`
- Equity: `$30,222.25`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM260717C00100000     17          2026-06-08         2026-06-09         9.25       8.325 -1572.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           86.96               23            0.81              0.47         82.98                69.62         0.691          pass              0.483             47.2                           0.384               -1.45             -0.096                                 ok            True                  False
  CTSH           92.86               28            0.86              0.32         52.85                51.28         0.579          pass              0.671             50.0                           0.420                1.40             -0.120                                 ok            True                  False
  ASML           94.74               19            2.56             31.37       1735.60                54.47         0.501          pass              0.554             17.1                           0.167                4.42              0.795                                 ok            True                  False
    ZS           50.00                6            5.54              5.01        127.10               157.94         0.779          pass              0.097              6.2                           0.161              -33.86             -1.976            downtrend_blocked_slope           False                  False
  INTU           54.55               11            4.25              9.08        301.62               100.92         0.617          pass              0.072              1.3                           0.083               -3.88             -0.637 downtrend_blocked_slope_and_streak           False                  False
   CEG           75.00               28            1.26              2.20        249.73                55.25         0.571          pass              0.205              9.2                           0.190              -17.92             -1.876 downtrend_blocked_slope_and_streak           False                  False
  MSFT           66.67                3            2.54              7.32        408.60                36.13         0.570          pass              0.079              7.2                           0.205               -3.55             -0.399            downtrend_blocked_slope           False                  False
  CDNS          100.00                6            3.20              8.84        390.45                58.79         0.569          pass              0.515             19.4                           0.252               -0.04              0.363                                 ok           False                  False
  ADSK           92.00               25            1.35              2.12        224.13                42.71         0.542          pass              0.531             19.0                           0.266               -6.81             -0.689            downtrend_blocked_slope           False                  False
   ADI          100.00                1            4.00             11.32        399.04                49.72         0.533          pass              0.470              5.4                           0.090               -7.42             -0.418            downtrend_blocked_slope           False                  False
  TTWO           95.45               22            1.61              2.40        211.52                37.58         0.525          pass              0.588             18.5                           0.310               -5.23             -0.496            downtrend_blocked_slope           False                  False
   CSX           92.86               28            0.42              0.14         47.05                21.30         0.507          pass              0.715             67.2                           0.460                0.95              0.180                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-09T12:00:03.055569-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:55:04.019844-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:50:02.014967-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:45:02.008648-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:40:06.401362-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:35:02.395564-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:30:02.013445-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:25:01.954572-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:20:06.212106-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:15:02.033784-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609123506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609123506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609123506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609123506)

</details>
