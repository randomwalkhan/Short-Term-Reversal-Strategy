# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-24 10:40:02 EDT`
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
  PYPL           84.00               25            0.93              0.36         55.84                61.86         0.659          pass              0.469             65.3                           0.493               19.78              1.852                                 ok            True                  False
   HON           85.71               21            1.01              1.74        245.52                40.09         0.551          pass              0.442             53.7                           0.365                7.67              0.888                                 ok            True                  False
  ASML           95.24               21            2.48             31.27       1789.60                56.08         0.549          pass              0.530              0.7                           0.108               -2.17              0.061                                 ok            True                  False
   STX           88.24               17            5.20             33.22        899.12               102.76         0.518          pass              0.330              3.9                           0.203               -4.88              0.281                                 ok            True                  False
  KLAC           83.33               18            3.75              5.74        216.27                98.03         0.621          pass              0.210              1.9                           0.088               -9.06             -0.789 downtrend_blocked_slope_and_streak           False                  False
  PANW           95.65               46            0.10              0.22        325.54                61.92         0.550          pass              0.905             83.2                           0.429               -0.18             -0.275                                 ok           False                  False
  META           86.96               46            0.16              0.66        605.82                54.86         0.541          pass              0.702             87.4                           0.776               -9.57             -1.021 downtrend_blocked_slope_and_streak           False                  False
  CSCO           89.19               37            0.35              0.28        112.64                38.92         0.539          pass              0.623             48.0                           0.287               -7.38             -0.653 downtrend_blocked_slope_and_streak           False                  False
  GILD           94.44               36            0.18              0.16        130.79                35.55         0.530          pass              0.852             80.3                           0.737                0.61             -0.021                                 ok           False                  False
  LRCX           77.78               18            4.08              9.14        315.86                88.87         0.525          pass              0.111              1.7                           0.099              -12.45             -1.053 downtrend_blocked_slope_and_streak           False                  False
  CRWD           90.91               44            0.59              0.75        183.10                61.02         0.522          pass              0.634             30.2                           0.243               -2.58             -0.679 downtrend_blocked_slope_and_streak           False                  False
  AMAT           84.62               13            4.52             17.83        555.16                96.41         0.521          pass              0.198              0.8                           0.201              -10.82             -0.905 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                   detail
2026-07-24T10:40:02.342835-04:00 early_entry_1040 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:35:04.435807-04:00 early_entry_1035 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:30:02.438509-04:00 early_entry_1030 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:25:03.433473-04:00 early_entry_1025 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:20:04.356287-04:00 early_entry_1020 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:15:02.377890-04:00 early_entry_1015 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:10:05.990333-04:00 early_entry_1010 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:05:02.385595-04:00 early_entry_1005 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:00:02.441453-04:00 early_entry_1000 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T09:50:06.179967-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "AAPL260821C00320000", "fill_price": 13.675, "pnl": 3185.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 21.83, "ticker": "AAPL"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260724104002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260724104002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260724104002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260724104002)

</details>
