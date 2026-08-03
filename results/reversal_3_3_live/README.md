# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-03 11:25:05 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$35,229.75`
- Equity: `$35,229.75`
- Realized PnL: `$25,229.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-03)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  PYPL     option         option PYPL260918C00057500     66          2026-07-31         2026-08-03        2.500      3.0550  3663.0        22.2 take_profit_day1_hit_at_scan
   CSX     option         option  CSX260918C00050000     86          2026-07-30         2026-08-03        1.925      1.7325 -1655.5       -10.0        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN          100.00               17            1.29              3.47        383.67                25.80         0.520          pass              0.614             38.5                           0.495                4.40              0.653                                 ok            True                  False
  SOXL           79.41               34            1.83              1.47        114.09               178.56         0.630          pass              0.473             83.4                           0.582              -17.68             -4.165 downtrend_blocked_slope_and_streak           False                  False
  DRAM           76.67               30            1.55              0.55         50.14               111.30         0.607          pass              0.407             71.0                           0.516               -6.54             -1.717 downtrend_blocked_slope_and_streak           False                  False
  AAPL           93.75               16            1.31              2.83        307.70                37.33         0.604          pass              0.502             11.6                           0.205               -6.65             -0.355 downtrend_blocked_slope_and_streak           False                  False
  LRCX           86.21               29            1.05              2.16        292.09                90.68         0.596          pass              0.595             80.9                           0.584               -5.48             -1.333 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           90.91               22            0.43              0.19         62.23                33.81         0.595          pass              0.608             59.1                           0.570                2.94              0.548                                 ok           False                  False
    MU           78.79               33            1.30              7.46        819.83               109.24         0.554          pass              0.448             79.8                           0.566               -6.13             -1.778 downtrend_blocked_slope_and_streak           False                  False
  INTC           85.37               41            0.07              0.04         90.18                83.69         0.552          pass              0.694             98.7                           0.687               -7.13             -1.657 downtrend_blocked_slope_and_streak           False                  False
   CSX           96.77               31            0.34              0.12         50.35                27.78         0.540          pass              0.792             66.0                           0.687                0.24             -0.052                                 ok           False                  False
   EXC           96.15               26            0.43              0.14         45.76                22.49         0.533          pass              0.743             61.0                           0.326               -0.73             -0.119                                 ok           False                  False
  MNST           75.00                8            2.01              1.36         95.80                24.15         0.533          pass              0.083              9.8                           0.316               -1.06              0.191                                 ok           False                  False
   PEP           87.88               33            0.15              0.15        139.50                26.18         0.532          pass              0.604             62.5                           0.494                2.87              0.492                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-08-03T11:25:05.765544-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:20:03.871415-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:15:01.863770-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:10:01.942425-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:05:04.817699-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:00:04.955349-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:55:01.983630-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:50:01.989461-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:45:01.762482-04:00 early_entry_1045 early_entry_shadow {"contract_symbol": "CSCO260918C00120000", "current_drop_pct": 0.53, "early_entry_score": 0.678, "early_reclaim_pct": 73.7, "entry_ask": 6.05, "entry_bid": 5.8, "entry_mode": "early", "entry_option_price": 5.925, "hypothetical_budget": 17614.88, "hypothetical_contracts": 29, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 9412.0, "option_spread_pct": 4.22, "option_volume": 63.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.746, "shadow_only": true, "success_rate": 88.89, "ticker": "CSCO", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.678, "early_reclaim_pct": 73.7, "matched_signals": 36, "recovery_stability_score": 0.746, "success_rate": 88.89, "ticker": "CSCO", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-03T10:40:04.670427-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260803112505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260803112505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260803112505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260803112505)

</details>
