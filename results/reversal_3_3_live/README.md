# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-18 10:35:06 EDT`
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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-18)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   WMT     option         option WMT261023C00108000    127          2026-09-17         2026-09-18        2.565        3.05 6159.5   18.908382 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           96.88               32            1.69              2.34        196.47                82.85         0.614          pass              0.700             30.7                           0.450                9.18              1.833                                 ok            True                  False
  MRVL           80.00               40            0.64              1.07        240.30                74.50         0.590          pass              0.399             46.7                           0.261               14.56              0.800                                 ok            True                  False
  CTSH          100.00               17            2.33              1.01         61.45                39.55         0.523          pass              0.533             11.4                           0.293               -6.50             -0.006                                 ok            True                  False
  INTC           84.62               39            0.70              0.53        108.57                60.44         0.518          pass              0.436             22.4                           0.229               17.86              0.927                                 ok            True                  False
  FTNT           80.00               10            3.45              4.16        170.80                57.60         0.500          pass              0.050              0.0                           0.170                6.57              1.117                                 ok            True                  False
  CRWD           63.64               11            3.73              6.41        242.95                97.92         0.617          pass              0.114             15.2                           0.338               10.03              1.721                                 ok           False                  False
  PYPL           91.43               35            0.33              0.12         52.89                57.74         0.616          pass              0.757             74.6                           0.679               -6.91             -0.417            downtrend_blocked_slope           False                  False
  NVDA           92.50               40            0.03              0.04        219.32                45.58         0.571          pass              0.877             95.4                           0.637               -3.91             -0.624           downtrend_blocked_streak           False                  False
   TRI           90.91               11            3.08              2.14         98.56                55.72         0.565          pass              0.376              7.3                           0.251              -13.73             -0.629 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00               40            0.27              0.37        192.37                58.58         0.564          pass              0.914             85.8                           0.729               -1.37              0.383                                 ok           False                  False
   EXC          100.00                8            1.07              0.32         42.50                15.46         0.561          pass              0.510             18.1                           0.217               -4.36             -0.460 downtrend_blocked_slope_and_streak           False                  False
  ADSK           84.38               32            0.94              1.44        218.02                55.63         0.550          pass              0.379             20.2                           0.263               -8.81             -0.066           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-18T10:35:06.106609-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:30:04.878508-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:25:05.756600-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:20:05.884783-04:00 early_entry_1020 early_entry_shadow {"contract_symbol": "TEAM261023C00190000", "current_drop_pct": 0.5, "early_entry_score": 0.864, "early_reclaim_pct": 73.8, "entry_ask": 16.3, "entry_bid": 13.7, "entry_mode": "early", "entry_option_price": 15.0, "hypothetical_budget": 35735.4, "hypothetical_contracts": 23, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 17.33, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.592, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.562, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.864, "early_reclaim_pct": 73.8, "matched_signals": 38, "recovery_stability_score": 0.592, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.562, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-18T10:15:05.598179-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:10:02.340504-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:10:02.340504-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"asset_type": "option", "contract_symbol": "WMT261023C00108000", "fill_price": 3.05, "pnl": 6159.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.91, "ticker": "WMT"}
2026-09-18T10:05:06.381889-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:00:06.717363-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T00:00:09.864377-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {'saved': 92, 'empty': 1}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260918103506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260918103506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260918103506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260918103506)

</details>
