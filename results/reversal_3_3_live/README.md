# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-22 10:00:06 EDT`
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
  CRWD           87.50               40            0.80              1.40        248.75                96.94         0.667            pass              0.638             57.0                           0.364               17.78              2.095                                 ok            True                  False
  PANW           80.00               40            1.06              2.75        370.58                79.39         0.564            pass              0.412             52.0                           0.331                9.15              1.204                                 ok            True                  False
  TEAM          100.00               24            2.49              3.41        194.21                58.22         0.530            pass              0.577             10.4                           0.184                8.15              1.002                                 ok            True                  False
  WDAY           93.55               31            1.20              1.62        191.23                50.40         0.514            pass              0.586             11.0                           0.185                1.79              0.418                                 ok            True                  False
  MSFT           95.24               21            1.03              3.63        500.05                22.55         0.508            pass              0.551              9.1                           0.179                0.50              0.083                                 ok            True                  False
  FTNT           84.62               26            1.99              2.44        174.18                58.27         0.507            pass              0.371             30.1                           0.252                9.06              1.162                                 ok            True                  False
   TRI           93.94               33            0.45              0.30         95.30                58.54         0.596            pass              0.679             31.5                           0.245               -3.85             -0.275 downtrend_blocked_slope_and_streak           False                  False
  INTC           83.33               42            0.15              0.13        121.73                69.88         0.577            pass              0.626             93.0                           0.732               16.40              1.539                                 ok           False                  False
  NVDA           90.24               41            0.02              0.03        227.37                46.18         0.558            pass              0.822             97.8                           0.499                0.83              0.171                                 ok           False                  False
   KHC           95.45               22            0.12              0.02         24.36                22.03         0.548            pass              0.735             66.7                           0.403               -2.25             -0.108                                 ok           False                  False
  KLAC           74.42               43            0.02              0.02        183.96                50.30         0.511            pass              0.549             99.2                           0.892               -2.67             -0.236                                 ok           False                  False
  ADBE           96.15               26            1.45              2.53        248.44                45.94         0.500 below_threshold              0.778             73.8                           0.352               -4.41             -0.331            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-22T10:00:06.196250-04:00 early_entry_1000      early_entry_shadow {"contract_symbol": "GILD261030C00150000", "current_drop_pct": 0.54, "early_entry_score": 0.825, "early_reclaim_pct": 95.3, "entry_ask": 7.35, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 6.225, "hypothetical_budget": 35735.4, "hypothetical_contracts": 57, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 36.14, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.659, "shadow_only": true, "success_rate": 93.55, "ticker": "GILD", "timing_score": 0.374, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.825, "early_reclaim_pct": 95.3, "matched_signals": 31, "recovery_stability_score": 0.659, "success_rate": 93.55, "ticker": "GILD", "timing_score": 0.374, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T09:20:04.200203-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 92, 'empty': 1}
2026-09-21T15:10:05.959722-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-21T15:05:05.768467-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-21T15:00:04.975214-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-21T14:55:04.962001-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-21T14:50:06.827514-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"early_entry_score": 0.641, "error": "CTSH: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "CTSH", "timing_score": 0.503}
2026-09-21T14:50:06.827514-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"early_entry_score": 0.649, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 17.62, "option_volume": 12.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.544}
2026-09-21T14:50:06.827514-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-21", "training_samples": 5798, "window": 5}
2026-09-21T14:50:06.827514-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_trade_after_option_and_timing_filters"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260922100006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260922100006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260922100006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260922100006)

</details>
