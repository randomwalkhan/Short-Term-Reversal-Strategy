# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 11:00:03 EDT`
Last processed slot: `manage_1100`

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

## Today's Closed Trades (2026-09-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KHC           93.75               16            0.63              0.11         24.38                22.04         0.548            pass              0.496             11.4                           0.231               -2.31             -0.132                                 ok            True                  False
  WDAY           94.29               35            0.54              0.73        193.56                50.60         0.544            pass              0.760             52.8                           0.337               -1.52              0.313                                 ok            True                  False
   PEP          100.00               13            0.78              0.71        129.45                15.76         0.547            pass              0.603             42.7                           0.569               -6.46             -0.637 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.44               39            0.17              0.30        248.79                46.23         0.539            pass              0.920             90.8                           0.742               -6.76             -0.430            downtrend_blocked_slope           False                  False
  CHTR           88.89               27            2.11              1.90        127.36                64.18         0.535            pass              0.457             17.6                           0.209              -17.46             -1.452 downtrend_blocked_slope_and_streak           False                  False
   ADP           95.45               22            0.63              1.19        270.71                22.01         0.521            pass              0.705             57.5                           0.564               -2.30              0.129           downtrend_blocked_streak           False                  False
  TMUS           92.86               14            1.38              1.62        167.49                33.56         0.521            pass              0.612             63.4                           0.775               -8.62             -0.882            downtrend_blocked_slope           False                  False
  VRSK           86.67               15            1.97              2.41        174.38                39.25         0.513            pass              0.334             23.8                           0.406               -7.20             -0.260            downtrend_blocked_slope           False                  False
   XEL          100.00               27            0.08              0.04         72.28                19.27         0.499 below_threshold              0.818             85.0                           0.629               -3.83             -0.524            downtrend_blocked_slope           False                  False
  PAYX           84.21               19            1.13              0.92        115.75                23.92         0.494 below_threshold              0.320             32.9                           0.483               -5.66             -0.204           downtrend_blocked_streak           False                  False
  SBUX           81.82               11            1.49              1.00         95.40                22.99         0.494 below_threshold              0.210             35.1                           0.435               -9.64             -0.836 downtrend_blocked_slope_and_streak           False                  False
   EXC           96.43               28            0.06              0.02         42.06                15.92         0.492 below_threshold              0.856             95.5                           0.666               -3.65             -0.456 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-21T11:00:03.910998-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:55:06.015379-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:50:06.524394-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:45:06.703596-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:40:05.776403-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:35:04.666862-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:30:01.878721-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:25:03.822733-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:20:05.839585-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:15:05.893967-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921110003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921110003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921110003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921110003)

</details>
