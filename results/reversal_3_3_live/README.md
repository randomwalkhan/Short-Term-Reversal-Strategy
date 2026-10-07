# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-07 14:55:05 EDT`
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

- Cash: `$734.30`
- Equity: `$105,946.80`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$800.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   1     55     52112.5                 53212.5         9.48           9.68      160.14        160.95          bid_ask_mid                       9.68                bid_ask_mid                    True          1100.0                   2.11         83.33               12              2.40         42.26           41.71                  40.56                 310.0           20.0               0.06                      ok
  NVDA     option         option NVDA261120C00235000       2026-10-07                   0     40     52300.0                 52000.0        13.08          13.00      236.83        236.72          bid_ask_mid                      13.00                bid_ask_mid                    True          -300.0                  -0.57         90.91               22              1.01         37.07           36.72                  24.15               17037.0         1205.0               0.01                      ok
```

## Today's Closed Trades (2026-10-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           93.33               15            1.25              0.27         31.01                26.61         0.539          pass              0.464              7.1                           0.280               -2.51             -0.206                                 ok            True                  False
  SNPS           82.50               40            0.57              2.02        504.31                54.22         0.526          pass              0.479             53.3                           0.404               21.60              2.335                                 ok            True                  False
  NVDA           90.48               21            1.05              1.76        238.48                24.15         0.515          pass              0.431              9.0                           0.178                4.97              0.668                                 ok            True                  False
  UPRO           82.76               29            0.65              0.71        156.11                30.90         0.510          pass              0.461             69.9                           0.659                3.39              0.359                                 ok            True                  False
  META           68.75               16            1.63              8.41        735.28                55.45         0.601          pass              0.203             34.5                           0.613               -2.32             -0.312            downtrend_blocked_slope           False                  False
  SOXL           79.17               24            4.86              5.59        161.86               111.15         0.599          pass              0.267             37.8                           0.451                6.85              1.239                                 ok           False                  False
   STX           88.24               34            0.91              5.14        803.43                69.91         0.560          pass              0.647             70.3                           0.462              -13.52             -1.295            downtrend_blocked_slope           False                  False
  QCOM           80.00               20            2.58              3.27        179.63                56.22         0.543          pass              0.174             17.8                           0.368              -10.59             -1.103 downtrend_blocked_slope_and_streak           False                  False
   CEG           87.80               41            0.22              0.46        300.20                58.89         0.530          pass              0.747             95.3                           0.795               13.59              1.086                                 ok           False                  False
   WDC           79.31               29            1.84              5.29        408.77                66.20         0.521          pass              0.317             46.1                           0.346              -14.82             -1.294            downtrend_blocked_slope           False                  False
  CSCO           89.74               39            0.04              0.04        117.92                34.67         0.513          pass              0.793             96.3                           0.631               11.20              1.127                                 ok           False                  False
   PEP           87.50                8            1.34              1.18        125.21                14.22         0.513          pass              0.290             13.0                           0.333               -4.72             -0.413            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-10-07T14:55:05.726912-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-10-07T14:50:06.730595-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"allocated_cash": 52300.0, "asset_type": "option", "contract_symbol": "NVDA261120C00235000", "contracts": 40, "early_entry_score": 0.461, "entry_mode": "regular", "entry_option_price": 13.075, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 17037.0, "option_spread_pct": 1.15, "option_volume": 1205.0, "success_rate": 90.91, "ticker": "NVDA", "timing_score": 0.512}
2026-10-07T14:50:06.730595-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"early_entry_score": 0.14, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 17.0, "option_spread_pct": 11.88, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "MPWR", "timing_score": 0.522}
2026-10-07T14:50:06.730595-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"early_entry_score": 0.49, "option_liquidity_status": "low_volume", "option_open_interest": 993.0, "option_spread_pct": 12.24, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "KDP", "timing_score": 0.545}
2026-10-07T14:50:06.730595-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-07", "training_samples": 5970, "window": 5}
2026-10-07T12:00:04.521112-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:55:05.517664-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:50:05.710520-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:45:01.712221-04:00 early_entry_1145      early_entry_shadow {"contract_symbol": "FTNT261120C00190000", "current_drop_pct": 0.59, "early_entry_score": 0.723, "early_reclaim_pct": 65.3, "entry_ask": 16.2, "entry_bid": 14.2, "entry_mode": "early", "entry_option_price": 15.2, "hypothetical_budget": 26517.15, "hypothetical_contracts": 17, "matched_signals": 42, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 13.16, "option_volume": 11.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.68, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.723, "early_reclaim_pct": 65.3, "matched_signals": 42, "recovery_stability_score": 0.68, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-07T11:40:04.680085-04:00 early_entry_1140      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261007145505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261007145505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261007145505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261007145505)

</details>
