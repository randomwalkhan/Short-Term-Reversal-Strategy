# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-25 15:30:05 EDT`
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

- Cash: `$18,092.50`
- Equity: `$30,102.50`
- Realized PnL: `$20,612.50`
- Unrealized PnL: `$-510.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260821C00380000       2026-06-25                   0      4     12520.0                 12010.0         31.3          30.02      379.69        377.78          bid_ask_mid                      30.02                bid_ask_mid                    True          -510.0                  -4.07         87.88               33              0.63         52.09           52.08                  76.92                2270.0         1394.0               0.03                      ok
```

## Today's Closed Trades (2026-06-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AVGO           85.71               28            0.99              2.64        380.95                76.92         0.675          pass              0.519             59.9                           0.332                1.83              0.120                                 ok            True                  False
  INTC           94.44               36            0.84              0.78        131.58                97.48         0.623          pass              0.869             82.9                           0.553               22.20              1.805                                 ok            True                   True
   WBD           94.12               17            0.55              0.11         27.15                20.10         0.584          pass              0.557             25.0                           0.357                3.13              0.170                                 ok            True                  False
   TRI           80.00               30            0.66              0.37         80.82                56.19         0.584          pass              0.380             62.8                           0.470               -1.85             -0.195                                 ok            True                  False
  GILD           86.36               22            0.73              0.64        124.88                27.45         0.553          pass              0.385             26.6                           0.345                2.94              0.124                                 ok            True                  False
  SNPS           83.33               12            2.64              8.58        460.34                46.83         0.533          pass              0.202             15.6                           0.133               -1.90              0.073                                 ok            True                  False
  CSCO           96.67               30            0.99              0.83        119.39                40.01         0.532          pass              0.724             45.9                           0.243               -0.20             -0.051                                 ok            True                  False
  UPRO           90.00               30            0.39              0.36        134.54                51.32         0.609          pass              0.681             73.3                           0.332                2.90             -0.087                                 ok           False                  False
   PEP          100.00                4            1.61              1.60        141.58                19.15         0.604          pass              0.523             21.0                           0.436               -3.01             -0.314            downtrend_blocked_slope           False                  False
  META           77.78                9            2.18              8.51        554.15                45.69         0.593          pass              0.152             30.9                           0.297               -4.35             -0.417 downtrend_blocked_slope_and_streak           False                  False
  CDNS           92.31               26            1.55              4.03        370.67                55.72         0.588          pass              0.594             33.6                           0.318               -4.80             -0.401            downtrend_blocked_slope           False                  False
  NVDA           63.64               11            2.44              3.40        197.45                46.92         0.551          pass              0.147             28.5                           0.283               -3.17             -0.340 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-06-25T15:10:04.366784-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-25T15:05:03.502084-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-25T15:00:05.541289-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-25T14:55:02.526574-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-25T14:50:05.514440-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"allocated_cash": 12520.0, "asset_type": "option", "contract_symbol": "AVGO260821C00380000", "contracts": 4, "early_entry_score": 0.654, "entry_mode": "regular", "entry_option_price": 31.3, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 2270.0, "option_spread_pct": 3.19, "option_volume": 1394.0, "success_rate": 87.88, "ticker": "AVGO", "timing_score": 0.668}
2026-06-25T14:50:05.514440-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-25", "training_samples": 5306, "window": 5}
2026-06-25T11:55:33.596906-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "DASH260821C00175000", "current_drop_pct": 0.94, "early_entry_score": 0.857, "early_reclaim_pct": 70.1, "entry_ask": 18.3, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 17.95, "hypothetical_budget": 15306.25, "hypothetical_contracts": 8, "matched_signals": 42, "option_liquidity_status": "low_volume", "option_open_interest": 954.0, "option_spread_pct": 3.9, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.556, "shadow_only": true, "success_rate": 95.24, "ticker": "DASH", "timing_score": 0.468, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.857, "early_reclaim_pct": 70.1, "matched_signals": 42, "recovery_stability_score": 0.556, "success_rate": 95.24, "ticker": "DASH", "timing_score": 0.468, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-25T11:12:19.435736-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-25T10:28:17.676892-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-25T09:18:02.513254-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260625153005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260625153005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260625153005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260625153005)

</details>
