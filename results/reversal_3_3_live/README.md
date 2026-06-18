# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 09:40:01 EDT`
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
  PAYX          100.00               13            1.48              1.01         97.15                31.76         0.582          pass              0.512             11.1                           0.125               -3.36             -0.219                                 ok            True                  False
  FTNT           92.31               13            2.19              2.21        143.19                48.02         0.581          pass              0.489             27.5                           0.256               -5.80             -0.023                                 ok            True                  False
  PANW           87.10               31            1.44              2.85        280.91                57.71         0.535          pass              0.467             28.2                           0.325               -0.43              0.464                                 ok            True                  False
    ZS           58.82               17            3.41              2.97        123.11               152.31         0.840          pass              0.147              5.4                           0.190              -11.18             -0.665 downtrend_blocked_slope_and_streak           False                  False
   KHC           85.71                7            0.56              0.09         23.16                27.50         0.673          pass              0.374             51.5                           0.458                4.53              0.408                                 ok           False                  False
  INTU           57.89               19            3.53              6.64        266.23                98.62         0.615          pass              0.121              0.0                           0.217              -14.04             -1.372 downtrend_blocked_slope_and_streak           False                  False
   EXC           88.00               25            0.11              0.04         45.54                20.58         0.561          pass              0.621             83.9                           0.523                1.97              0.226                                 ok           False                  False
  CRWD           72.22               18            2.38             11.37        678.09                64.33         0.545          pass              0.187             26.3                           0.321               -7.28             -0.017                                 ok           False                  False
  COST           72.22               18            0.99              6.71        962.72                23.27         0.536          pass              0.194             28.9                           0.243               -1.68             -0.048                                 ok           False                  False
   BKR           69.23               13            1.88              0.79         59.73                38.86         0.535          pass              0.099              8.5                           0.211              -10.85             -0.844 downtrend_blocked_slope_and_streak           False                  False
  GILD           88.89               27            0.45              0.39        125.28                29.17         0.523          pass              0.577             58.2                           0.366               -2.69             -0.182           downtrend_blocked_streak           False                  False
   TRI           66.67               15            2.60              1.44         78.63                52.51         0.521          pass              0.101              5.1                           0.211               -9.97             -0.891 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618094001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618094001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618094001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618094001)

</details>
