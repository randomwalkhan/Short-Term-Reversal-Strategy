# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-14 13:28:44 EDT`
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
  TEAM           81.25               32            1.93              2.24        165.02               127.34         0.775          pass              0.316             19.5                           0.272               61.15              5.661                  ok            True                  False
  SOXL           81.25               32            3.52              3.58        143.83               164.53         0.774          pass              0.320             20.8                           0.221               22.25              1.752                  ok            True                  False
  INSM           80.00               20            2.03              1.80        125.56               108.96         0.760          pass              0.256             37.7                           0.706               25.52              3.283                  ok            True                  False
  SHOP           95.24               21            2.56              2.84        157.31                83.25         0.662          pass              0.620             26.7                           0.269               31.86              3.053                  ok            True                  False
  TMUS           90.00               30            0.86              1.11        182.91                56.42         0.614          pass              0.612             50.2                           0.268                5.26              0.403                  ok            True                  False
  MRVL           80.00               35            1.10              1.72        221.44                86.88         0.612          pass              0.383             51.7                           0.367               17.15              1.200                  ok            True                  False
  LRCX           84.00               25            2.90              6.84        334.08                86.66         0.600          pass              0.276              3.1                           0.128               11.68              1.087                  ok            True                  False
  DXCM           80.95               21            1.71              1.09         91.01                54.70         0.599          pass              0.159              0.0                           0.240                7.75              0.822                  ok            True                  False
  INTC           86.11               36            1.65              1.21        104.04                80.36         0.570          pass              0.436             14.4                           0.186               14.00              1.021                  ok            True                  False
   TRI           85.19               27            2.34              1.74        105.33                75.25         0.565          pass              0.414             35.4                           0.387                5.56              0.383                  ok            True                  False
  UPRO           82.76               29            0.83              0.92        157.29                41.59         0.561          pass              0.282              8.7                           0.258               11.47              0.789                  ok            True                  False
  FAST          100.00               20            0.71              0.26         51.23                25.38         0.543          pass              0.650             43.0                           0.400                6.84              0.780                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-08-14T11:37:55.972745-04:00 early_entry_1135      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-14T10:55:04.531949-04:00 early_entry_1055      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-14T10:55:04.531949-04:00      manage_1100                    exit                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "BKR260918C00065000", "fill_price": 2.25, "pnl": 3185.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.88, "ticker": "BKR"}
2026-08-14T00:00:04.633795-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-08-13T15:10:04.909039-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-13T15:05:06.030850-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-13T15:00:02.921317-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-13T14:55:04.897309-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                              {"early_entry_score": 0.522, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 5317.0, "option_spread_pct": 28.57, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "FAST", "timing_score": 0.586}
2026-08-13T14:55:04.897309-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-13", "training_samples": 5661, "window": 5}
2026-08-13T14:55:04.897309-04:00       entry_1500                   entry {"allocated_cash": 18865.0, "asset_type": "option", "contract_symbol": "BKR260918C00065000", "contracts": 98, "early_entry_score": 0.39, "entry_mode": "regular", "entry_option_price": 1.925, "execution_mode": "option", "matched_signals": 19, "option_liquidity_status": "ok", "option_open_interest": 2279.0, "option_spread_pct": 12.99, "option_volume": 49.0, "success_rate": 84.21, "ticker": "BKR", "timing_score": 0.546}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260814132844)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260814132844)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260814132844)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260814132844)

</details>
