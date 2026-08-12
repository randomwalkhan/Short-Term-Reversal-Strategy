# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-12 10:00:04 EDT`
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

- Cash: `$35,098.00`
- Equity: `$35,098.00`
- Realized PnL: `$25,098.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-12)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  LRCX     option         option LRCX260918C00310000      5          2026-08-10         2026-08-12        26.85        34.9 4025.0   29.981378 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           83.78               37            0.81              0.87        153.71               126.50         0.795          pass              0.574             71.2                           0.426               46.56              5.190                  ok            True                  False
  PYPL           90.00               20            1.19              0.49         58.79                59.96         0.690          pass              0.546             47.8                           0.385               -0.09              0.206                  ok            True                  False
  SHOP           97.06               34            1.21              1.29        152.06                81.89         0.656          pass              0.713             29.2                           0.263               16.72              2.911                  ok            True                  False
  ABNB          100.00               13            2.05              2.66        183.84                64.05         0.645          pass              0.577             30.7                           0.267               18.41              2.279                  ok            True                  False
 CMCSA           88.24               17            1.15              0.21         25.56                42.38         0.625          pass              0.413             28.0                           0.271                7.12              0.688                  ok            True                  False
   ROP          100.00               12            2.12              5.94        396.95                44.32         0.616          pass              0.515             13.5                           0.181                0.45              0.157                  ok            True                  False
  GEHC           95.24               21            1.76              0.90         72.37                54.33         0.610          pass              0.614             26.4                           0.246               -0.60              0.303                  ok            True                  False
  TMUS           88.24               34            0.60              0.76        178.27                55.82         0.607          pass              0.537             32.1                           0.273                2.41              0.272                  ok            True                  False
  ISRG           85.29               34            0.78              2.18        400.30                69.94         0.603          pass              0.432             23.4                           0.145               12.79              1.317                  ok            True                  False
  DXCM           88.89               36            0.66              0.42         89.35                59.17         0.581          pass              0.698             76.4                           0.591               19.31              1.147                  ok            True                   True
  MDLZ           90.91               22            0.83              0.36         61.63                29.90         0.570          pass              0.549             40.4                           0.397               -2.87             -0.209                  ok            True                  False
   ADP          100.00               17            1.70              3.23        269.71                32.74         0.563          pass              0.512              3.0                           0.179                0.99              0.113                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-08-12T10:00:04.707045-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "REGN260918C00790000", "current_drop_pct": 0.58, "early_entry_score": 0.816, "early_reclaim_pct": 62.7, "entry_ask": 32.7, "entry_bid": 25.0, "entry_mode": "early", "entry_option_price": 28.85, "hypothetical_budget": 17549.0, "hypothetical_contracts": 6, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 45.0, "option_spread_pct": 26.69, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.62, "shadow_only": true, "success_rate": 94.74, "ticker": "REGN", "timing_score": 0.484, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.816, "early_reclaim_pct": 62.7, "matched_signals": 38, "recovery_stability_score": 0.62, "success_rate": 94.74, "ticker": "REGN", "timing_score": 0.484, "trend_health_status": "ok"}, {"current_drop_pct": 0.66, "early_entry_score": 0.698, "early_reclaim_pct": 76.4, "matched_signals": 36, "recovery_stability_score": 0.591, "success_rate": 88.89, "ticker": "DXCM", "timing_score": 0.581, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-12T09:50:02.620693-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"asset_type": "option", "contract_symbol": "LRCX260918C00310000", "fill_price": 34.9, "pnl": 4025.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 29.98, "ticker": "LRCX"}
2026-08-12T09:35:01.769154-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 93}
2026-08-12T09:30:01.771593-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 93}
2026-08-12T09:25:01.593760-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 93}
2026-08-12T09:20:03.729351-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 93}
2026-08-12T09:15:01.696450-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 93}
2026-08-12T09:10:04.748220-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 93}
2026-08-12T09:05:02.776077-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 93}
2026-08-12T09:00:03.695691-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260812100004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260812100004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260812100004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260812100004)

</details>
