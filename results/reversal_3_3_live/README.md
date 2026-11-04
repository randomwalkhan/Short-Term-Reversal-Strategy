# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 10:30:06 EST`
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

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   ADI           80.00               15            1.86              5.46        417.45                38.61         0.500 below_threshold              0.122             12.9                           0.239                1.49              0.580                                 ok            True                  False
  INTC           63.64               22            2.81              1.19         60.04               129.60         0.753            pass              0.255             33.1                           0.292              -36.69             -4.942            downtrend_blocked_slope           False                  False
  SOXL           65.00               20            4.58              2.34         72.12               167.58         0.648            pass              0.260             42.9                           0.307              -32.42             -3.039            downtrend_blocked_slope           False                  False
  DRAM           65.00               20            2.41              0.80         47.30                69.30         0.565            pass              0.226             34.3                           0.277               -5.43             -0.134                                 ok           False                  False
  REGN           75.00                4            2.80             19.09        965.18                48.26         0.546            pass              0.098             14.5                           0.195               17.43              2.097                                 ok           False                  False
  LRCX           69.05               42            0.00              0.01        230.72                62.98         0.533            pass              0.553             99.9                           0.675              -11.54             -0.517            downtrend_blocked_slope           False                  False
  ASML           76.92               13            2.33             25.32       1541.29                44.05         0.520            pass              0.154             27.4                           0.300               -9.47             -0.548            downtrend_blocked_slope           False                  False
  KLAC           73.53               34            0.87              0.95        155.79                57.09         0.516            pass              0.411             66.5                           0.429               -5.25              0.273                                 ok           False                  False
  NVDA           75.00               20            1.04              1.51        206.04                32.59         0.507            pass              0.305             62.5                           0.530               -7.85             -0.701 downtrend_blocked_slope_and_streak           False                  False
  AVGO           75.00               32            0.88              2.04        331.25                44.04         0.504            pass              0.364             55.6                           0.364               -2.54             -0.024                                 ok           False                  False
  MCHP           90.00               20            1.85              1.01         77.47                45.40         0.499 below_threshold              0.383              0.0                           0.203               -0.90              0.240                                 ok           False                  False
  AMAT           68.42               38            0.70              1.88        381.11                58.39         0.497 below_threshold              0.472             78.7                           0.615               -7.27             -0.233                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                            detail
2026-11-04T10:30:06.151589-05:00 early_entry_1030 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:25:06.359695-05:00 early_entry_1025 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:20:05.681556-05:00 early_entry_1020 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:15:05.290161-05:00 early_entry_1015 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:10:06.483796-05:00 early_entry_1010 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:05:05.606953-05:00 early_entry_1005 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:00:05.152440-05:00 early_entry_1000 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T09:20:05.283761-05:00     data_refresh       data_refresh                                                                                                                                                         {'saved': 91, 'empty': 2}
2026-11-03T16:10:06.665587-05:00      manage_1600               exit {"asset_type": "option", "contract_symbol": "MDLZ261218C00067500", "fill_price": 1.305, "pnl": -6815.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MDLZ"}
2026-11-03T15:10:05.032509-05:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104103006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104103006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104103006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104103006)

</details>
