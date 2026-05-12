# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 11:45:01 EDT`
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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$33,603.50`
- Equity: `$33,603.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-12)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS260618C00520000      5          2026-05-12         2026-05-12         35.0        31.5 -1750.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           87.50               40            1.09              0.66         87.03               115.89         0.702          pass              0.639             56.4                           0.430               23.88              2.556                                 ok            True                  False
  FTNT           93.94               33            0.96              0.78        115.11                70.54         0.601          pass              0.698             37.6                           0.331               33.38              3.606                                 ok            True                  False
   XEL           91.67               12            1.33              0.75         80.28                27.14         0.539          pass              0.552             57.9                           0.402                0.06             -0.088                                 ok            True                  False
    ZS           82.86               35            1.06              1.11        148.40                59.15         0.531          pass              0.420             41.5                           0.330                8.25              1.272                                 ok            True                  False
  INTU           88.57               35            0.73              2.01        392.43                46.70         0.523          pass              0.623             58.4                           0.327               -2.49             -0.099                                 ok            True                  False
  CDNS           95.83               24            1.84              4.69        362.19                37.36         0.522          pass              0.602             18.9                           0.389                9.90              1.145                                 ok            True                  False
  MNST           85.71               35            0.62              0.37         86.25                49.64         0.516          pass              0.614             81.3                           0.536               11.25              1.208                                 ok            True                  False
  WDAY           88.64               44            0.54              0.46        121.22                61.87         0.513          pass              0.621             46.4                           0.264               -0.34              0.089                                 ok            True                  False
   CSX           86.67               30            0.75              0.23         44.64                30.07         0.510          pass              0.467             35.0                           0.575               -1.82             -0.123                                 ok            True                  False
 CMCSA           92.31               26            0.64              0.11         24.98                62.25         0.681          pass              0.594             30.4                           0.288              -10.02             -0.989 downtrend_blocked_slope_and_streak           False                  False
   TXN           85.71                7            2.79              5.82        295.27                67.69         0.680          pass              0.265             14.9                           0.325                9.78              0.932                                 ok           False                  False
  SHOP           89.19               37            1.11              0.80        102.20                84.99         0.647          pass              0.557             22.4                           0.252              -16.92             -2.120            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-12T11:45:01.039711-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:40:05.033124-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:35:01.042494-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:30:01.054285-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:25:05.158793-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:20:04.203525-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:15:02.113250-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:10:01.083696-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:05:04.072050-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:00:02.153694-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512114501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512114501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512114501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512114501)

</details>
