# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-05 10:10:06 EDT`
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

- Cash: `$88,586.80`
- Equity: `$88,586.80`
- Realized PnL: `$78,586.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-05)

```text
ticker asset_type execution_mode        instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
    ZS     option         option ZS261120C00200000     27          2026-10-02         2026-10-05        14.85      17.525 7222.5   18.013468 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           82.76               29            2.71              3.10        162.38               114.85         0.688          pass              0.333             21.3                           0.268               12.30              0.925                                 ok            True                  False
   TRI           87.88               33            0.95              0.65         97.34                53.36         0.537          pass              0.563             48.6                           0.398                1.32              0.078                                 ok            True                  False
  AMAT           84.62               39            1.01              3.81        538.41                49.71         0.512          pass              0.410             14.2                           0.121               15.15              1.613                                 ok            True                  False
  MRVL           83.33               36            0.80              1.52        271.64                54.74         0.511          pass              0.468             51.7                           0.438                4.95              0.470                                 ok            True                  False
   ADI           84.21               19            1.75              5.12        414.95                32.86         0.510          pass              0.223              0.0                           0.150                7.01              0.759                                 ok            True                  False
    MU           90.91               33            0.96              7.20       1071.80                50.82         0.509          pass              0.636             46.8                           0.531                1.98              0.041                                 ok            True                  False
  DRAM           80.56               36            0.13              0.06         61.76                54.09         0.585          pass              0.487             80.0                           0.624                0.19             -0.112                                 ok           False                  False
  AMGN           85.29               34            0.41              1.15        402.55                47.11         0.552          pass              0.575             72.7                           0.643                2.10              0.125                                 ok           False                  False
  ASML           76.92               26            1.14             14.95       1860.90                42.39         0.549          pass              0.256             31.6                           0.272                7.87              0.820                                 ok           False                  False
  QCOM           89.29               28            1.20              1.55        184.21                56.36         0.543          pass              0.571             49.6                           0.380               -5.96             -0.934 downtrend_blocked_slope_and_streak           False                  False
  INTC           83.87               31            2.16              1.81        118.56                74.20         0.540          pass              0.462             54.8                           0.518               -4.13             -0.545            downtrend_blocked_slope           False                  False
  LRCX           78.79               33            1.53              3.72        345.90                57.64         0.515          pass              0.230              8.3                           0.133               13.32              1.400                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-10-05T10:10:06.753289-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.76, "early_entry_score": 0.842, "early_reclaim_pct": 86.0, "entry_ask": 2.55, "entry_bid": 2.2, "entry_mode": "early", "entry_option_price": 2.375, "hypothetical_budget": 44293.4, "hypothetical_contracts": 186, "matched_signals": 32, "option_liquidity_status": "wide_spread", "option_open_interest": 3445.0, "option_spread_pct": 14.74, "option_volume": 62.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.709, "shadow_only": true, "success_rate": 96.88, "ticker": "FAST", "timing_score": 0.378, "top_candidates": [{"current_drop_pct": 0.76, "early_entry_score": 0.842, "early_reclaim_pct": 86.0, "matched_signals": 32, "recovery_stability_score": 0.709, "success_rate": 96.88, "ticker": "FAST", "timing_score": 0.378, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-05T10:05:01.984758-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-05T10:00:05.004899-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-05T09:55:04.847980-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"asset_type": "option", "contract_symbol": "ZS261120C00200000", "fill_price": 17.525, "pnl": 7222.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.01, "ticker": "ZS"}
2026-10-05T03:00:05.114767-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {'saved': 92, 'empty': 1}
2026-10-03T02:55:05.889514-04:00   share_ext_0255      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:50:05.063422-04:00   share_ext_0250      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:45:04.071042-04:00   share_ext_0245      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:40:05.983879-04:00   share_ext_0240      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:35:05.098506-04:00   share_ext_0235      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261005101006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261005101006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261005101006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261005101006)

</details>
