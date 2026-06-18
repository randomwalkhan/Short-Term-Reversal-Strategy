# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 10:25:02 EDT`
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

- Cash: `$26,514.50`
- Equity: `$26,514.50`
- Realized PnL: `$16,514.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           86.21               29            0.64              0.53        117.90                34.58         0.557          pass              0.407             19.7                           0.262               -0.31              0.023                                 ok            True                  False
  CRWD           84.38               32            1.11              5.29        680.69                64.33         0.547          pass              0.515             65.7                           0.600               -6.07              0.042                                 ok            True                  False
  PANW           90.00               40            0.67              1.33        281.56                57.71         0.527          pass              0.719             66.5                           0.361                0.35              0.499                                 ok            True                  False
  MDLZ           95.45               22            0.88              0.37         60.70                21.28         0.524          pass              0.556              7.8                           0.085               -1.09             -0.154                                 ok            True                  False
    ZS           73.33               30            1.58              1.38        123.79               152.31         0.869          pass              0.388             56.0                           0.760               -9.50             -0.580 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            0.71              0.12         23.15                27.50         0.705          pass              0.586             38.4                           0.324                4.37              0.401                                 ok           False                  False
  INTU           75.00               36            1.24              2.33        268.08                98.62         0.674          pass              0.439             66.1                           0.759              -12.00             -1.265 downtrend_blocked_slope_and_streak           False                  False
   TRI           77.78               27            0.69              0.39         79.08                52.51         0.582          pass              0.396             74.7                           0.811               -8.21             -0.803 downtrend_blocked_slope_and_streak           False                  False
  AMGN           93.75               16            1.10              2.64        340.53                27.62         0.575          pass              0.488              7.8                           0.177               -2.23             -0.092           downtrend_blocked_streak           False                  False
  GILD           90.00               10            1.56              1.37        124.86                29.17         0.567          pass              0.334              3.4                           0.172               -3.78             -0.233           downtrend_blocked_streak           False                  False
  PAYX          100.00               30            0.06              0.04         97.56                31.76         0.558          pass              0.878             96.3                           0.832               -1.97             -0.155                                 ok           False                  False
  WDAY           81.58               38            0.88              0.75        121.51                69.08         0.547          pass              0.509             75.3                           0.751              -18.36             -2.068 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-18T10:25:02.315380-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:20:06.081546-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:15:06.113244-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:10:05.150482-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:05:02.276759-04:00 early_entry_1005 early_entry_shadow                {"contract_symbol": "FTNT260724C00143000", "current_drop_pct": 0.68, "early_entry_score": 0.881, "early_reclaim_pct": 77.6, "entry_ask": 9.5, "entry_bid": 5.95, "entry_mode": "early", "entry_option_price": 7.725, "hypothetical_budget": 13257.25, "hypothetical_contracts": 17, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 34.0, "option_spread_pct": 45.95, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.741, "shadow_only": true, "success_rate": 97.56, "ticker": "FTNT", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.881, "early_reclaim_pct": 77.6, "matched_signals": 41, "recovery_stability_score": 0.741, "success_rate": 97.56, "ticker": "FTNT", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-18T10:00:05.319103-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "FTNT260724C00143000", "current_drop_pct": 0.62, "early_entry_score": 0.886, "early_reclaim_pct": 79.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 9.9, "hypothetical_budget": 13257.25, "hypothetical_contracts": 13, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 34.0, "option_spread_pct": null, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.755, "shadow_only": true, "success_rate": 97.62, "ticker": "FTNT", "timing_score": 0.481, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.886, "early_reclaim_pct": 79.3, "matched_signals": 42, "recovery_stability_score": 0.755, "success_rate": 97.62, "ticker": "FTNT", "timing_score": 0.481, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-18T09:20:05.276411-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-06-17T16:10:06.900615-04:00      manage_1600               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "GOOG260724C00380000", "fill_price": 8.3025, "pnl": -1383.75, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GOOG"}
2026-06-17T15:10:05.396926-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T15:05:04.450318-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618102502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618102502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618102502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618102502)

</details>
