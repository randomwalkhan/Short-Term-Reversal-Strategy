# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-14 10:55:04 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$41,228.00`
- Equity: `$41,228.00`
- Realized PnL: `$31,228.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-14)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   BKR     option         option BKR260918C00065000     98          2026-08-13         2026-08-14        1.925        2.25 3185.0   16.883117 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  SOXL           83.78               37            0.82              0.83        145.00               164.53         0.869          pass              0.579             70.2                           0.602               25.67              1.877                  ok            True                  False
  ALNY           80.95               21            1.89              3.00        225.83               128.90         0.840          pass              0.302             39.7                           0.267                8.42              0.482                  ok            True                  False
  TEAM           81.25               32            1.75              2.04        165.11               127.34         0.782          pass              0.338             26.7                           0.306               61.43              5.669                  ok            True                  False
  LRCX           87.50               32            1.26              2.96        335.74                86.66         0.670          pass              0.528             38.2                           0.314               13.57              1.164                  ok            True                  False
  SHOP           93.33               15            3.21              3.56        157.00                83.25         0.658          pass              0.478              7.9                           0.085               30.98              3.022                  ok            True                  False
  MRVL           80.56               36            0.70              1.08        221.72                86.88         0.636          pass              0.436             61.3                           0.602               17.63              1.219                  ok            True                  False
  TMUS           90.91               33            0.67              0.85        183.01                56.42         0.609          pass              0.690             61.5                           0.357                5.47              0.412                  ok            True                  False
   ROP          100.00               20            1.40              3.91        395.83                41.86         0.586          pass              0.632             35.6                           0.495               -0.01              0.100                  ok            True                  False
  FAST          100.00               17            0.93              0.34         51.20                25.38         0.549          pass              0.576             25.0                           0.435                6.60              0.770                  ok            True                  False
  ASML           88.89               36            0.70              9.04       1844.02                47.59         0.542          pass              0.587             40.7                           0.420               12.64              1.264                  ok            True                  False
  AMGN          100.00               18            1.42              4.15        416.06                27.74         0.524          pass              0.563             19.1                           0.181                6.94              0.894                  ok            True                  False
   ADP           95.24               21            1.56              3.02        274.94                31.43         0.517          pass              0.556             10.2                           0.190                2.05              0.172                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-08-14T10:55:04.531949-04:00 early_entry_1055      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-14T10:55:04.531949-04:00      manage_1100                    exit                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "BKR260918C00065000", "fill_price": 2.25, "pnl": 3185.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.88, "ticker": "BKR"}
2026-08-14T00:00:04.633795-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-08-13T15:10:04.909039-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-13T15:05:06.030850-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-13T15:00:02.921317-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-13T14:55:04.897309-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-13", "training_samples": 5661, "window": 5}
2026-08-13T14:55:04.897309-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                              {"early_entry_score": 0.522, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 5317.0, "option_spread_pct": 28.57, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "FAST", "timing_score": 0.586}
2026-08-13T14:55:04.897309-04:00       entry_1500                   entry {"allocated_cash": 18865.0, "asset_type": "option", "contract_symbol": "BKR260918C00065000", "contracts": 98, "early_entry_score": 0.39, "entry_mode": "regular", "entry_option_price": 1.925, "execution_mode": "option", "matched_signals": 19, "option_liquidity_status": "ok", "option_open_interest": 2279.0, "option_spread_pct": 12.99, "option_volume": 49.0, "success_rate": 84.21, "ticker": "BKR", "timing_score": 0.546}
2026-08-13T11:55:02.213370-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260814105504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260814105504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260814105504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260814105504)

</details>
