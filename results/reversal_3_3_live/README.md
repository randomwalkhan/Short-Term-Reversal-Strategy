# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 10:30:06 EST`
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

- Cash: `$96,129.80`
- Equity: `$96,129.80`
- Realized PnL: `$86,129.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00380000     13          2026-11-19         2026-11-20        37.05      33.345 -4816.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           86.67               15            2.25              3.97        250.06                49.35         0.528          pass              0.285              7.1                           0.100               -0.88             -0.368                                 ok            True                  False
   MAR           92.00               25            0.52              1.50        413.40                25.25         0.522          pass              0.580             35.8                           0.228               -0.93             -0.104                                 ok            True                  False
  INTC           60.00               25            2.61              1.02         55.28               141.91         0.770          pass              0.345             55.9                           0.358               -3.58             -0.880 downtrend_blocked_slope_and_streak           False                  False
   APP          100.00                3            5.48             14.53        372.79               122.37         0.732          pass              0.473              0.0                           0.150               -8.42             -0.696 downtrend_blocked_slope_and_streak           False                  False
  IDXX           97.78               45            0.01              0.04        689.63                78.44         0.693          pass              0.960             96.8                           0.525                2.01             -0.020                                 ok           False                  False
  FTNT           70.00               20            2.37              2.18        130.53                96.17         0.677          pass              0.199             21.5                           0.211                8.00              0.687                                 ok           False                  False
   BKR           71.43               14            1.78              0.58         46.42                56.86         0.601          pass              0.188             33.8                           0.243               -3.78             -0.412 downtrend_blocked_slope_and_streak           False                  False
  UPRO           90.00               10            2.72              2.25        116.93                72.20         0.596          pass              0.401             24.8                           0.209              -11.06             -1.602 downtrend_blocked_slope_and_streak           False                  False
  MCHP           80.95               21            2.51              1.03         58.03                78.21         0.584          pass              0.205             16.0                           0.252               -2.31             -0.453            downtrend_blocked_slope           False                  False
  QCOM           84.00               25            1.71              1.94        161.18                69.46         0.579          pass              0.385             40.1                           0.285               -3.73             -0.754 downtrend_blocked_slope_and_streak           False                  False
   TXN          100.00                2            4.27              8.54        282.09                59.73         0.544          pass              0.466              3.9                           0.097               -1.38             -0.401                                 ok           False                  False
  CSCO           73.08               26            0.99              0.65         94.42                50.60         0.544          pass              0.308             48.9                           0.321               -0.09             -0.354                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-11-20T10:30:06.085636-05:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:25:04.965468-05:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:20:06.105218-05:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:20:06.105218-05:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"asset_type": "option", "contract_symbol": "APP270115C00380000", "fill_price": 33.345, "pnl": -4816.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "APP"}
2026-11-20T10:15:05.923687-05:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:10:04.986532-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:05:06.571641-05:00 early_entry_1005 early_entry_shadow   {"contract_symbol": "CEG270115C00250000", "current_drop_pct": 1.4, "early_entry_score": 0.698, "early_reclaim_pct": 63.5, "entry_ask": 17.2, "entry_bid": 15.0, "entry_mode": "early", "entry_option_price": 16.1, "hypothetical_budget": 26390.65, "hypothetical_contracts": 16, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 753.0, "option_spread_pct": 13.66, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.745, "shadow_only": true, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 1.4, "early_entry_score": 0.698, "early_reclaim_pct": 63.5, "matched_signals": 34, "recovery_stability_score": 0.745, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-20T10:00:05.975978-05:00 early_entry_1000 early_entry_shadow {"contract_symbol": "CEG270115C00250000", "current_drop_pct": 1.11, "early_entry_score": 0.722, "early_reclaim_pct": 71.0, "entry_ask": 18.0, "entry_bid": 16.0, "entry_mode": "early", "entry_option_price": 17.0, "hypothetical_budget": 26390.65, "hypothetical_contracts": 15, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 753.0, "option_spread_pct": 11.76, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.696, "shadow_only": true, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.511, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.722, "early_reclaim_pct": 71.0, "matched_signals": 34, "recovery_stability_score": 0.696, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.511, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-20T01:25:03.363046-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T01:20:04.815073-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120103006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120103006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120103006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120103006)

</details>
