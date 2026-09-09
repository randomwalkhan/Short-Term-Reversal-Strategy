# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-09 10:15:03 EDT`
Last processed slot: `early_entry_1015`

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

- Cash: `$39,968.10`
- Equity: `$77,343.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$195.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD261016C00210000       2026-09-08                   1     26     37180.0                 37375.0         14.3          14.38      209.63        208.93          bid_ask_mid                      14.38                bid_ask_mid                    True           195.0                   0.52         88.89               36              1.63         52.75            55.9                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   PEP           92.86               14            0.73              0.71        138.15                16.46         0.555          pass              0.485             19.8                           0.277               -2.36             -0.192                                 ok            True                  False
   WMT           85.29               34            0.56              0.42        105.87                40.18         0.541          pass              0.455             33.1                           0.359                0.07              0.282                                 ok            True                  False
  NVDA           90.91               33            0.76              1.20        225.21                44.12         0.538          pass              0.528              9.9                           0.117                5.14              0.629                                 ok            True                  False
  LRCX           82.93               41            0.56              1.25        319.89                52.73         0.510          pass              0.546             72.3                           0.686                1.26             -0.049                                 ok            True                  False
  TMUS           91.67               12            1.65              2.09        180.79                25.45         0.504          pass              0.410             11.8                           0.174               -1.03              0.188                                 ok            True                  False
  MSFT           89.29               28            0.65              2.26        492.98                23.28         0.500          pass              0.436              6.0                           0.073               -0.20             -0.087                                 ok            True                  False
  MSTR           85.00               40            0.36              0.35        136.37               103.38         0.709          pass              0.461             18.9                           0.102                7.25              0.962                                 ok           False                  False
  CRWD           91.30               46            0.36              0.54        209.79                89.86         0.658          pass              0.716             49.7                           0.285               12.88              0.602                                 ok           False                  False
   STX           86.84               38            0.13              0.85        904.02                74.46         0.627          pass              0.711             93.0                           0.720                9.92              0.586                                 ok           False                  False
  WDAY           92.50               40            0.42              0.55        186.05                77.37         0.623          pass              0.809             71.2                           0.637               -4.59             -0.234                                 ok           False                  False
   KHC          100.00               18            0.22              0.04         24.88                28.58         0.606          pass              0.762             82.8                           0.786               -0.31              0.073                                 ok           False                  False
  PYPL           94.74               38            0.17              0.06         53.15                58.35         0.588          pass              0.921             94.3                           0.829              -14.53             -1.412 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-09-09T10:15:03.852683-04:00 early_entry_1015 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:10:05.084916-04:00 early_entry_1010 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:05:03.958272-04:00 early_entry_1005 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:00:05.981446-04:00 early_entry_1000 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T00:00:04.345374-04:00     data_refresh       data_refresh                                                                                                {'saved': 93}
2026-09-08T15:10:02.485838-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-08T15:05:04.629730-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-08T15:00:03.621763-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-08T14:55:03.619621-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-08T14:50:01.652709-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-08", "training_samples": 5748, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260909101503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260909101503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260909101503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260909101503)

</details>
