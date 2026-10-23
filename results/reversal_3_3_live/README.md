# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-23 10:20:06 EDT`
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

- Cash: `$73,431.80`
- Equity: `$142,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$-2,000.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261120C00230000       2026-10-22                   1     40     71400.0                 69400.0        17.85          17.35      223.97        222.07          bid_ask_mid                      17.35                bid_ask_mid                    True         -2000.0                   -2.8         100.0               38              0.68         80.16           83.24                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           91.67               12            1.39              0.34         35.04                27.06         0.564          pass              0.401              6.7                           0.089                9.26              0.899                                 ok            True                  False
   KHC           81.25               16            1.59              0.28         24.97                34.71         0.533          pass              0.134              2.5                           0.087               10.87              1.084                                 ok            True                  False
   EXC           80.00               15            0.98              0.31         44.72                20.91         0.532          pass              0.180             31.2                           0.211                6.35              0.570                                 ok            True                  False
   MAR           88.89               18            0.99              2.75        395.62                21.06         0.527          pass              0.446             34.3                           0.303                7.38              0.946                                 ok            True                  False
   ADP           91.30               23            0.72              1.56        307.27                23.94         0.512          pass              0.645             68.4                           0.387               12.86              1.238                                 ok            True                  False
   AEP           86.36               22            0.75              0.69        130.35                17.81         0.507          pass              0.339             12.9                           0.142                5.58              0.486                                 ok            True                  False
   CEG           85.71               28            1.02              1.83        254.43                65.49         0.609          pass              0.535             67.2                           0.723              -15.25             -1.687 downtrend_blocked_slope_and_streak           False                  False
  MDLZ          100.00                1            2.21              1.01         64.76                24.03         0.577          pass              0.472              4.6                           0.109                5.53              0.539                                 ok           False                  False
  REGN           77.78                9            1.94             11.14        814.31                31.70         0.553          pass              0.055              0.0                           0.163                7.59              0.825                                 ok           False                  False
   WDC           75.56               45            0.18              0.44        354.00                71.39         0.551          pass              0.544             96.3                           0.900              -11.00             -0.877 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00               39            0.49              0.76        222.83                49.30         0.535          pass              0.843             65.5                           0.427                7.39              0.935                                 ok           False                  False
  MSTR           89.19               37            0.68              0.69        145.50                68.96         0.535          pass              0.727             82.9                           0.474               -6.17             -0.538            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-23T10:20:06.283023-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:15:04.978635-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:10:06.503805-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:05:04.082507-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:00:04.565947-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T00:00:06.660227-04:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-10-22T15:10:06.169647-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-22T15:05:02.793544-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-22T15:00:05.670192-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-22T14:55:05.642488-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261023102006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261023102006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261023102006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261023102006)

</details>
