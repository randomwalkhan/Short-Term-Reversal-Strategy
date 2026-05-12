# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 09:55:01 EDT`
Last processed slot: `manage_1000`

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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$35,353.50`
- Equity: `$35,353.50`
- Realized PnL: `$25,353.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           88.37               43            0.76              0.47         87.11               115.89         0.704          pass              0.702             69.5                           0.404               24.29              2.571                  ok            True                  False
  INTC          100.00               19            3.21              2.91        128.19               104.15         0.637          pass              0.656             44.1                           0.681               48.23              3.992                  ok            True                  False
  FTNT           93.94               33            1.07              0.87        115.07                70.54         0.598          pass              0.645             20.0                           0.215               33.22              3.600                  ok            True                  False
  GOOG           88.24               34            0.67              1.81        385.99                39.86         0.554          pass              0.569             44.7                           0.365               10.56              1.049                  ok            True                  False
  INTU           88.89               27            1.17              3.22        391.91                46.70         0.547          pass              0.505             33.3                           0.219               -2.92             -0.119                  ok            True                  False
    ZS           83.33               30            1.40              1.46        148.25                59.15         0.547          pass              0.288              3.7                           0.058                7.88              1.257                  ok            True                  False
   XEL           91.67               12            1.38              0.78         80.27                27.14         0.537          pass              0.547             56.3                           0.347                0.01             -0.090                  ok            True                  False
  ASML           87.50               16            2.96             32.41       1551.92                49.29         0.530          pass              0.309              5.2                           0.221                9.75              1.325                  ok            True                  False
  CDNS           96.67               30            1.31              3.34        362.77                37.36         0.520          pass              0.670             28.3                           0.255               10.49              1.169                  ok            True                  False
   CSX           86.21               29            0.80              0.25         44.63                30.07         0.517          pass              0.363              6.5                           0.171               -1.88             -0.125                  ok            True                  False
  SBUX           96.77               31            0.94              0.69        105.44                32.96         0.511          pass              0.758             55.8                           0.323                7.68              0.316                  ok            True                  False
   STX           91.67               24            2.52             14.71        827.71                54.89         0.502          pass              0.547             30.8                           0.450               40.41              3.059                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-11T12:00:16.292660-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:53:58.426024-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:47:42.065930-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:41:24.132378-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:35:07.512033-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:28:46.452605-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:22:14.545933-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:15:52.009097-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:09:25.222860-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:02:58.554215-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512095501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512095501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512095501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512095501)

</details>
