# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 15:40:04 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$36,793.00`
- Equity: `$36,793.00`
- Realized PnL: `$26,793.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-27)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  GILD     option         option GILD260918C00130000     25          2026-07-24         2026-07-27         6.55        7.65 2750.0   16.793893 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   EXC           95.24               21            0.61              0.20         47.44                24.01         0.555          pass              0.734             68.5                           0.397                0.32              0.122                                 ok            True                  False
   XEL          100.00               13            1.13              0.64         81.39                20.22         0.555          pass              0.562             28.7                           0.400                0.34              0.132                                 ok            True                  False
   STX           89.47               19            4.12             24.53        841.18               103.51         0.523          pass              0.516             50.3                           0.652               -5.11              0.432                                 ok            True                  False
   WDC           90.00               20            4.35             15.84        513.01               113.75         0.520          pass              0.545             53.3                           0.648              -10.51             -0.088                                 ok            True                  False
   AEP           80.00               15            1.30              1.23        135.01                20.37         0.508          pass              0.150             22.1                           0.284               -1.36             -0.023                                 ok            True                  False
  PYPL           88.64               44            0.03              0.01         56.15                61.92         0.612          pass              0.785             97.8                           0.474               17.81              1.312                                 ok           False                  False
  DRAM           78.57               28            2.03              0.76         52.88                97.77         0.601          pass              0.371             63.6                           0.685               -9.04             -0.521            downtrend_blocked_slope           False                  False
  TMUS           89.66               29            0.83              1.05        179.64                59.26         0.576          pass              0.596             51.3                           0.276               -5.21             -0.647            downtrend_blocked_slope           False                  False
  KLAC           89.47               19            3.48              5.12        208.32                94.03         0.572          pass              0.523             51.1                           0.606               -8.57             -0.812 downtrend_blocked_slope_and_streak           False                  False
   TXN           89.47               38            0.03              0.05        279.56                50.69         0.540          pass              0.789             98.7                           0.823               -6.39             -0.690            downtrend_blocked_slope           False                  False
  INTC           86.84               38            0.93              0.60         92.06                79.50         0.537          pass              0.675             84.1                           0.674              -11.30             -0.925 downtrend_blocked_slope_and_streak           False                  False
  META           89.13               46            0.10              0.41        595.01                53.75         0.532          pass              0.692             65.0                           0.353               -9.46             -1.213 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                detail
2026-07-27T15:10:06.692175-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-27T15:05:03.663832-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-27T15:00:02.669579-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-27T14:55:05.984850-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-27T14:50:01.830454-04:00       entry_1500           entry_skipped                                                                                                                                                                                                {"reason": "no_trade_after_option_and_timing_filters"}
2026-07-27T14:50:01.830454-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.242, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 375.0, "option_spread_pct": 15.38, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "AEP", "timing_score": 0.504}
2026-07-27T14:50:01.830454-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.544, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 216.0, "option_spread_pct": 14.49, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "XEL", "timing_score": 0.558}
2026-07-27T14:50:01.830454-04:00       entry_1500          timing_overlay                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-27", "training_samples": 5518, "window": 5}
2026-07-27T12:00:02.583905-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:55:01.558921-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727154004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727154004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727154004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727154004)

</details>
