# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-30 10:40:05 EDT`
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

- Cash: `$117,176.55`
- Equity: `$117,176.55`
- Realized PnL: `$107,176.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  MSTR     option         option MSTR261218C00140000     41          2026-10-29         2026-10-30       15.025     13.5225 -6160.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FAST           95.45               22            0.71              0.26         52.44                21.92         0.519            pass              0.557              8.5                           0.122                2.78              0.216                                 ok            True                  False
    ZS           87.50               16            3.01              5.22        245.58                59.82         0.504            pass              0.386             31.7                           0.392               15.90              2.006                                 ok            True                  False
  ALNY           83.33               30            1.45              1.77        173.24               108.34         0.674            pass              0.361             23.7                           0.134              -26.03             -2.402            downtrend_blocked_slope           False                  False
  FTNT           82.35               17            2.43              2.37        138.09                91.61         0.673            pass              0.254             25.7                           0.349              -19.75             -1.548            downtrend_blocked_slope           False                  False
  GOOG           76.19               21            1.18              2.33        281.32                50.42         0.631            pass              0.224             29.3                           0.304              -17.19             -1.753 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           73.91               23            1.24              2.47        282.76                51.94         0.620            pass              0.229             26.8                           0.288              -17.70             -1.813 downtrend_blocked_slope_and_streak           False                  False
   CSX           66.67                6            1.58              0.58         51.99                27.59         0.556            pass              0.087             10.4                           0.211                5.62              0.912                                 ok           False                  False
  MELI           75.76               33            1.21             14.09       1654.09                48.11         0.516            pass              0.384             59.8                           0.659              -10.58             -1.460 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00                9            3.71              5.30        201.83                50.04         0.514            pass              0.543             30.6                           0.444               -5.43             -0.500            downtrend_blocked_slope           False                  False
  CRWD           76.19               21            2.29              4.18        259.36                58.11         0.510            pass              0.233             36.2                           0.350               12.22              1.744                                 ok           False                  False
  META           81.08               37            0.36              1.57        623.85                38.13         0.504            pass              0.515             85.4                           0.746              -12.27             -1.620 downtrend_blocked_slope_and_streak           False                  False
  SBUX           60.00                5            2.48              1.83        104.72                26.25         0.497 below_threshold              0.083             11.2                           0.176                5.51              0.698                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                               detail
2026-10-30T10:40:05.937875-04:00 early_entry_1040 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:35:06.022002-04:00 early_entry_1035 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:30:06.573840-04:00 early_entry_1030 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:25:05.620452-04:00 early_entry_1025 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:20:04.876554-04:00 early_entry_1020 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:15:03.894708-04:00 early_entry_1015 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:10:05.733840-04:00 early_entry_1010 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:05:02.865531-04:00 early_entry_1005 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:00:06.058650-04:00 early_entry_1000 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T09:50:05.911217-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "MSTR261218C00140000", "fill_price": 13.5225, "pnl": -6160.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261030104005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261030104005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261030104005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261030104005)

</details>
