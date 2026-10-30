# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-30 12:50:06 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           85.71               28            1.39              2.58        263.47                64.38         0.604          pass              0.493             53.5                           0.367               -3.86             -0.258                                 ok            True                  False
  FAST           95.45               22            0.70              0.26         52.44                21.92         0.515          pass              0.661             43.2                           0.577                2.79              0.217                                 ok            True                  False
  MSFT          100.00               13            1.67              6.20        527.48                19.58         0.507          pass              0.602             43.9                           0.417               -1.47             -0.080                                 ok            True                  False
  IDXX           81.82               11            2.13              8.58        572.30                25.33         0.500          pass              0.162             19.0                           0.343                0.60              0.212                                 ok            True                  False
  FTNT           72.73               11            3.12              3.04        137.80                91.61         0.659          pass              0.095              7.6                           0.263              -20.32             -1.581            downtrend_blocked_slope           False                  False
  ALNY           79.17               24            2.00              2.43        172.96               108.34         0.654          pass              0.306             49.2                           0.599              -26.44             -2.427            downtrend_blocked_slope           False                  False
 GOOGL           75.00               16            1.53              3.04        282.52                51.94         0.646          pass              0.134             10.0                           0.125              -17.94             -1.826 downtrend_blocked_slope_and_streak           False                  False
  GOOG           71.43               14            1.59              3.14        280.97                50.42         0.644          pass              0.104              4.5                           0.083              -17.54             -1.772 downtrend_blocked_slope_and_streak           False                  False
  MELI           72.00               25            1.72             19.94       1651.58                48.11         0.534          pass              0.283             43.2                           0.518              -11.03             -1.483 downtrend_blocked_slope_and_streak           False                  False
  META           79.31               29            0.80              3.49        623.03                38.13         0.524          pass              0.382             67.6                           0.476              -12.66             -1.640 downtrend_blocked_slope_and_streak           False                  False
  ISRG           85.71                7            2.32              7.29        445.63                27.40         0.522          pass              0.234              9.9                           0.259                2.73              0.379                                 ok           False                  False
  SBUX           71.43                7            2.13              1.57        104.84                26.25         0.512          pass              0.145             31.3                           0.489                5.89              0.715                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-30T12:00:06.415858-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:55:05.950697-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:50:06.698728-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:45:05.073767-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:40:04.093863-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:35:04.895794-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:30:05.799923-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:25:03.898317-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:20:07.033470-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:15:06.943574-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261030125006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261030125006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261030125006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261030125006)

</details>
