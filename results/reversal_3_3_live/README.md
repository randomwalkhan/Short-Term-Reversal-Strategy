# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-02 11:50:03 EST`
Last processed slot: `manage_1200`

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

- Cash: `$126,926.55`
- Equity: `$126,926.55`
- Realized PnL: `$116,926.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-02)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261218C00260000     30          2026-10-30         2026-11-02         19.4       22.65 9750.0   16.752577 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  GILD           91.67               24            0.97              1.16        170.18                29.81         0.502            pass              0.639             61.4                           0.778               10.42              1.012                                 ok            True                  False
  SOXL           73.33               30            1.80              0.97         76.63               161.32         0.769            pass              0.279             22.9                           0.213              -23.30             -1.426            downtrend_blocked_slope           False                  False
  INTC           58.33               12            4.70              2.16         64.83               126.81         0.699            pass              0.099              5.2                           0.217              -31.90             -2.711            downtrend_blocked_slope           False                  False
  ALNY           76.19               21            2.43              2.81        163.80               108.44         0.643            pass              0.304             55.4                           0.748              -30.99             -3.556            downtrend_blocked_slope           False                  False
  FTNT           75.00                4            4.03              3.84        134.43                91.18         0.634            pass              0.112             16.3                           0.441              -23.85             -2.643 downtrend_blocked_slope_and_streak           False                  False
  CSCO           70.59               17            1.33              0.97        104.09                35.63         0.530            pass              0.131             10.3                           0.104               -3.17             -0.057           downtrend_blocked_streak           False                  False
  TEAM          100.00               39            0.56              0.76        191.40                55.13         0.512            pass              0.881             78.9                           0.853              -11.23             -1.390            downtrend_blocked_slope           False                  False
  AAPL           88.89                9            1.59              3.84        342.99                14.54         0.510            pass              0.301              4.4                           0.198               -1.10              0.018                                 ok           False                  False
  LRCX           67.74               31            1.71              2.86        237.89                61.33         0.504            pass              0.235             14.8                           0.214              -13.66             -0.868 downtrend_blocked_slope_and_streak           False                  False
  META           80.56               36            0.43              1.84        614.20                38.01         0.502            pass              0.380             47.3                           0.380              -13.19             -1.523 downtrend_blocked_slope_and_streak           False                  False
   CSX           82.76               29            0.64              0.23         51.89                27.38         0.499 below_threshold              0.347             32.3                           0.311                7.88              0.874                                 ok           False                  False
    MU           77.27               22            2.62             16.21        877.79                60.34         0.498 below_threshold              0.154              7.9                           0.179               -4.79              0.094                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-11-02T11:50:03.622445-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:45:06.353234-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:40:04.764399-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:35:05.778212-05:00 early_entry_1135 early_entry_shadow {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.63, "early_entry_score": 0.813, "early_reclaim_pct": 75.5, "entry_ask": 3.0, "entry_bid": 2.6, "entry_mode": "early", "entry_option_price": 2.8, "hypothetical_budget": 63463.28, "hypothetical_contracts": 226, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1017.0, "option_spread_pct": 14.29, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.589, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.813, "early_reclaim_pct": 75.5, "matched_signals": 41, "recovery_stability_score": 0.589, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T11:30:05.925389-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:25:05.711228-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:20:05.561484-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:15:06.056353-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:10:06.789885-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:05:06.412913-05:00 early_entry_1105 early_entry_shadow              {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.6, "early_entry_score": 0.818, "early_reclaim_pct": 76.9, "entry_ask": 3.0, "entry_bid": 2.75, "entry_mode": "early", "entry_option_price": 2.875, "hypothetical_budget": 63463.28, "hypothetical_contracts": 220, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 1017.0, "option_spread_pct": 8.7, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.564, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.488, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.818, "early_reclaim_pct": 76.9, "matched_signals": 41, "recovery_stability_score": 0.564, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261102115003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261102115003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261102115003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261102115003)

</details>
