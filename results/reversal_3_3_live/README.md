# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-26 10:35:51 EDT`
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

- Cash: `$29,360.50`
- Equity: `$29,360.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  AVGO     option         option AVGO260821C00380000      4          2026-06-25         2026-06-26         31.3       28.17 -1252.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
    MU           88.24               17            3.35             28.49       1201.35               127.35         0.714          pass              0.508             56.7                           0.553               17.77              1.604                      ok            True                  False
  DRAM           92.31               13            4.41              2.37         75.87               122.54         0.693          pass              0.536             39.6                           0.500               12.87              1.276                      ok            True                  False
  KLAC           90.00               10            3.99              7.22        255.71                93.32         0.639          pass              0.421             30.3                           0.484                3.04              0.184                      ok            True                  False
  INTC           91.67               24            2.36              2.19        131.93                97.28         0.622          pass              0.639             57.5                           0.566               10.93              1.146                      ok            True                  False
  AMAT           90.91               11            3.84             17.95        660.31                87.16         0.592          pass              0.484             42.4                           0.585               16.23              1.418                      ok            True                  False
  LRCX          100.00               10            4.76             13.39        396.08                86.42         0.536          pass              0.544             30.3                           0.420                5.64              0.578                      ok            True                  False
  PCAR           82.61               23            1.01              0.86        121.31                36.28         0.533          pass              0.409             66.6                           0.690                2.44              0.077                      ok            True                  False
  SOXL           90.00               10           11.83             20.92        243.64               236.70         0.506          pass              0.383             21.8                           0.291               -0.57              0.045                      ok            True                  False
  MRVL          100.00               16            4.52              8.89        277.45               155.27         0.788          pass              0.598             26.5                           0.274               -4.33             -0.423 downtrend_blocked_slope           False                  False
  AVGO           75.00               12            2.93              7.78        375.57                76.91         0.656          pass              0.132             17.7                           0.283               -4.46             -0.292 downtrend_blocked_slope           False                  False
   TXN           88.89                9            3.02              6.59        308.99                63.36         0.629          pass              0.361             20.3                           0.339                1.78              0.196                      ok           False                  False
  ASML           95.24               21            2.48             31.97       1827.48                66.48         0.601          pass              0.647             37.9                           0.541               -5.47             -0.490 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-06-26T10:35:51.274137-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-26T10:35:51.274137-04:00      manage_1030               exit                                                                                                                                                                                                                                                      {"asset_type": "option", "contract_symbol": "AVGO260821C00380000", "fill_price": 28.17, "pnl": -1252.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "AVGO"}
2026-06-26T10:15:51.250947-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-26T00:00:07.288133-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                          {'saved': 93}
2026-06-25T15:10:04.366784-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-25T15:05:03.502084-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-25T15:00:05.541289-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-25T14:55:02.526574-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-25T14:50:05.514440-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-25", "training_samples": 5306, "window": 5}
2026-06-25T14:50:05.514440-04:00       entry_1500              entry {"allocated_cash": 12520.0, "asset_type": "option", "contract_symbol": "AVGO260821C00380000", "contracts": 4, "early_entry_score": 0.654, "entry_mode": "regular", "entry_option_price": 31.3, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 2270.0, "option_spread_pct": 3.19, "option_volume": 1394.0, "success_rate": 87.88, "ticker": "AVGO", "timing_score": 0.668}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260626103551)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260626103551)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260626103551)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260626103551)

</details>
