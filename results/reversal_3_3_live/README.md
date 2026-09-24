# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-24 10:05:06 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$67,953.30`
- Equity: `$67,953.30`
- Realized PnL: `$57,953.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261023C00165000     30          2026-09-23         2026-09-24       11.725     10.5525 -3517.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MSTR           94.44               36            0.75              0.85        161.84               109.59         0.766          pass              0.877             80.6                           0.475               21.32              2.760                  ok            True                  False
  CRWD           87.18               39            1.12              2.05        261.61                96.70         0.697          pass              0.533             26.0                           0.229               24.91              2.217                  ok            True                  False
  SOXL           80.65               31            3.31              3.39        144.80               119.42         0.661          pass              0.394             56.7                           0.664               12.42              2.337                  ok            True                  False
  PANW           80.49               41            0.73              2.02        392.43                79.07         0.626          pass              0.471             65.2                           0.407               16.51              1.354                  ok            True                  False
  NVDA           91.67               24            1.27              2.01        224.65                44.57         0.587          pass              0.568             35.1                           0.552               -0.35              0.390                  ok            True                  False
  TEAM          100.00               33            1.43              1.96        194.24                58.95         0.554          pass              0.741             44.2                           0.245                8.18              0.832                  ok            True                  False
  ADSK           82.14               28            1.49              2.26        216.18                55.47         0.551          pass              0.352             40.1                           0.403                3.53              0.237                  ok            True                  False
  MPWR           85.19               27            1.69             16.08       1348.58                51.84         0.550          pass              0.444             45.8                           0.716               10.70              1.216                  ok            True                  False
    MU           89.66               29            1.91             14.34       1065.73                49.67         0.533          pass              0.544             35.5                           0.496                2.30              0.935                  ok            True                  False
  DRAM           82.14               28            2.08              0.90         61.51                51.34         0.529          pass              0.298             22.8                           0.260               -1.58              0.499                  ok            True                  False
  MSFT          100.00               14            1.65              5.78        498.11                22.42         0.522          pass              0.515             12.0                           0.165                0.14              0.067                  ok            True                  False
   WMT           82.35               17            1.22              0.94        110.13                21.22         0.520          pass              0.183              7.2                           0.194                3.17              0.281                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-09-24T10:05:06.327033-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:05:06.327033-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"asset_type": "option", "contract_symbol": "MSTR261023C00165000", "fill_price": 10.5525, "pnl": -3517.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
2026-09-24T10:00:05.543945-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T15:10:05.441341-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-09-23T15:05:06.124690-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-09-23T15:00:04.510549-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-09-23T14:55:06.453181-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-09-23T14:50:06.624928-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"allocated_cash": 35175.0, "asset_type": "option", "contract_symbol": "MSTR261023C00165000", "contracts": 30, "early_entry_score": 0.563, "entry_mode": "regular", "entry_option_price": 11.725, "execution_mode": "option", "matched_signals": 27, "option_liquidity_status": "ok", "option_open_interest": 984.0, "option_spread_pct": 2.13, "option_volume": 82.0, "success_rate": 92.59, "ticker": "MSTR", "timing_score": 0.682}
2026-09-23T14:50:06.624928-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-23", "training_samples": 5799, "window": 5}
2026-09-23T12:00:04.450444-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "PYPL261023C00053000", "current_drop_pct": 0.51, "early_entry_score": 0.756, "early_reclaim_pct": 75.0, "entry_ask": 1.83, "entry_bid": 1.69, "entry_mode": "early", "entry_option_price": 1.76, "hypothetical_budget": 35735.4, "hypothetical_contracts": 203, "matched_signals": 35, "option_liquidity_status": "low_open_interest", "option_open_interest": 0.0, "option_spread_pct": 7.95, "option_volume": 34.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.731, "shadow_only": true, "success_rate": 91.43, "ticker": "PYPL", "timing_score": 0.601, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.756, "early_reclaim_pct": 75.0, "matched_signals": 35, "recovery_stability_score": 0.731, "success_rate": 91.43, "ticker": "PYPL", "timing_score": 0.601, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260924100506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260924100506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260924100506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260924100506)

</details>
