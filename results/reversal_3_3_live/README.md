# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-06 15:40:01 EDT`
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

- Cash: `$17,608.25`
- Equity: `$34,145.75`
- Realized PnL: `$24,370.75`
- Unrealized PnL: `$-225.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  INTC     option         option INTC260918C00100000       2026-08-06                   0     15     16762.5                 16537.5        11.18          11.02      100.37        100.21          bid_ask_mid                      11.02                bid_ask_mid                    True          -225.0                  -1.34          85.0               40              0.68         79.69           79.08                  86.71               28020.0         1406.0               0.03                      ok
```

## Today's Closed Trades (2026-08-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  PYPL     option         option PYPL260918C00057500     55          2026-08-05         2026-08-06        2.865       3.325 2530.0   16.055846 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ISRG           86.84               38            0.55              1.44        374.58                72.98         0.664          pass              0.558             40.9                           0.282               12.39              1.070                                 ok            True                  False
  AMZN           80.49               41            0.51              0.97        272.24                61.64         0.583          pass              0.307             11.8                           0.174               16.10              2.300                                 ok            True                  False
  WDAY           82.86               35            0.69              0.82        170.28                67.74         0.576          pass              0.554             84.6                           0.835               32.53              2.547                                 ok            True                  False
  INTC           84.62               39            0.85              0.60        100.80                86.71         0.559          pass              0.625             84.3                           0.480               -0.03              0.773                                 ok            True                  False
  MNST           89.47               19            0.85              0.56         94.22                25.70         0.556          pass              0.523             51.5                           0.558                0.11             -0.078                                 ok            True                  False
   MAR           96.88               32            0.63              1.58        360.63                38.12         0.535          pass              0.772             57.4                           0.538               -1.49             -0.684                                 ok            True                  False
   PEP           84.00               25            0.55              0.53        138.55                25.05         0.522          pass              0.419             53.4                           0.398                2.27              0.078                                 ok            True                  False
  UPRO           82.86               35            0.54              0.58        152.99                43.16         0.515          pass              0.414             39.9                           0.278               11.96              1.452                                 ok            True                  False
    MU           80.56               36            0.36              2.26        892.22               111.75         0.684          pass              0.542             95.1                           0.638              -10.12             -0.502           downtrend_blocked_streak           False                  False
  AMAT           91.67               36            0.69              2.58        533.13                86.87         0.661          pass              0.803             84.1                           0.590               -5.73              0.161           downtrend_blocked_streak           False                  False
   ROP           94.74               38            0.06              0.16        394.46                46.42         0.580          pass              0.923             95.2                           0.770               11.03              0.832                                 ok           False                  False
   CSX           90.91               22            0.79              0.28         51.00                29.11         0.556          pass              0.465             12.9                           0.211               -3.97             -0.415 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-08-06T15:10:06.321105-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-08-06T15:05:05.205099-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-08-06T15:00:02.209761-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-08-06T14:55:01.108594-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-08-06T14:50:04.202564-04:00       entry_1500              entry {"allocated_cash": 16762.5, "asset_type": "option", "contract_symbol": "INTC260918C00100000", "contracts": 15, "early_entry_score": 0.652, "entry_mode": "regular", "entry_option_price": 11.175, "execution_mode": "option", "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 28020.0, "option_spread_pct": 3.13, "option_volume": 1406.0, "success_rate": 85.0, "ticker": "INTC", "timing_score": 0.565}
2026-08-06T14:50:04.202564-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-06", "training_samples": 5584, "window": 5}
2026-08-06T12:00:02.173564-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:55:01.207054-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:50:03.918933-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:50:03.918933-04:00      manage_1200               exit                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.325, "pnl": 2530.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.06, "ticker": "PYPL"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260806154001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260806154001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260806154001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260806154001)

</details>
