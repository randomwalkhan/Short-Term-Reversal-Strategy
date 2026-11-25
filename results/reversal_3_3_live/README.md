# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-25 12:54:28 EST`
Last processed slot: `manage_1300`

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

- Cash: `$103,969.80`
- Equity: `$103,969.80`
- Realized PnL: `$93,969.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  REGN           81.48               27            1.02              7.06        984.07                56.69         0.606          pass              0.368             51.6                           0.603                1.94              0.097                                 ok            True                  False
  AMGN           90.48               21            0.66              2.18        473.00                33.69         0.567          pass              0.614             68.3                           0.746                1.16             -0.093                                 ok            True                  False
   APP           87.50               32            1.76              4.70        379.10               128.63         0.769          pass              0.646             74.3                           0.787               -7.50             -1.084 downtrend_blocked_slope_and_streak           False                  False
  ALNY           80.00               45            0.48              0.55        164.37               118.50         0.739          pass              0.543             89.6                           0.885                2.48             -0.105                                 ok           False                  False
  INTC           52.94               17            4.58              1.76         54.05               154.72         0.717          pass              0.285             55.5                           0.853              -16.34             -1.346 downtrend_blocked_slope_and_streak           False                  False
  IDXX           97.50               40            0.35              1.76        711.33                78.73         0.692          pass              0.923             84.6                           0.757                0.99             -0.015                                 ok           False                  False
  FTNT           84.78               46            0.05              0.05        132.48                97.42         0.689          pass              0.693             98.8                           0.889                3.38              0.384                                 ok           False                  False
  MCHP           85.71               28            0.78              0.31         56.23                89.73         0.687          pass              0.596             85.0                           0.894               -9.25             -0.878            downtrend_blocked_slope           False                  False
  MPWR           50.00               16            3.61             30.09       1177.21               121.95         0.641          pass              0.267             54.2                           0.754              -22.42             -2.249            downtrend_blocked_slope           False                  False
  UPRO           66.67                9            3.03              2.50        116.85                94.19         0.620          pass              0.269             69.1                           0.894              -19.30             -2.457 downtrend_blocked_slope_and_streak           False                  False
  MRVL           61.11               18            4.66              4.29        129.73               142.93         0.615          pass              0.281             55.5                           0.860              -25.68             -2.757            downtrend_blocked_slope           False                  False
  NVDA           75.00                4            6.01              6.54        152.58               127.00         0.612          pass              0.164             34.3                           0.672              -15.94             -1.451 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                    detail
2026-11-25T11:56:08.535993-05:00 early_entry_1155      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-25T10:40:03.209992-05:00 early_entry_1040      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-25T10:06:20.719395-05:00 early_entry_1005      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-25T09:20:10.412914-05:00     data_refresh            data_refresh                                                                                                                                                                                                                 {'saved': 91, 'empty': 2}
2026-11-24T15:10:06.406477-05:00       entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-24T15:05:05.745009-05:00       entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-24T15:00:04.642854-05:00       entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-24T14:55:06.326922-05:00       entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-24T14:50:04.541007-05:00       entry_1500           entry_skipped                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-11-24T14:50:04.541007-05:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.494, "option_liquidity_status": "low_volume", "option_open_interest": 122.0, "option_spread_pct": 8.89, "option_volume": 4.0, "reason": "no_trade_low_option_liquidity", "ticker": "ODFL", "timing_score": 0.512}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261125125428)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261125125428)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261125125428)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261125125428)

</details>
