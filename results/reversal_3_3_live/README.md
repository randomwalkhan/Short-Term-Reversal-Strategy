# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-30 10:25:05 EDT`
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
  ALNY           86.84               38            0.82              0.99        173.57               108.34         0.667            pass              0.607             57.1                           0.292              -25.56             -2.373            downtrend_blocked_slope           False                  False
  FTNT           70.00               10            3.17              3.09        137.78                91.61         0.660            pass              0.075              3.1                           0.097              -20.36             -1.583            downtrend_blocked_slope           False                  False
 GOOGL           73.68               19            1.35              2.69        282.67                51.94         0.637            pass              0.184             20.2                           0.190              -17.80             -1.818 downtrend_blocked_slope_and_streak           False                  False
  GOOG           73.68               19            1.27              2.51        281.25                50.42         0.635            pass              0.195             23.8                           0.219              -17.27             -1.758 downtrend_blocked_slope_and_streak           False                  False
   CEG           84.21               38            0.42              0.78        264.25                64.38         0.597            pass              0.617             86.0                           0.639               -2.91             -0.214                                 ok           False                  False
  MELI           69.23               13            2.35             27.36       1648.40                48.11         0.570            pass              0.143             22.0                           0.187              -11.61             -1.513 downtrend_blocked_slope_and_streak           False                  False
   CSX           72.73               11            1.17              0.43         52.06                27.59         0.553            pass              0.163             33.8                           0.362                6.06              0.931                                 ok           False                  False
  META           77.27               22            1.19              5.21        622.29                38.13         0.546            pass              0.289             51.6                           0.407              -13.01             -1.658 downtrend_blocked_slope_and_streak           False                  False
  SBUX           71.43                7            2.17              1.60        104.82                26.25         0.514            pass              0.115             21.3                           0.192                5.84              0.713                                 ok           False                  False
  MSFT          100.00               11            1.93              7.17        527.07                19.58         0.506            pass              0.563             35.1                           0.294               -1.73             -0.093           downtrend_blocked_streak           False                  False
  NXPI           87.50                8            2.85              5.30        263.73                41.25         0.499 below_threshold              0.253              1.2                           0.105               12.69              1.338                                 ok           False                  False
  FAST           96.30               27            0.57              0.21         52.46                21.92         0.497 below_threshold              0.629             22.1                           0.228                2.93              0.223                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                               detail
2026-10-30T10:25:05.620452-04:00 early_entry_1025 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:20:04.876554-04:00 early_entry_1020 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:15:03.894708-04:00 early_entry_1015 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:10:05.733840-04:00 early_entry_1010 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:05:02.865531-04:00 early_entry_1005 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:00:06.058650-04:00 early_entry_1000 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T09:50:05.911217-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "MSTR261218C00140000", "fill_price": 13.5225, "pnl": -6160.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
2026-10-30T00:00:05.693119-04:00     data_refresh       data_refresh                                                                                                                                                            {'saved': 91, 'empty': 2}
2026-10-29T15:10:05.741220-04:00       entry_1500       slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-10-29T15:05:04.728633-04:00       entry_1500       slot_skipped                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261030102505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261030102505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261030102505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261030102505)

</details>
