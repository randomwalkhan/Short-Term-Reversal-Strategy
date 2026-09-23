# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-23 10:00:05 EDT`
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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           80.00               30            4.08              4.33        150.09               119.42         0.611          pass              0.291             32.3                           0.300               15.88              2.474                                 ok            True                  False
  ADSK           81.82               33            0.82              1.26        219.08                55.47         0.567          pass              0.322             21.3                           0.154                5.42              0.319                                 ok            True                  False
  DRAM           83.33               30            1.37              0.61         63.36                51.34         0.562          pass              0.378             33.2                           0.323                1.90              0.656                                 ok            True                  False
  INTC           81.82               33            1.83              1.59        123.18                67.82         0.531          pass              0.328             24.3                           0.256               14.45              2.098                                 ok            True                  False
  UPRO           82.14               28            0.98              1.06        153.29                31.44         0.505          pass              0.275             15.6                           0.224                3.42              0.505                                 ok            True                  False
  PYPL           91.43               35            0.48              0.18         52.81                57.12         0.610          pass              0.607             25.0                           0.174                0.89             -0.137                                 ok           False                  False
  NVDA           90.91               33            0.39              0.62        228.60                44.57         0.593          pass              0.636             44.0                           0.357                2.04              0.498                                 ok           False                  False
   XEL          100.00                6            1.33              0.67         71.77                15.29         0.552          pass              0.487             10.7                           0.168               -5.92             -0.566 downtrend_blocked_slope_and_streak           False                  False
   WBD           92.50               40            0.11              0.02         30.82                38.24         0.544          pass              0.841             84.4                           0.540               10.34              1.012                                 ok           False                  False
   PEP          100.00               10            1.09              1.00        130.76                15.28         0.541          pass              0.472              6.1                           0.148               -5.07             -0.630 downtrend_blocked_slope_and_streak           False                  False
   KHC           92.31               13            1.23              0.21         23.91                22.23         0.523          pass              0.432             10.6                           0.197               -3.68             -0.230           downtrend_blocked_streak           False                  False
  CHTR           84.21               19            2.99              2.46        116.21                65.60         0.522          pass              0.286             20.6                           0.216              -15.04             -2.095 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-09-23T10:00:05.505875-04:00 early_entry_1000      early_entry_shadow {"contract_symbol": "CTAS261023C00200000", "current_drop_pct": 0.53, "early_entry_score": 0.845, "early_reclaim_pct": 84.6, "entry_ask": 5.3, "entry_bid": 3.8, "entry_mode": "early", "entry_option_price": 4.55, "hypothetical_budget": 35735.4, "hypothetical_contracts": 78, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 32.97, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.713, "shadow_only": true, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.38, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.845, "early_reclaim_pct": 84.6, "matched_signals": 33, "recovery_stability_score": 0.713, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.38, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T09:35:04.357346-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 92, 'empty': 1}
2026-09-23T09:30:01.473090-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 92, 'empty': 1}
2026-09-23T09:25:05.427577-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 92, 'empty': 1}
2026-09-23T09:20:04.649319-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 92, 'empty': 1}
2026-09-22T15:10:06.051324-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-09-22T15:05:04.283152-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-09-22T15:00:05.737900-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-09-22T14:55:05.306648-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-09-22T14:50:01.294026-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"early_entry_score": 0.689, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 24.88, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.507}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260923100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260923100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260923100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260923100005)

</details>
