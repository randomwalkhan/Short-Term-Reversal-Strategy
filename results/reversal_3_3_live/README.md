# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-18 10:20:05 EDT`
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
    ZS           96.88               32            1.70              2.35        196.46                82.85         0.613          pass              0.699             30.3                           0.303                9.17              1.832                                 ok            True                  False
  MRVL           80.00               40            0.73              1.23        240.23                74.50         0.584          pass              0.374             38.7                           0.253               14.45              0.795                                 ok            True                  False
  TEAM          100.00               38            0.50              0.68        192.24                58.58         0.562          pass              0.864             73.8                           0.592               -1.60              0.373                                 ok            True                   True
  CTSH          100.00               25            1.63              0.71         61.58                39.55         0.515          pass              0.665             37.8                           0.421               -5.83              0.026                                 ok            True                  False
  INTC           82.93               41            0.56              0.43        108.62                60.44         0.512          pass              0.442             37.4                           0.258               18.02              0.933                                 ok            True                  False
  FTNT           81.82               11            3.22              3.89        170.91                57.60         0.511          pass              0.120              4.5                           0.115                6.82              1.127                                 ok            True                  False
  PYPL           91.67               36            0.26              0.09         52.90                57.74         0.615          pass              0.787             80.4                           0.757               -6.84             -0.414            downtrend_blocked_slope           False                  False
  CRWD           66.67                9            4.22              7.26        242.59                97.92         0.606          pass              0.073              4.0                           0.089                9.47              1.698                                 ok           False                  False
   TRI           91.67               12            2.55              1.78         98.72                55.72         0.590          pass              0.453             23.0                           0.404              -13.26             -0.604 downtrend_blocked_slope_and_streak           False                  False
   EXC          100.00                6            1.20              0.36         42.49                15.46         0.565          pass              0.481              8.2                           0.122               -4.49             -0.466 downtrend_blocked_slope_and_streak           False                  False
  SNPS           85.71               49            0.04              0.12        381.12                63.09         0.558          pass              0.644             78.6                           0.358               -8.48             -0.777            downtrend_blocked_slope           False                  False
  ADSK           85.71               35            0.66              1.01        218.21                55.63         0.551          pass              0.506             44.0                           0.368               -8.56             -0.053           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-18T10:20:05.884783-04:00 early_entry_1020 early_entry_shadow {"contract_symbol": "TEAM261023C00190000", "current_drop_pct": 0.5, "early_entry_score": 0.864, "early_reclaim_pct": 73.8, "entry_ask": 16.3, "entry_bid": 13.7, "entry_mode": "early", "entry_option_price": 15.0, "hypothetical_budget": 35735.4, "hypothetical_contracts": 23, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 17.33, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.592, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.562, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.864, "early_reclaim_pct": 73.8, "matched_signals": 38, "recovery_stability_score": 0.592, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.562, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-18T10:15:05.598179-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:10:02.340504-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:10:02.340504-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"asset_type": "option", "contract_symbol": "WMT261023C00108000", "fill_price": 3.05, "pnl": 6159.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.91, "ticker": "WMT"}
2026-09-18T10:05:06.381889-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:00:06.717363-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T00:00:09.864377-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {'saved': 92, 'empty': 1}
2026-09-17T15:10:01.182099-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-09-17T15:05:01.143983-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-09-17T15:00:04.868136-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260918102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260918102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260918102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260918102005)

</details>
