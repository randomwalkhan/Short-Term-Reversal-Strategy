# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-24 10:15:01 EDT`
Last processed slot: `early_entry_1015`

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
  ALNY           80.00               20            2.08              3.44        234.74               131.78         0.807          pass              0.254             35.5                           0.320                6.60              0.714                                 ok            True                  False
  REGN          100.00               21            1.13              6.59        831.22                30.64         0.548          pass              0.528              0.0                           0.166                2.17              0.454                                 ok            True                  False
  ASML           83.33               24            1.80             22.23       1754.23                48.84         0.545          pass              0.284             15.9                           0.121               -0.09             -0.286                                 ok            True                  False
  TEAM           85.37               41            0.08              0.09        171.77               117.34         0.786          pass              0.708             95.3                           0.681               13.04              1.371                                 ok           False                  False
  INSM           83.78               37            1.07              0.94        125.37               110.84         0.764          pass              0.518             53.6                           0.636               -7.66             -0.611 downtrend_blocked_slope_and_streak           False                  False
   APP           67.57               37            1.61              3.44        304.29                90.15         0.626          pass              0.362             39.8                           0.394              -11.25             -0.683            downtrend_blocked_slope           False                  False
  AMAT           90.91               22            2.96             10.19        487.95                82.60         0.622          pass              0.499             21.9                           0.341               -8.40             -1.024            downtrend_blocked_slope           False                  False
  GEHC           97.56               41            0.21              0.11         74.77                48.71         0.580          pass              0.844             61.9                           0.434                2.36              0.281                                 ok           False                  False
  UPRO           84.00               25            1.09              1.14        149.39                39.04         0.580          pass              0.327             20.8                           0.257               -4.34             -0.495            downtrend_blocked_slope           False                  False
  DXCM           89.74               39            0.38              0.25         92.23                49.72         0.557          pass              0.680             57.1                           0.401                4.95              0.281                                 ok           False                  False
  CSCO           81.48               27            1.29              1.00        110.61                42.43         0.555          pass              0.261             17.5                           0.198              -10.58             -1.186            downtrend_blocked_slope           False                  False
  MCHP           83.33               24            3.22              1.70         74.89                69.56         0.553          pass              0.269             10.6                           0.183              -10.07             -0.865            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                   detail
2026-08-24T10:15:01.389030-04:00 early_entry_1015 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:10:01.316901-04:00 early_entry_1010 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:05:05.120136-04:00 early_entry_1005 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:00:02.345614-04:00 early_entry_1000 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T09:20:01.323688-04:00     data_refresh       data_refresh                                                                                                                                                                            {'saved': 93}
2026-08-21T12:00:13.505037-04:00 early_entry_1200 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T11:55:10.146119-04:00 early_entry_1155 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T11:50:07.256034-04:00 early_entry_1150 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T11:50:07.256034-04:00      manage_1200               exit {"asset_type": "option", "contract_symbol": "ABNB261016C00180000", "fill_price": 14.125, "pnl": 4565.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 17.22, "ticker": "ABNB"}
2026-08-21T11:15:05.200635-04:00 early_entry_1115 early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260824101501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260824101501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260824101501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260824101501)

</details>
