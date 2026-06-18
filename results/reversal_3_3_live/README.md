# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 09:30:03 EDT`
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
  PAYX          100.00               19            0.94              0.64         97.31                31.76         0.586          pass              0.519              0.0                           0.282               -2.83             -0.195                                 ok            True                  False
  FTNT           94.12               17            1.96              2.02        146.16                48.02         0.542          pass              0.615             46.0                           0.486               -3.69              0.078                                 ok            True                  False
    ZS           77.14               35            1.07              0.93        123.98               152.31         0.883          pass              0.328             24.4                           0.392               -9.03             -0.556 downtrend_blocked_slope_and_streak           False                  False
   KHC           80.00                5            0.65              0.11         23.15                27.50         0.680          pass              0.068              0.0                           0.308                4.44              0.404                                 ok           False                  False
  INTU           66.67               24            2.68              5.04        266.92                98.62         0.659          pass              0.170              3.7                           0.263              -13.28             -1.332 downtrend_blocked_slope_and_streak           False                  False
   PEP          100.00               19            0.21              0.21        141.50                22.29         0.620          pass              0.669             49.2                           0.406                0.44              0.158                                 ok           False                  False
   APP           82.22               45            0.01              0.02        479.48                73.91         0.573          pass              0.607             96.8                           0.601              -14.21             -1.481            downtrend_blocked_slope           False                  False
   ADI           93.94               33            0.40              1.18        415.50                53.37         0.571          pass              0.622             13.4                           0.219               -3.37              0.198                                 ok           False                  False
  TEAM           87.80               41            0.81              0.48         84.18                82.55         0.565          pass              0.652             62.4                           0.482              -17.53             -1.875 downtrend_blocked_slope_and_streak           False                  False
   ADP          100.00               15            1.46              2.27        221.03                29.04         0.561          pass              0.603             37.9                           0.531               -4.71             -0.532            downtrend_blocked_slope           False                  False
  AMGN           83.33                6            1.78              4.33        345.99                27.62         0.557          pass              0.237             30.9                           0.388               -1.14             -0.042                                 ok           False                  False
   TRI           75.00               20            1.89              1.05         78.80                52.51         0.557          pass              0.122              0.0                           0.225               -9.32             -0.858 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618093003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618093003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618093003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618093003)

</details>
