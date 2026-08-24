# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-24 09:30:03 EDT`
Last processed slot: `manage_0930`

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
  TEAM           83.78               37            0.76              0.91        171.42               117.34         0.774          pass              0.502             48.0                           0.341               12.27              1.340                                 ok            True                  False
  WDAY           80.00               35            0.60              0.85        199.65                82.42         0.641          pass              0.445             71.4                           0.340                7.93              0.918                                 ok            True                  False
  LRCX           84.00               25            2.79              6.12        311.38                88.60         0.623          pass              0.330             20.2                           0.335               -0.38             -0.301                                 ok            True                  False
   WDC           85.71               21            4.54             14.61        453.18               100.71         0.561          pass              0.290              2.7                           0.206                0.05              0.146                                 ok            True                  False
    MU           82.61               23            4.42             29.88        953.97                97.17         0.559          pass              0.298             28.5                           0.327                7.33              0.840                                 ok            True                  False
  ALNY           88.10               42            0.17              0.27        236.10               131.78         0.821          pass              0.702             68.0                           0.433                8.69              0.802                                 ok           False                  False
  INSM           85.37               41            0.59              0.52        125.55               110.84         0.783          pass              0.421              0.0                           0.244               -7.21             -0.589 downtrend_blocked_slope_and_streak           False                  False
   APP           71.11               45            0.35              0.76        305.45                90.15         0.675          pass              0.450             60.9                           0.572              -10.12             -0.626            downtrend_blocked_slope           False                  False
  AMAT           88.89               27            2.25              7.77        488.99                82.60         0.635          pass              0.513             33.0                           0.479               -7.73             -0.991            downtrend_blocked_slope           False                  False
  SHOP           93.94               33            1.32              1.38        148.66                80.43         0.632          pass              0.724             45.4                           0.370               -5.09             -0.567            downtrend_blocked_slope           False                  False
  MCHP           86.84               38            1.10              0.58         75.37                69.56         0.614          pass              0.575             48.3                           0.380               -8.11             -0.766            downtrend_blocked_slope           False                  False
  GEHC           97.62               42            0.00              0.00         74.82                48.71         0.590          pass              0.959            100.0                           0.539                2.58              0.291                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260824093003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260824093003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260824093003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260824093003)

</details>
