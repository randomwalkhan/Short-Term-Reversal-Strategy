# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-07 13:30:04 EDT`
Last processed slot: `manage_1330`

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

- Cash: `$53,034.30`
- Equity: `$106,109.30`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$962.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   1     55     52112.5                 53075.0         9.48           9.65      160.14         160.2          bid_ask_mid                       9.65                bid_ask_mid                    True           962.5                   1.85         83.33               12               2.4         42.26           44.23                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           81.48               27            4.20              4.83        162.19               111.15         0.619          pass              0.353             46.2                           0.667                7.59              1.270                                 ok            True                  False
   CEG           90.62               32            0.84              1.77        299.64                58.89         0.552          pass              0.731             81.9                           0.833               12.88              1.058                                 ok            True                   True
   KDP           93.75               16            1.12              0.24         31.03                26.61         0.542          pass              0.485              7.9                           0.199               -2.38             -0.200                                 ok            True                  False
  MPWR           81.25               16            3.21             33.08       1459.51                53.62         0.527          pass              0.194             22.5                           0.379                5.39              0.944                                 ok            True                  False
  UPRO           82.76               29            0.71              0.77        156.08                30.90         0.507          pass              0.452             67.1                           0.746                3.33              0.356                                 ok            True                  False
  NVDA           88.00               25            0.80              1.34        238.66                24.15         0.502          pass              0.456             30.7                           0.405                5.24              0.679                                 ok            True                  False
  META           61.54               13            1.87              9.68        734.73                55.45         0.597          pass              0.153             24.5                           0.388               -2.56             -0.324            downtrend_blocked_slope           False                  False
   STX           88.57               35            0.67              3.78        804.01                69.91         0.568          pass              0.687             78.2                           0.656              -13.31             -1.284            downtrend_blocked_slope           False                  False
  QCOM           78.95               19            2.64              3.35        179.60                56.22         0.544          pass              0.162             15.8                           0.252              -10.64             -1.106 downtrend_blocked_slope_and_streak           False                  False
  SNPS           82.93               41            0.38              1.34        504.60                54.22         0.531          pass              0.538             69.0                           0.746               21.84              2.344                                 ok           False                  False
   WDC           80.00               30            1.66              4.78        408.99                66.20         0.526          pass              0.340             51.3                           0.560              -14.67             -1.286            downtrend_blocked_slope           False                  False
  ASML           72.73               22            1.53             19.69       1825.66                39.86         0.516          pass              0.291             53.1                           0.634                3.52              0.644                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-10-07T12:00:04.521112-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:55:05.517664-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:50:05.710520-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:45:01.712221-04:00 early_entry_1145 early_entry_shadow      {"contract_symbol": "FTNT261120C00190000", "current_drop_pct": 0.59, "early_entry_score": 0.723, "early_reclaim_pct": 65.3, "entry_ask": 16.2, "entry_bid": 14.2, "entry_mode": "early", "entry_option_price": 15.2, "hypothetical_budget": 26517.15, "hypothetical_contracts": 17, "matched_signals": 42, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 13.16, "option_volume": 11.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.68, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.723, "early_reclaim_pct": 65.3, "matched_signals": 42, "recovery_stability_score": 0.68, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-07T11:40:04.680085-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:35:06.426609-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:30:05.653907-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:25:06.559799-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:20:05.827676-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:15:06.288558-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "FTNT261120C00190000", "current_drop_pct": 0.62, "early_entry_score": 0.716, "early_reclaim_pct": 63.1, "entry_ask": 15.75, "entry_bid": 14.2, "entry_mode": "early", "entry_option_price": 14.975, "hypothetical_budget": 26517.15, "hypothetical_contracts": 17, "matched_signals": 42, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 10.35, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.724, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.476, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.716, "early_reclaim_pct": 63.1, "matched_signals": 42, "recovery_stability_score": 0.724, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.476, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261007133004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261007133004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261007133004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261007133004)

</details>
