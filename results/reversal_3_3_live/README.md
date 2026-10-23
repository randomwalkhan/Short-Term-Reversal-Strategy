# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-23 15:30:05 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$1,161.80`
- Equity: `$148,359.30`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$3,527.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option  EXC261218C00045000       2026-10-23                   0    657     72270.0                 77197.5         1.10           1.18       44.42         44.51          bid_ask_mid                       1.18                bid_ask_mid                    True          4927.5                   6.82          80.0               15              0.97         20.09           21.07                  20.91                 278.0           48.0               0.09                      ok
  TEAM     option         option TEAM261120C00230000       2026-10-22                   1     40     71400.0                 70000.0        17.85          17.50      223.97        224.59          bid_ask_mid                      17.50                bid_ask_mid                    True         -1400.0                  -1.96         100.0               38              0.68         80.16           79.00                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           93.33               15            1.17              0.29         35.07                27.06         0.555          pass              0.571             42.3                           0.380                9.51              0.910                                 ok            True                  False
   KHC           86.96               23            1.06              0.19         25.01                34.71         0.524          pass              0.476             50.5                           0.682               11.47              1.109                                 ok            True                  False
  COST           81.82               11            1.41             10.07       1013.90                17.03         0.517          pass              0.129              7.4                           0.263                6.01              0.643                                 ok            True                  False
   ADP           91.30               23            0.71              1.53        307.29                23.94         0.513          pass              0.647             69.1                           0.647               12.88              1.239                                 ok            True                  False
  ORLY          100.00               13            1.66              1.07         91.54                17.78         0.508          pass              0.527             18.6                           0.386                4.65              0.598                                 ok            True                  False
   AEP           85.00               20            0.81              0.74        130.32                17.81         0.507          pass              0.395             48.0                           0.672                5.52              0.483                                 ok            True                  False
   EXC           86.96               23            0.76              0.24         44.75                20.91         0.504          pass              0.467             48.1                           0.630                6.59              0.580                                 ok            True                  False
   CEG           85.29               34            0.68              1.21        254.69                65.49         0.594          pass              0.595             78.3                           0.720              -14.96             -1.671 downtrend_blocked_slope_and_streak           False                  False
  MDLZ          100.00                1            2.25              1.03         64.75                24.03         0.571          pass              0.512             18.4                           0.467                5.49              0.537                                 ok           False                  False
   STX           72.97               37            0.89              4.00        640.43                72.64         0.544          pass              0.453             73.0                           0.492              -18.72             -1.853 downtrend_blocked_slope_and_streak           False                  False
   XEL           75.00                8            1.21              0.67         78.68                16.59         0.535          pass              0.160             35.6                           0.649                5.73              0.587                                 ok           False                  False
   MAR           75.00                8            1.64              4.54        394.85                21.06         0.534          pass              0.053              0.0                           0.247                6.68              0.916                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-10-23T15:10:05.007293-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-23T15:05:06.359707-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-23T15:00:05.816544-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-23T14:55:04.189334-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-23T14:50:05.144728-04:00       entry_1500                   entry {"allocated_cash": 72270.0, "asset_type": "option", "contract_symbol": "EXC261218C00045000", "contracts": 657, "early_entry_score": 0.187, "entry_mode": "regular", "entry_option_price": 1.1, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 278.0, "option_spread_pct": 9.09, "option_volume": 48.0, "success_rate": 80.0, "ticker": "EXC", "timing_score": 0.532}
2026-10-23T14:50:05.144728-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                            {"early_entry_score": 0.573, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 3202.0, "option_spread_pct": 23.73, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "KDP", "timing_score": 0.556}
2026-10-23T14:50:05.144728-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-23", "training_samples": 6184, "window": 5}
2026-10-23T12:00:05.040170-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T11:55:05.962130-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T11:50:05.123171-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261023153005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261023153005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261023153005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261023153005)

</details>
