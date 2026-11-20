# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 10:45:05 EST`
Last processed slot: `early_entry_1045`

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
  NXPI           90.91               11            2.61              4.61        249.79                49.35         0.533          pass              0.371              6.8                           0.072               -1.25             -0.385                                 ok            True                  False
  INTC           52.94               17            3.68              1.44         55.10               141.91         0.749          pass              0.235             37.9                           0.227               -4.64             -0.930 downtrend_blocked_slope_and_streak           False                  False
  IDXX           97.78               45            0.02              0.10        689.61                78.44         0.692          pass              0.946             92.2                           0.414                1.99             -0.021                                 ok           False                  False
   APP          100.00                3            6.23             16.53        371.94               122.37         0.688          pass              0.469              0.0                           0.157               -9.16             -0.732 downtrend_blocked_slope_and_streak           False                  False
  FTNT           57.14               14            2.91              2.67        130.31                96.17         0.666          pass              0.104              3.5                           0.087                7.40              0.661                                 ok           False                  False
   BKR           66.67               12            2.27              0.74         46.35                56.86         0.577          pass              0.117             15.4                           0.120               -4.27             -0.434 downtrend_blocked_slope_and_streak           False                  False
  QCOM           85.00               20            2.35              2.66        160.87                69.46         0.571          pass              0.310             17.8                           0.141               -4.35             -0.784 downtrend_blocked_slope_and_streak           False                  False
  CSCO           70.59               17            1.63              1.08         94.24                50.60         0.557          pass              0.150             15.9                           0.118               -0.74             -0.383                                 ok           False                  False
  UPRO           80.00                5            3.76              3.10        116.56                72.20         0.549          pass              0.055              0.0                           0.150              -12.01             -1.650 downtrend_blocked_slope_and_streak           False                  False
  MCHP           60.00               10            3.85              1.57         57.80                78.21         0.536          pass              0.054              0.0                           0.150               -3.65             -0.515            downtrend_blocked_slope           False                  False
   MAR           92.31               26            0.50              1.44        413.42                25.25         0.517          pass              0.602             38.5                           0.317               -0.91             -0.103                                 ok           False                  False
  DASH           83.67               49            0.04              0.05        157.11                67.24         0.514          pass              0.644             98.3                           0.586              -12.58             -1.462 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-11-20T10:45:05.890117-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:40:06.786688-05:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:35:04.912768-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:30:06.085636-05:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:25:04.965468-05:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:20:06.105218-05:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:20:06.105218-05:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "APP270115C00380000", "fill_price": 33.345, "pnl": -4816.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "APP"}
2026-11-20T10:15:05.923687-05:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:10:04.986532-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:05:06.571641-05:00 early_entry_1005 early_entry_shadow {"contract_symbol": "CEG270115C00250000", "current_drop_pct": 1.4, "early_entry_score": 0.698, "early_reclaim_pct": 63.5, "entry_ask": 17.2, "entry_bid": 15.0, "entry_mode": "early", "entry_option_price": 16.1, "hypothetical_budget": 26390.65, "hypothetical_contracts": 16, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 753.0, "option_spread_pct": 13.66, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.745, "shadow_only": true, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 1.4, "early_entry_score": 0.698, "early_reclaim_pct": 63.5, "matched_signals": 34, "recovery_stability_score": 0.745, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120104505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120104505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120104505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120104505)

</details>
