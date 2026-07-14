# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-14 15:10:01 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$4,915.25`
- Equity: `$26,692.75`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$-302.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL260821C00315000       2026-07-14                   0     11     12705.0                 12787.5        11.55          11.62      315.21        315.60          bid_ask_mid                      11.62                bid_ask_mid                    True            82.5                   0.65         95.83               24              0.66         28.20           27.85                  35.57               11042.0         1070.0               0.02                      ok
  META     option         option META260821C00660000       2026-07-13                   1      2      9375.0                  8990.0        46.88          44.95      660.72        658.86          bid_ask_mid                      44.95                bid_ask_mid                    True          -385.0                  -4.11         81.82               22              1.27         53.38           53.02                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN           94.12               17            1.12              2.82        359.24                21.45         0.551          pass              0.567             29.7                           0.415               -1.15             -0.087                                 ok            True                  False
  GILD           88.46               26            0.65              0.59        131.15                32.97         0.545          pass              0.558             57.1                           0.585                3.34              0.423                                 ok            True                  False
  PAYX          100.00               22            1.13              0.88        110.37                31.82         0.544          pass              0.746             70.5                           0.413                9.70              0.939                                 ok            True                  False
  CTAS           90.62               32            0.73              0.94        183.35                31.28         0.502          pass              0.659             59.5                           0.670                7.88              0.657                                 ok            True                  False
   KHC           88.89                9            0.91              0.16         25.16                36.18         0.665          pass              0.446             47.5                           0.531                3.35              0.333                                 ok           False                  False
  MDLZ          100.00                3            1.79              0.75         59.54                31.17         0.638          pass              0.494             10.1                           0.252               -1.44              0.005                                 ok           False                  False
   ADP          100.00                6            2.05              3.61        249.50                31.20         0.585          pass              0.583             41.4                           0.315                9.30              0.825                                 ok           False                  False
   PEP           83.33                6            2.01              1.95        137.65                30.22         0.583          pass              0.147              0.0                           0.215               -2.15             -0.148                                 ok           False                  False
   XEL          100.00               23            0.40              0.22         80.38                22.03         0.567          pass              0.683             46.7                           0.359               -2.22             -0.138                                 ok           False                  False
  AAPL           96.67               30            0.49              1.09        316.84                35.57         0.561          pass              0.819             76.5                           0.704               12.07              1.131                                 ok           False                  False
   KDP           75.00                4            2.67              0.58         31.00                34.17         0.556          pass              0.071              5.1                           0.167               -9.21             -0.838 downtrend_blocked_slope_and_streak           False                  False
   EXC           95.45               22            0.45              0.15         47.03                22.01         0.552          pass              0.770             78.4                           0.492               -0.58              0.003                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-07-14T15:10:01.456053-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-14T15:05:02.308534-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-14T15:00:04.423415-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-14T14:55:01.276896-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-14T14:50:02.479277-04:00       entry_1500              entry {"allocated_cash": 12705.0, "asset_type": "option", "contract_symbol": "AAPL260821C00315000", "contracts": 11, "early_entry_score": 0.757, "entry_mode": "regular", "entry_option_price": 11.55, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 11042.0, "option_spread_pct": 1.73, "option_volume": 1070.0, "success_rate": 95.83, "ticker": "AAPL", "timing_score": 0.589}
2026-07-14T14:50:02.479277-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-14", "training_samples": 5400, "window": 5}
2026-07-14T12:00:02.352813-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:55:01.322008-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:50:02.227286-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:45:01.430125-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260714151001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260714151001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260714151001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260714151001)

</details>
