# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-13 15:55:05 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$19,178.00`
- Equity: `$37,063.00`
- Realized PnL: `$28,043.00`
- Unrealized PnL: `$-980.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   BKR     option         option BKR260918C00065000       2026-08-13                   0     98     18865.0                 17885.0         1.92           1.82       63.47          63.5          bid_ask_mid                       1.82                bid_ask_mid                    True          -980.0                  -5.19         84.21               19              1.26         33.72           31.64                  33.24                2279.0           49.0               0.13                      ok
```

## Today's Closed Trades (2026-08-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  AMAT           87.50               24            2.69             10.33        543.72                85.10         0.619            pass              0.385              9.8                           0.095                6.30              0.511                       ok            True                  False
  MCHP           86.67               30            2.09              1.16         78.94                74.47         0.593            pass              0.370              0.0                           0.150                3.69              0.846                       ok            True                  False
  FAST          100.00               10            1.85              0.68         51.93                25.01         0.572            pass              0.469              4.0                           0.221                9.85              1.134                       ok            True                  False
   BKR           85.71               21            1.22              0.55         64.04                33.24         0.538            pass              0.447             55.9                           0.541                6.39              0.782                       ok            True                  False
  VRTX           93.75               16            1.63              6.00        523.16                27.73         0.521            pass              0.478              6.3                           0.150                7.36              1.174                       ok            True                  False
  INSM           62.50                8            4.29              3.98        130.58               107.72         0.675            pass              0.076              2.7                           0.151               24.74              3.699                       ok           False                  False
  AMZN           79.41               34            0.82              1.53        266.62                61.57         0.628            pass              0.266             14.5                           0.198               12.56              0.434                       ok           False                  False
   MAR           90.91               33            0.64              1.59        353.90                36.15         0.543            pass              0.610             37.0                           0.505               -6.17             -0.473  downtrend_blocked_slope           False                  False
  ROST           85.71               14            1.38              2.40        247.22                22.10         0.529            pass              0.363             43.8                           0.657               -3.07             -0.124 downtrend_blocked_streak           False                  False
  NXPI           74.36               39            0.61              0.99        232.98                51.39         0.529            pass              0.354             36.0                           0.297               -5.37              0.063                       ok           False                  False
   HON           91.89               37            0.47              0.77        235.01                35.57         0.509            pass              0.731             60.9                           0.612               -3.17             -0.593  downtrend_blocked_slope           False                  False
  CTAS           86.36               22            1.23              1.75        202.76                34.24         0.499 below_threshold              0.334             11.5                           0.270               -2.80             -0.124 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-08-13T15:10:04.909039-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-13T15:05:06.030850-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-13T15:00:02.921317-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-13T14:55:04.897309-04:00       entry_1500                   entry {"allocated_cash": 18865.0, "asset_type": "option", "contract_symbol": "BKR260918C00065000", "contracts": 98, "early_entry_score": 0.39, "entry_mode": "regular", "entry_option_price": 1.925, "execution_mode": "option", "matched_signals": 19, "option_liquidity_status": "ok", "option_open_interest": 2279.0, "option_spread_pct": 12.99, "option_volume": 49.0, "success_rate": 84.21, "ticker": "BKR", "timing_score": 0.546}
2026-08-13T14:55:04.897309-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                              {"early_entry_score": 0.522, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 5317.0, "option_spread_pct": 28.57, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "FAST", "timing_score": 0.586}
2026-08-13T14:55:04.897309-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-13", "training_samples": 5661, "window": 5}
2026-08-13T11:55:02.213370-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:53:25.963945-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:45:10.117918-04:00 early_entry_1145      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:40:06.788937-04:00 early_entry_1140      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260813155505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260813155505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260813155505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260813155505)

</details>
