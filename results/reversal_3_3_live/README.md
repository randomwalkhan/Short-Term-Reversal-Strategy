# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-25 10:35:06 EDT`
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

- Cash: `$73,553.30`
- Equity: `$73,553.30`
- Realized PnL: `$63,553.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-25)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  SOXL     option         option SOXL261030C00145000     16          2026-09-24         2026-09-25       20.275      23.775 5600.0   17.262639 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           93.10               29            1.72              1.95        160.78               109.71         0.718          pass              0.649             33.6                           0.438               21.27              2.824                                 ok            True                  False
  CRWD           86.11               36            1.51              2.75        258.49                96.70         0.674          pass              0.545             47.0                           0.564               22.45              2.083                                 ok            True                  False
   TRI           87.10               31            1.11              0.78         99.99                57.78         0.559          pass              0.617             77.2                           0.612                3.66             -0.121                                 ok            True                  False
  FTNT           85.00               20            2.54              3.18        177.31                58.17         0.542          pass              0.308             18.1                           0.310                9.62              1.063                                 ok            True                  False
  INTC           82.86               35            1.52              1.36        126.81                68.53         0.525          pass              0.442             48.8                           0.543               21.87              2.990                                 ok            True                  False
  SHOP           82.61               23            1.94              1.97        144.31                62.63         0.522          pass              0.308             33.3                           0.573               10.52              1.296                                 ok            True                  False
  PANW           62.50               16            3.18              8.68        386.20                80.20         0.594          pass              0.164             21.5                           0.418               11.53              1.187                                 ok           False                  False
  TEAM          100.00               42            0.08              0.10        192.57                57.21         0.579          pass              0.940             94.0                           0.631                7.18              0.663                                 ok           False                  False
   XEL           88.89                9            0.91              0.44         69.37                16.48         0.555          pass              0.332             13.1                           0.237               -7.86             -0.772 downtrend_blocked_slope_and_streak           False                  False
   KHC           95.00               20            0.44              0.07         23.83                23.05         0.545          pass              0.698             58.8                           0.552               -2.60             -0.323            downtrend_blocked_slope           False                  False
   WBD           93.48               46            0.02              0.00         30.84                38.24         0.533          pass              0.888             91.7                           0.756                9.34              1.161                                 ok           False                  False
  NVDA           90.91               33            0.32              0.50        224.37                44.14         0.524          pass              0.649             50.9                           0.344                2.56              0.664                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-25T10:35:06.003979-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:30:06.584523-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:25:05.951093-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:20:05.036960-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:15:03.948523-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:10:05.955817-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:05:04.806529-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.74, "early_entry_score": 0.835, "early_reclaim_pct": 86.3, "entry_ask": 3.2, "entry_bid": 2.5, "entry_mode": "early", "entry_option_price": 2.85, "hypothetical_budget": 36776.65, "hypothetical_contracts": 129, "matched_signals": 30, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 3441.0, "option_spread_pct": 24.56, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.569, "shadow_only": true, "success_rate": 96.67, "ticker": "FAST", "timing_score": 0.43, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.835, "early_reclaim_pct": 86.3, "matched_signals": 30, "recovery_stability_score": 0.569, "success_rate": 96.67, "ticker": "FAST", "timing_score": 0.43, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-25T10:00:06.218962-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T09:55:06.037252-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"asset_type": "option", "contract_symbol": "SOXL261030C00145000", "fill_price": 23.775, "pnl": 5600.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 17.26, "ticker": "SOXL"}
2026-09-25T00:00:05.872425-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 92, 'empty': 1}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260925103506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260925103506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260925103506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260925103506)

</details>
