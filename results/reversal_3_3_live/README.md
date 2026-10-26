# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-26 15:50:06 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$1,421.80`
- Equity: `$138,694.30`
- Realized PnL: `$127,691.80`
- Unrealized PnL: `$1,002.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option  EXC261218C00045000       2026-10-23                   1    657     72270.0                 73912.5          1.1           1.12       44.42         44.42          bid_ask_mid                       1.12                bid_ask_mid                    True          1642.5                   2.27          80.0               15              0.97         20.09           21.53                  20.91                 278.0           48.0               0.09                      ok
  TEAM     option         option TEAM261218C00230000       2026-10-26                   0     32     64000.0                 63360.0         20.0          19.80      220.60        222.36          bid_ask_mid                      19.80                bid_ask_mid                    True          -640.0                  -1.00         100.0               12              3.08         70.90           67.58                  47.89                 302.0           39.0               0.10                      ok
```

## Today's Closed Trades (2026-10-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM261120C00230000     40          2026-10-22         2026-10-26        17.85      16.065 -7140.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   ADP           81.82               11            1.30              2.76        302.98                24.93         0.545            pass              0.180             23.6                           0.494                9.65              1.097                                 ok            True                  False
   KHC           89.29               28            0.58              0.10         24.76                34.81         0.542            pass              0.520             32.6                           0.293                9.82              1.087                                 ok            True                  False
  CTSH           87.50               16            2.27              1.12         70.06                46.28         0.517            pass              0.387             31.6                           0.604               15.52              1.747                                 ok            True                  False
   XEL           86.96               23            0.57              0.31         77.92                17.66         0.505            pass              0.358             11.9                           0.248                4.63              0.538                                 ok            True                  False
  TEAM          100.00               21            2.31              3.67        226.04                47.89         0.503            pass              0.619             31.9                           0.566                7.03              0.997                                 ok            True                  False
   CEG           83.33               36            0.61              1.09        252.98                65.46         0.601            pass              0.513             63.5                           0.371              -14.29             -1.582 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           87.50                8            1.44              0.64         63.52                25.23         0.567            pass              0.314             19.1                           0.377                1.77              0.318                                 ok           False                  False
   PEP           82.14               28            0.30              0.29        135.65                25.03         0.507            pass              0.368             46.8                           0.330                6.85              0.835                                 ok           False                  False
  AAPL           90.00               20            0.93              2.26        346.76                16.45         0.496 below_threshold              0.538             51.7                           0.560                1.03              0.156                                 ok           False                  False
  VRTX           78.95               19            1.38              5.06        521.76                29.59         0.496 below_threshold              0.261             50.5                           0.738                1.91              0.641                                 ok           False                  False
  META           71.43               14            1.58              7.11        639.57                42.27         0.492 below_threshold              0.269             64.5                           0.424              -14.87             -1.822 downtrend_blocked_slope_and_streak           False                  False
 CMCSA          100.00                2            2.91              0.46         22.49                23.68         0.485 below_threshold              0.498             16.5                           0.315                6.53              0.857                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-26T15:10:06.955297-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-26T15:05:03.905393-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-26T15:00:06.230753-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-26T14:55:05.952188-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-26T14:50:06.038156-04:00       entry_1500                   entry {"allocated_cash": 64000.0, "asset_type": "option", "contract_symbol": "TEAM261218C00230000", "contracts": 32, "early_entry_score": 0.492, "entry_mode": "regular", "entry_option_price": 20.0, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 302.0, "option_spread_pct": 10.0, "option_volume": 39.0, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.514}
2026-10-26T14:50:06.038156-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                {"early_entry_score": 0.565, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 81.0, "option_spread_pct": 22.0, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.533}
2026-10-26T14:50:06.038156-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                {"early_entry_score": 0.52, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 722.0, "option_spread_pct": 14.29, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTSH", "timing_score": 0.538}
2026-10-26T14:50:06.038156-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-26", "training_samples": 6183, "window": 5}
2026-10-26T12:00:05.800227-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:55:06.449404-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261026155006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261026155006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261026155006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261026155006)

</details>
