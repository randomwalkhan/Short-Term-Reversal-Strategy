# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-29 10:15:01 EDT`
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

- Cash: `$34,954.75`
- Equity: `$34,954.75`
- Realized PnL: `$24,954.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-29)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
   CSX     option         option CSX260918C00052500    129          2026-07-28         2026-07-29        1.425      1.2825 -1838.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FAST          100.00               12            1.23              0.41         47.92                27.18         0.585          pass              0.577             35.2                           0.340                4.44              0.458                                 ok            True                  False
   MAR          100.00               29            0.80              2.14        382.60                28.18         0.515          pass              0.758             60.1                           0.477                4.76              0.404                                 ok            True                  False
  GILD           89.66               29            0.56              0.52        134.10                34.28         0.515          pass              0.579             47.9                           0.376                2.71             -0.019                                 ok            True                  False
   HON           80.00               15            1.70              2.94        245.79                39.75         0.511          pass              0.101              5.4                           0.168                9.06              1.144                                 ok            True                  False
  AVGO           80.00               30            1.08              2.88        379.68                41.80         0.500          pass              0.305             40.5                           0.344               -4.43             -0.033                                 ok            True                  False
  ISRG           73.91               23            1.30              3.29        360.39                72.57         0.647          pass              0.291             46.6                           0.401               -8.19             -0.882                                 ok           False                  False
   WDC           85.29               34            0.20              0.65        463.23                95.99         0.590          pass              0.651             97.0                           0.542               -9.98             -0.130           downtrend_blocked_streak           False                  False
  META           91.18               34            0.77              3.19        592.04                53.87         0.588          pass              0.602             28.5                           0.281              -13.57             -1.524 downtrend_blocked_slope_and_streak           False                  False
  TMUS           90.62               32            0.61              0.78        182.05                56.22         0.575          pass              0.644             52.1                           0.343               -3.38             -0.874            downtrend_blocked_slope           False                  False
  DRAM           78.57               28            1.77              0.59         47.52               100.66         0.558          pass              0.428             83.9                           0.541              -18.25             -1.221 downtrend_blocked_slope_and_streak           False                  False
  MRVL           84.38               32            1.99              2.44        173.43                89.75         0.520          pass              0.508             64.3                           0.351              -17.10             -1.078 downtrend_blocked_slope_and_streak           False                  False
   CSX           96.77               31            0.31              0.11         50.79                28.82         0.515          pass              0.768             59.0                           0.530                2.53              0.313                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                            detail
2026-07-29T10:15:01.489767-04:00 early_entry_1015 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:10:01.513835-04:00 early_entry_1010 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:05:02.493653-04:00 early_entry_1005 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:00:06.571588-04:00 early_entry_1000 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T09:50:04.461343-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "CSX260918C00052500", "fill_price": 1.2825, "pnl": -1838.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSX"}
2026-07-29T09:35:02.435322-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:30:03.798822-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:25:01.530149-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:20:02.789351-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:15:01.480372-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260729101501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260729101501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260729101501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260729101501)

</details>
