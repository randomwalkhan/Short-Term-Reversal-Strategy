# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 09:55:01 EDT`
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
  CRWD           80.77               26            1.43              6.82        680.04                64.33         0.563          pass              0.351             55.8                           0.382               -6.38              0.027                                 ok            True                  False
   WMT           87.10               31            0.52              0.43        117.95                34.58         0.552          pass              0.488             34.6                           0.323               -0.19              0.028                                 ok            True                  False
    ZS           68.18               22            2.54              2.21        123.43               152.31         0.860          pass              0.255             29.6                           0.258              -10.38             -0.624 downtrend_blocked_slope_and_streak           False                  False
   KHC           85.71                7            0.43              0.07         23.17                27.50         0.681          pass              0.409             62.7                           0.546                4.67              0.414                                 ok           False                  False
  INTU           70.37               27            1.94              3.65        267.52                98.62         0.681          pass              0.323             47.1                           0.544              -12.62             -1.298 downtrend_blocked_slope_and_streak           False                  False
  PAYX          100.00               27            0.32              0.22         97.49                31.76         0.561          pass              0.812             80.9                           0.601               -2.22             -0.166                                 ok           False                  False
  TEAM           88.10               42            0.64              0.38         84.23                82.55         0.558          pass              0.710             79.4                           0.711              -17.39             -1.868 downtrend_blocked_slope_and_streak           False                  False
  GILD           84.21               19            0.81              0.71        125.15                29.17         0.551          pass              0.301             24.6                           0.187               -3.04             -0.198           downtrend_blocked_streak           False                  False
  PANW           90.48               42            0.25              0.50        281.92                57.71         0.542          pass              0.796             87.5                           0.523                0.78              0.518                                 ok           False                  False
  WDAY           78.79               33            1.41              1.20        121.32                69.08         0.541          pass              0.389             60.4                           0.619              -18.79             -2.093 downtrend_blocked_slope_and_streak           False                  False
   TRI           72.22               18            2.28              1.27         78.71                52.51         0.528          pass              0.156             16.6                           0.142               -9.68             -0.877 downtrend_blocked_slope_and_streak           False                  False
  COST           50.00               10            1.53             10.33        961.16                23.27         0.527          pass              0.053              0.0                           0.177               -2.21             -0.073                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot              event_type                                                                                                                                                                                                                                                                  detail
2026-06-18T09:20:05.276411-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                                           {'saved': 93}
2026-06-17T16:10:06.900615-04:00  manage_1600                    exit                                                                                     {"asset_type": "option", "contract_symbol": "GOOG260724C00380000", "fill_price": 8.3025, "pnl": -1383.75, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GOOG"}
2026-06-17T15:10:05.396926-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-17T15:05:04.450318-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-17T15:00:06.393380-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-17T14:55:04.542004-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-17T14:50:06.575124-04:00   entry_1500 entry_candidate_skipped {"early_entry_score": 0.711, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 67.0, "option_spread_pct": 30.66, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.589}
2026-06-17T14:50:06.575124-04:00   entry_1500          timing_overlay                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-17", "training_samples": 5231, "window": 5}
2026-06-17T14:50:06.575124-04:00   entry_1500 entry_candidate_skipped                                                                                   {"early_entry_score": 0.468, "error": "XEL: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "XEL", "timing_score": 0.64}
2026-06-17T14:50:06.575124-04:00   entry_1500 entry_candidate_skipped                                                                                {"early_entry_score": 0.541, "error": "PAYX: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "PAYX", "timing_score": 0.608}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618095501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618095501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618095501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618095501)

</details>
