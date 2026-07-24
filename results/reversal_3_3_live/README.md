# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-24 10:25:03 EDT`
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
  PYPL           80.95               21            1.13              0.44         55.81                61.86         0.668          pass              0.340             58.0                           0.338               19.54              1.843                                 ok            True                  False
   STX           89.47               19            3.87             24.77        902.74               102.76         0.602          pass              0.445             24.2                           0.254               -3.56              0.344                                 ok            True                  False
  GILD           92.59               27            0.50              0.46        130.66                35.55         0.566          pass              0.640             44.8                           0.400                0.28             -0.036                                 ok            True                  False
  ASML           92.31               26            1.83             23.04       1793.12                56.08         0.556          pass              0.571             26.8                           0.363               -1.52              0.092                                 ok            True                  False
  KLAC           84.00               25            2.30              3.51        217.22                98.03         0.685          pass              0.305             10.0                           0.164               -7.69             -0.721 downtrend_blocked_slope_and_streak           False                  False
  AMAT           88.89               18            3.09             12.17        557.59                96.41         0.608          pass              0.368              5.5                           0.181               -9.47             -0.837 downtrend_blocked_slope_and_streak           False                  False
  LRCX           84.00               25            2.49              5.56        317.40                88.87         0.606          pass              0.346             26.3                           0.305              -10.99             -0.978 downtrend_blocked_slope_and_streak           False                  False
   WDC           94.12               17            5.41             21.15        549.24               114.14         0.550          pass              0.504              8.6                           0.167               -9.35             -0.303            downtrend_blocked_slope           False                  False
  META           86.96               46            0.11              0.45        605.91                54.86         0.545          pass              0.714             91.4                           0.684               -9.53             -1.019 downtrend_blocked_slope_and_streak           False                  False
  CSCO           90.00               40            0.07              0.05        112.74                38.92         0.540          pass              0.791             90.2                           0.531               -7.11             -0.640 downtrend_blocked_slope_and_streak           False                  False
  CRWD           91.30               46            0.17              0.22        183.32                61.02         0.538          pass              0.793             79.2                           0.498               -2.18             -0.660 downtrend_blocked_slope_and_streak           False                  False
   APP           77.78               36            2.08              5.80        396.38                79.31         0.522          pass              0.303             25.7                           0.329              -22.96             -1.917            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                   detail
2026-07-24T10:25:03.433473-04:00 early_entry_1025 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:20:04.356287-04:00 early_entry_1020 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:15:02.377890-04:00 early_entry_1015 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:10:05.990333-04:00 early_entry_1010 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:05:02.385595-04:00 early_entry_1005 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:00:02.441453-04:00 early_entry_1000 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T09:50:06.179967-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "AAPL260821C00320000", "fill_price": 13.675, "pnl": 3185.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 21.83, "ticker": "AAPL"}
2026-07-24T00:00:02.342132-04:00     data_refresh       data_refresh                                                                                                                                                                            {'saved': 93}
2026-07-23T15:10:05.971667-04:00       entry_1500       slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-07-23T15:05:04.134167-04:00       entry_1500       slot_skipped                                                                                                                                                          {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260724102503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260724102503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260724102503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260724102503)

</details>
