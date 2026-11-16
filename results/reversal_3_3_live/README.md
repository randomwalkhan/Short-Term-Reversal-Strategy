# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 09:40:05 EST`
Last processed slot: `manage_0930`

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

- Cash: `$117,024.80`
- Equity: `$117,024.80`
- Realized PnL: `$107,024.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  QCOM           88.89               36            0.70              0.85        172.11                68.34         0.586          pass              0.688             72.9                           0.746                5.66              0.746                      ok            True                   True
  ABNB           81.82               22            1.50              1.97        185.94                54.57         0.586          pass              0.352             54.8                           0.451                7.52              0.909                      ok            True                  False
   CEG           84.62               39            0.53              1.04        279.33                61.55         0.560          pass              0.604             77.2                           0.847                8.18              1.273                      ok            True                  False
  MSFT           96.67               30            0.82              3.02        522.58                36.51         0.534          pass              0.587              0.0                           0.243                2.45             -0.082                      ok            True                  False
  AMZN           80.00               15            2.02              3.76        265.05                41.74         0.534          pass              0.137             16.8                           0.174                6.37              0.601                      ok            True                  False
   APP           91.84               49            0.35              1.00        408.67               119.53         0.760          pass              0.793             67.0                           0.364               78.14              5.735                      ok           False                  False
  ALNY           77.78               36            1.00              1.16        164.54               110.81         0.746          pass              0.302             17.9                           0.124                3.41              0.203                      ok           False                  False
  FTNT           78.57               28            1.70              1.51        126.57                93.31         0.697          pass              0.198              2.7                           0.088               -0.91              0.053                      ok           False                  False
  INTC           63.64               11            5.77              2.41         58.63               143.21         0.689          pass              0.123             15.9                           0.252               -6.25              0.142                      ok           False                  False
  UPRO           88.89                9            2.70              2.62        137.44                68.17         0.648          pass              0.334             10.7                           0.204               -3.10             -0.089                      ok           False                  False
   BKR           60.00               10            2.35              0.81         49.09                57.94         0.598          pass              0.096             12.1                           0.137               -8.56             -0.537 downtrend_blocked_slope           False                  False
 GOOGL           66.67                9            2.49              5.16        293.56                54.19         0.588          pass              0.084              8.4                           0.126                3.37              0.517                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-11-16T09:20:05.612126-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {'saved': 91, 'empty': 2}
2026-11-06T16:10:06.061391-05:00      manage_1600               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"asset_type": "option", "contract_symbol": "MDLZ261218C00065000", "fill_price": 2.79, "pnl": -6138.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MDLZ"}
2026-11-06T15:10:05.130683-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-06T15:05:05.959531-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-06T15:00:05.889317-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-06T14:55:04.803922-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-06T14:50:04.935495-05:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"allocated_cash": 61380.0, "asset_type": "option", "contract_symbol": "MDLZ261218C00065000", "contracts": 198, "early_entry_score": 0.675, "entry_mode": "regular", "entry_option_price": 3.1, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 3966.0, "option_spread_pct": 6.45, "option_volume": 43.0, "success_rate": 93.33, "ticker": "MDLZ", "timing_score": 0.574}
2026-11-06T14:50:04.935495-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-06", "training_samples": 6334, "window": 5}
2026-11-06T12:00:04.909641-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:55:04.780197-05:00 early_entry_1155 early_entry_shadow {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.53, "early_entry_score": 0.732, "early_reclaim_pct": 83.7, "entry_ask": 4.3, "entry_bid": 4.05, "entry_mode": "early", "entry_option_price": 4.175, "hypothetical_budget": 61581.4, "hypothetical_contracts": 147, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 4507.0, "option_spread_pct": 5.99, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.712, "shadow_only": true, "success_rate": 89.47, "ticker": "SBUX", "timing_score": 0.419, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.732, "early_reclaim_pct": 83.7, "matched_signals": 38, "recovery_stability_score": 0.712, "success_rate": 89.47, "ticker": "SBUX", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116094005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116094005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116094005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116094005)

</details>
