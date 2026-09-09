# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-09 10:30:01 EDT`
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

- Cash: `$39,968.10`
- Equity: `$76,303.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$-845.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD261016C00210000       2026-09-08                   1     26     37180.0                 36335.0         14.3          13.98      209.63        209.75          bid_ask_mid                      13.98                bid_ask_mid                    True          -845.0                  -2.27         88.89               36              1.63         52.75           52.18                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  WDAY           91.67               36            0.71              0.92        185.88                77.37         0.628          pass              0.701             51.3                           0.405               -4.87             -0.247                                 ok            True                  False
   WMT           85.29               34            0.56              0.41        105.87                40.18         0.542          pass              0.456             33.7                           0.253                0.08              0.282                                 ok            True                  False
  CPRT           80.00               25            1.50              0.34         32.45                44.55         0.510          pass              0.280             43.0                           0.623               -3.66             -0.089                                 ok            True                  False
   KHC          100.00               20            0.08              0.01         24.89                28.58         0.602          pass              0.808             93.7                           0.815               -0.17              0.080                                 ok           False                  False
  PYPL           94.29               35            0.30              0.11         53.13                58.35         0.597          pass              0.877             90.0                           0.736              -14.64             -1.418 downtrend_blocked_slope_and_streak           False                  False
  PAYX          100.00               16            1.17              0.96        116.52                30.90         0.571          pass              0.577             26.6                           0.366               -7.54             -0.753            downtrend_blocked_slope           False                  False
   PEP          100.00                9            1.05              1.02        138.01                16.46         0.571          pass              0.507             16.6                           0.250               -2.68             -0.206                                 ok           False                  False
  PANW           86.36               44            0.36              0.85        336.61                67.50         0.565          pass              0.642             72.0                           0.376               -1.22             -0.802                                 ok           False                  False
   EXC           92.86               14            0.44              0.14         43.89                15.52         0.561          pass              0.548             40.9                           0.266               -0.31              0.016                                 ok           False                  False
  ADBE           94.74               38            0.17              0.31        257.13                50.01         0.555          pass              0.830             64.8                           0.398               -6.24             -0.815            downtrend_blocked_slope           False                  False
  MELI          100.00                4            3.07             41.33       1908.54                47.09         0.550          pass              0.513             19.4                           0.422               -6.50             -0.229           downtrend_blocked_streak           False                  False
  SBUX           91.67               12            1.33              0.95        101.60                23.45         0.536          pass              0.490             37.3                           0.492               -4.83             -0.551 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-09T10:30:01.975692-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:25:04.909615-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:20:01.984247-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:15:03.852683-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:10:05.084916-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:05:03.958272-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:00:05.981446-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T00:00:04.345374-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-09-08T15:10:02.485838-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-09-08T15:05:04.629730-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260909103001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260909103001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260909103001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260909103001)

</details>
