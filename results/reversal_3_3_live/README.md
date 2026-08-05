# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 14:20:01 EDT`
Last processed slot: `manage_1430`

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

- Cash: `$31,840.75`
- Equity: `$31,840.75`
- Realized PnL: `$21,840.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-05)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   PEP     option         option PEP260918C00140000     40          2026-08-04         2026-08-05          4.1        3.69 -1640.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  PYPL           91.18               34            0.67              0.27         58.42                60.15         0.613          pass              0.752             77.5                           0.430                4.76              0.481                       ok            True                  False
 CMCSA           83.33               12            1.42              0.25         24.82                44.00         0.598          pass              0.283             40.3                           0.558                4.49              1.001                       ok            True                  False
  CTAS           90.00               20            1.33              1.90        202.84                37.77         0.582          pass              0.486             31.4                           0.373               -0.21             -0.118                       ok            True                  False
  MRVL           80.00               35            1.94              2.96        217.32               100.52         0.569          pass              0.365             47.0                           0.377                1.59              0.253                       ok            True                  False
  PAYX          100.00               21            0.63              0.52        118.44                35.13         0.562          pass              0.768             79.5                           0.701                7.58              0.770                       ok            True                  False
  MSFT           81.58               38            0.55              1.88        492.00                57.86         0.550          pass              0.471             62.2                           0.607               25.56              3.080                       ok            True                  False
  CPRT           87.50               16            2.26              0.47         29.20                38.86         0.511          pass              0.352             20.4                           0.332                5.76              0.597                       ok            True                  False
  DRAM           75.00               36            0.08              0.03         54.88               109.93         0.740          pass              0.541             97.9                           0.681               -5.06             -0.553 downtrend_blocked_streak           False                  False
  SOXL           78.79               33            2.94              2.88        138.66               182.46         0.735          pass              0.402             58.4                           0.515              -15.66             -1.798 downtrend_blocked_streak           False                  False
  AMAT           90.91               33            1.01              3.85        544.97                87.24         0.658          pass              0.707             65.7                           0.533               -2.31             -0.291 downtrend_blocked_streak           False                  False
  TMUS           83.33                6            2.67              3.32        175.79                55.59         0.638          pass              0.217             21.4                           0.323               -9.67             -0.459  downtrend_blocked_slope           False                  False
  LRCX           86.21               29            1.57              3.49        316.25                92.33         0.627          pass              0.534             59.8                           0.559               -2.05             -0.115 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                         detail
2026-08-05T12:00:04.693066-04:00 early_entry_1200 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:55:03.663510-04:00 early_entry_1155 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:50:01.727726-04:00 early_entry_1150 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:50:01.727726-04:00      manage_1200               exit {"asset_type": "option", "contract_symbol": "PEP260918C00140000", "fill_price": 3.69, "pnl": -1640.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PEP"}
2026-08-05T11:45:04.673736-04:00 early_entry_1145 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:40:04.834796-04:00 early_entry_1140 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:35:01.719935-04:00 early_entry_1135 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:30:04.698899-04:00 early_entry_1130 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:25:03.699168-04:00 early_entry_1125 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:20:04.670230-04:00 early_entry_1120 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805142001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805142001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805142001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805142001)

</details>
