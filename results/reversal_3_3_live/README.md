# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-24 09:50:01 EDT`
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

- Cash: `$57,703.00`
- Equity: `$57,703.00`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ALNY           84.62               26            1.59              2.62        235.10               131.78         0.814          pass              0.388             25.6                           0.257                7.14              0.737                                 ok            True                  False
  LRCX           80.95               21            3.64              7.99        310.57                88.60         0.575          pass              0.245             29.6                           0.395               -1.25             -0.341                                 ok            True                  False
  ASML           85.19               27            1.50             18.48       1755.84                48.84         0.546          pass              0.396             30.1                           0.238                0.22             -0.272                                 ok            True                  False
   CEG           80.00               30            0.74              1.41        272.28                35.55         0.503          pass              0.304             40.0                           0.321                0.32             -0.182                                 ok            True                  False
  TEAM           84.21               38            0.24              0.29        171.69               117.34         0.791          pass              0.634             85.2                           0.644               12.86              1.364                                 ok           False                  False
  INSM           80.95               21            2.11              1.86        124.97               110.84         0.788          pass              0.188              3.6                           0.092               -8.64             -0.659 downtrend_blocked_slope_and_streak           False                  False
  AMAT           90.48               21            3.02             10.42        487.85                82.60         0.626          pass              0.462             15.4                           0.251               -8.46             -1.027            downtrend_blocked_slope           False                  False
   APP           66.67               36            2.02              4.32        303.92                90.15         0.607          pass              0.307             24.5                           0.323              -11.62             -0.702            downtrend_blocked_slope           False                  False
  UPRO           84.00               25            1.06              1.11        149.40                39.04         0.582          pass              0.333             22.6                           0.207               -4.32             -0.494            downtrend_blocked_slope           False                  False
  CSCO           76.19               21            1.54              1.20        110.53                42.43         0.572          pass              0.130              0.0                           0.218              -10.80             -1.197            downtrend_blocked_slope           False                  False
  MCHP           81.82               22            3.35              1.77         74.86                69.56         0.559          pass              0.184              0.0                           0.183              -10.20             -0.871            downtrend_blocked_slope           False                  False
  DXCM           90.48               42            0.12              0.08         92.31                49.72         0.554          pass              0.794             86.5                           0.609                5.23              0.293                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-24T09:20:01.323688-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-08-21T12:00:13.505037-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T11:55:10.146119-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T11:50:07.256034-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T11:50:07.256034-04:00      manage_1200               exit                                                                                                                                                                                                                                              {"asset_type": "option", "contract_symbol": "ABNB261016C00180000", "fill_price": 14.125, "pnl": 4565.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 17.22, "ticker": "ABNB"}
2026-08-21T11:15:05.200635-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T10:36:48.615754-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T10:18:45.233650-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T00:00:05.323227-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-08-20T14:55:07.817083-04:00       entry_1500              entry {"allocated_cash": 26510.0, "asset_type": "option", "contract_symbol": "ABNB261016C00180000", "contracts": 22, "early_entry_score": 0.826, "entry_mode": "regular", "entry_option_price": 12.05, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 783.0, "option_spread_pct": 5.81, "option_volume": 31.0, "success_rate": 93.94, "ticker": "ABNB", "timing_score": 0.625}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260824095001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260824095001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260824095001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260824095001)

</details>
