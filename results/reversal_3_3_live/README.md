# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-30 13:05:06 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           85.71               28            1.30              2.40        263.55                64.38         0.609            pass              0.503             56.7                           0.327               -3.77             -0.254                                 ok            True                  False
  MSFT          100.00               14            1.54              5.70        527.70                19.58         0.508            pass              0.623             48.4                           0.487               -1.33             -0.074                                 ok            True                  False
  FTNT           72.73               11            3.10              3.02        137.81                91.61         0.660            pass              0.098              8.3                           0.300              -20.30             -1.579            downtrend_blocked_slope           False                  False
  ALNY           80.00               25            1.91              2.33        173.00               108.34         0.654            pass              0.319             51.3                           0.411              -26.38             -2.423            downtrend_blocked_slope           False                  False
 GOOGL           76.47               17            1.49              2.96        282.55                51.94         0.643            pass              0.156             15.1                           0.214              -17.91             -1.824 downtrend_blocked_slope_and_streak           False                  False
  GOOG           73.33               15            1.55              3.07        281.01                50.42         0.641            pass              0.137             13.2                           0.199              -17.50             -1.771 downtrend_blocked_slope_and_streak           False                  False
  MELI           75.00               28            1.62             18.77       1652.08                48.11         0.524            pass              0.312             46.5                           0.557              -10.94             -1.478 downtrend_blocked_slope_and_streak           False                  False
  ISRG           85.71                7            2.38              7.46        445.56                27.40         0.518            pass              0.236             10.6                           0.233                2.67              0.376                                 ok           False                  False
  META           79.41               34            0.51              2.23        623.56                38.13         0.509            pass              0.449             79.2                           0.682              -12.41             -1.626 downtrend_blocked_slope_and_streak           False                  False
  IDXX           77.78                9            2.31              9.30        572.00                25.33         0.499 below_threshold              0.087             12.2                           0.205                0.42              0.204                                 ok           False                  False
  FAST           96.30               27            0.53              0.20         52.47                21.92         0.494 below_threshold              0.733             56.9                           0.617                2.97              0.225                                 ok           False                  False
  MPWR           65.52               29            1.19              9.95       1194.54                59.27         0.493 below_threshold              0.351             58.3                           0.256               -2.17             -0.450            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261030130506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261030130506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261030130506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261030130506)

</details>
