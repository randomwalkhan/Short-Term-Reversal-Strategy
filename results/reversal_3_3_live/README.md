# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-24 10:35:04 EDT`
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

- Cash: `$34,043.00`
- Equity: `$34,043.00`
- Realized PnL: `$24,043.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00320000     13          2026-07-23         2026-07-24       11.225      13.675 3185.0   21.826281 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           84.00               25            0.93              0.36         55.84                61.86         0.659          pass              0.469             65.3                           0.455               19.78              1.852                                 ok            True                  False
   HON           85.00               20            1.07              1.84        245.48                40.09         0.553          pass              0.409             51.1                           0.396                7.61              0.886                                 ok            True                  False
  ASML           91.30               23            2.23             28.12       1790.95                56.08         0.548          pass              0.475             10.7                           0.196               -1.92              0.073                                 ok            True                  False
   STX           88.24               17            4.96             31.72        899.77               102.76         0.538          pass              0.329              2.9                           0.131               -4.65              0.292                                 ok            True                  False
  KLAC           82.61               23            3.15              4.82        216.66                98.03         0.632          pass              0.244              8.3                           0.216               -8.50             -0.761 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           96.77               31            0.00              0.00         60.05                31.80         0.577          pass              0.898            100.0                           0.570                2.07              0.217                                 ok           False                  False
  LRCX           80.00               20            3.45              7.72        316.47                88.87         0.565          pass              0.139              5.4                           0.234              -11.87             -1.023 downtrend_blocked_slope_and_streak           False                  False
  AMAT           86.67               15            3.86             15.22        556.28                96.41         0.563          pass              0.277              3.2                           0.235              -10.20             -0.874 downtrend_blocked_slope_and_streak           False                  False
  META           86.96               46            0.03              0.11        606.05                54.86         0.551          pass              0.734             97.9                           0.806               -9.45             -1.015 downtrend_blocked_slope_and_streak           False                  False
  PANW           95.83               48            0.02              0.04        325.61                61.92         0.542          pass              0.944             96.8                           0.465               -0.10             -0.272                                 ok           False                  False
  CSCO           89.74               39            0.14              0.11        112.71                38.92         0.541          pass              0.745             79.2                           0.440               -7.18             -0.643 downtrend_blocked_slope_and_streak           False                  False
  GILD           94.12               34            0.24              0.22        130.76                35.55         0.538          pass              0.810             73.3                           0.665                0.55             -0.024                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                   detail
2026-07-24T10:35:04.435807-04:00 early_entry_1035 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:30:02.438509-04:00 early_entry_1030 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:25:03.433473-04:00 early_entry_1025 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:20:04.356287-04:00 early_entry_1020 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:15:02.377890-04:00 early_entry_1015 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:10:05.990333-04:00 early_entry_1010 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:05:02.385595-04:00 early_entry_1005 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:00:02.441453-04:00 early_entry_1000 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T09:50:06.179967-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "AAPL260821C00320000", "fill_price": 13.675, "pnl": 3185.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 21.83, "ticker": "AAPL"}
2026-07-24T00:00:02.342132-04:00     data_refresh       data_refresh                                                                                                                                                                            {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260724103504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260724103504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260724103504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260724103504)

</details>
