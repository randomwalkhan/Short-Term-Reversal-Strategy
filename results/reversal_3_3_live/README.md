# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-30 10:15:03 EDT`
Last processed slot: `early_entry_1015`

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
  FAST           96.00               25            0.58              0.21         52.46                21.92         0.509            pass              0.597             15.3                           0.185                2.92              0.223                                 ok            True                  False
  MSFT          100.00               14            1.56              5.80        527.66                19.58         0.507            pass              0.620             47.6                           0.553               -1.36             -0.075                                 ok            True                  False
  NXPI           90.91               11            2.55              4.74        263.97                41.25         0.502            pass              0.365              5.7                           0.182               13.04              1.352                                 ok            True                  False
  FTNT           78.57               14            2.76              2.69        137.95                91.61         0.671            pass              0.117              7.9                           0.202              -20.03             -1.564            downtrend_blocked_slope           False                  False
 GOOGL           73.68               19            1.35              2.68        282.67                51.94         0.637            pass              0.186             20.6                           0.233              -17.79             -1.818 downtrend_blocked_slope_and_streak           False                  False
  GOOG           75.00               20            1.25              2.46        281.26                50.42         0.632            pass              0.205             25.1                           0.264              -17.25             -1.757 downtrend_blocked_slope_and_streak           False                  False
   CSX           66.67                6            1.58              0.58         51.99                27.59         0.556            pass              0.087             10.4                           0.129                5.62              0.912                                 ok           False                  False
  MELI           65.00               20            2.03             23.59       1650.02                48.11         0.540            pass              0.219             32.8                           0.297              -11.32             -1.498 downtrend_blocked_slope_and_streak           False                  False
  META           80.77               26            1.04              4.54        622.58                38.13         0.533            pass              0.354             57.8                           0.543              -12.87             -1.651 downtrend_blocked_slope_and_streak           False                  False
  SBUX           66.67                6            2.28              1.69        104.79                26.25         0.512            pass              0.067              5.1                           0.085                5.72              0.708                                 ok           False                  False
  AAPL           94.74               19            0.93              2.28        347.93                13.86         0.498 below_threshold              0.674             56.9                           0.453                0.64              0.131                                 ok           False                  False
  ISRG           91.67               24            1.12              3.52        447.25                27.40         0.496 below_threshold              0.512             19.3                           0.184                3.99              0.434                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                               detail
2026-10-30T10:15:03.894708-04:00 early_entry_1015 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:10:05.733840-04:00 early_entry_1010 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:05:02.865531-04:00 early_entry_1005 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:00:06.058650-04:00 early_entry_1000 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T09:50:05.911217-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "MSTR261218C00140000", "fill_price": 13.5225, "pnl": -6160.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
2026-10-30T00:00:05.693119-04:00     data_refresh       data_refresh                                                                                                                                                            {'saved': 91, 'empty': 2}
2026-10-29T15:10:05.741220-04:00       entry_1500       slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-10-29T15:05:04.728633-04:00       entry_1500       slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-10-29T15:00:04.604775-04:00       entry_1500       slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-10-29T14:55:06.721591-04:00       entry_1500       slot_skipped                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261030101503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261030101503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261030101503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261030101503)

</details>
