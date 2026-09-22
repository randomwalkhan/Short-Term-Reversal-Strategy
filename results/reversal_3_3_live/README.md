# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-22 09:50:05 EDT`
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

## Today's Closed Trades (2026-09-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           85.71               35            1.58              2.77        248.16                96.94         0.650            pass              0.390              2.0                           0.069               16.85              2.059                                 ok            True                  False
  TEAM          100.00               31            1.52              2.09        194.78                58.22         0.555            pass              0.646             16.8                           0.241                9.22              1.047                                 ok            True                  False
  FTNT           84.21               19            2.61              3.20        173.86                58.27         0.514            pass              0.224              0.0                           0.190                8.38              1.134                                 ok            True                  False
  MSFT           95.45               22            0.93              3.28        500.20                22.55         0.511            pass              0.531              0.0                           0.183                0.60              0.088                                 ok            True                  False
   TRI           94.44               36            0.07              0.05         95.41                58.54         0.602            pass              0.883             88.1                           0.467               -3.49             -0.258 downtrend_blocked_slope_and_streak           False                  False
  INTC           83.33               42            0.03              0.03        121.77                69.88         0.584            pass              0.643             98.6                           0.923               16.53              1.544                                 ok           False                  False
  PANW           72.41               29            2.02              5.25        369.51                79.39         0.563            pass              0.184              0.3                           0.033                8.10              1.160                                 ok           False                  False
   WBD           92.86               42            0.05              0.01         30.80                38.22         0.540            pass              0.747             50.0                           0.308                9.48              0.743                                 ok           False                  False
  WDAY           95.12               41            0.38              0.51        191.70                50.40         0.514            pass              0.726             24.7                           0.206                2.64              0.455                                 ok           False                  False
  ADBE           96.77               31            1.05              1.83        248.74                45.94         0.496 below_threshold              0.833             81.1                           0.421               -4.02             -0.313            downtrend_blocked_slope           False                  False
  CDNS           81.63               49            0.07              0.15        294.84                48.28         0.477 below_threshold              0.583             97.3                           0.534                3.72              0.224                                 ok           False                  False
  KLAC           71.43               35            1.32              1.69        183.24                50.30         0.476 below_threshold              0.343             43.1                           0.539               -3.93             -0.295                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                  detail
2026-09-22T09:20:04.200203-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                               {'saved': 92, 'empty': 1}
2026-09-21T15:10:05.959722-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-21T15:05:05.768467-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-21T15:00:04.975214-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-21T14:55:04.962001-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-21T14:50:06.827514-04:00       entry_1500          timing_overlay                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-21", "training_samples": 5798, "window": 5}
2026-09-21T14:50:06.827514-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-09-21T14:50:06.827514-04:00       entry_1500 entry_candidate_skipped                                                                                {"early_entry_score": 0.641, "error": "CTSH: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "CTSH", "timing_score": 0.503}
2026-09-21T14:50:06.827514-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.649, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 17.62, "option_volume": 12.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.544}
2026-09-21T12:00:03.740450-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260922095005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260922095005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260922095005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260922095005)

</details>
