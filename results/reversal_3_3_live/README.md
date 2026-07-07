# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-07 10:46:12 EDT`
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

- Cash: `$25,746.75`
- Equity: `$25,746.75`
- Realized PnL: `$15,746.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-07)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  AMAT     option         option AMAT260821C00600000      1          2026-07-06         2026-07-07       75.775     68.1975 -757.75       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  UPRO           93.33               15            2.09              2.12        143.50                55.41         0.586            pass              0.494             15.5                           0.203                0.20              0.524                                 ok            True                  False
  VRTX           90.00               10            1.80              6.66        526.73                27.95         0.526            pass              0.449             43.4                           0.637               11.41              1.301                                 ok            True                  False
  CSCO           90.91               11            1.58              1.26        113.44                39.71         0.575            pass              0.403             16.1                           0.205               -7.35             -0.722 downtrend_blocked_slope_and_streak           False                  False
  PCAR           78.57               14            1.83              1.61        125.22                37.79         0.530            pass              0.127             15.8                           0.277                2.91              0.450                                 ok           False                  False
  FAST           94.12               17            1.35              0.46         48.11                20.37         0.497 below_threshold              0.516             14.5                           0.237                3.34              0.543                                 ok           False                  False
  MSTR           65.52               29            2.82              1.99         99.92               102.64         0.490 below_threshold              0.252             25.5                           0.286              -10.53             -0.215           downtrend_blocked_streak           False                  False
  ODFL           88.10               42            0.22              0.33        216.30                38.04         0.481 below_threshold              0.691             75.8                           0.524               -1.62             -0.138                                 ok           False                  False
  QCOM           70.59               17            3.38              4.42        184.59                82.48         0.477 below_threshold              0.141             15.6                           0.130              -18.81             -1.824 downtrend_blocked_slope_and_streak           False                  False
   ADI           60.00                5            4.29             11.68        383.83                61.47         0.470 below_threshold              0.065              6.0                           0.171              -16.46             -1.341            downtrend_blocked_slope           False                  False
  FTNT           92.86               14            2.39              2.72        161.18                37.70         0.455 below_threshold              0.540             41.8                           0.588                8.99              1.047                                 ok           False                  False
  ASML           80.00                5            5.66             72.32       1794.07                78.10         0.452 below_threshold              0.058              4.1                           0.232              -10.76             -0.318            downtrend_blocked_slope           False                  False
   APP           82.14               28            2.73             10.40        539.33                75.58         0.438 below_threshold              0.347             42.2                           0.567               12.68              1.937                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-07-07T10:46:12.062462-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-07T09:56:39.997866-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "AMAT260821C00600000", "fill_price": 68.1975, "pnl": -757.75, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "AMAT"}
2026-07-07T00:00:02.324788-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-07-06T15:10:01.561163-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-06T15:05:05.496825-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-06T15:00:02.458877-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-06T14:55:01.446622-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-06T14:50:04.793934-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"allocated_cash": 7577.5, "asset_type": "option", "contract_symbol": "AMAT260821C00600000", "contracts": 1, "early_entry_score": 0.663, "entry_mode": "regular", "entry_option_price": 75.775, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 762.0, "option_spread_pct": 7.32, "option_volume": 41.0, "success_rate": 95.83, "ticker": "AMAT", "timing_score": 0.677}
2026-07-06T14:50:04.793934-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-06", "training_samples": 5342, "window": 5}
2026-07-06T12:00:06.575444-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "VRTX260807C00525000", "current_drop_pct": 0.75, "early_entry_score": 0.793, "early_reclaim_pct": 74.7, "entry_ask": 26.8, "entry_bid": 18.0, "entry_mode": "early", "entry_option_price": 22.4, "hypothetical_budget": 13252.25, "hypothetical_contracts": 5, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 4.0, "option_spread_pct": 39.29, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.633, "shadow_only": true, "success_rate": 93.94, "ticker": "VRTX", "timing_score": 0.436, "top_candidates": [{"current_drop_pct": 0.75, "early_entry_score": 0.793, "early_reclaim_pct": 74.7, "matched_signals": 33, "recovery_stability_score": 0.633, "success_rate": 93.94, "ticker": "VRTX", "timing_score": 0.436, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260707104612)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260707104612)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260707104612)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260707104612)

</details>
