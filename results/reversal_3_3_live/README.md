# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-26 15:30:06 EDT`
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

- Cash: `$1,421.80`
- Equity: `$136,049.30`
- Realized PnL: `$127,691.80`
- Unrealized PnL: `$-1,642.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261218C00230000       2026-10-26                   0     32     64000.0                 64000.0         20.0          20.00      220.60        220.88          bid_ask_mid                      20.00                bid_ask_mid                    True             0.0                   0.00         100.0               12              3.08         70.90           70.20                  47.89                 302.0           39.0               0.10                      ok
   EXC     option         option  EXC261218C00045000       2026-10-23                   1    657     72270.0                 70627.5          1.1           1.08       44.42         44.49          bid_ask_mid                       1.08                bid_ask_mid                    True         -1642.5                  -2.27          80.0               15              0.97         20.09           20.24                  20.91                 278.0           48.0               0.09                      ok
```

## Today's Closed Trades (2026-10-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM261120C00230000     40          2026-10-22         2026-10-26        17.85      16.065 -7140.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CTSH          100.00               11            2.68              1.32         69.97                46.28         0.537            pass              0.518             19.2                           0.285               15.03              1.728                                 ok            True                  False
  TEAM          100.00               13            2.96              4.71        225.59                47.89         0.515            pass              0.509             12.7                           0.329                6.32              0.967                                 ok            True                  False
  TMUS           84.85               33            0.46              0.47        146.34                64.13         0.631            pass              0.569             74.4                           0.706               -3.95             -0.386            downtrend_blocked_slope           False                  False
   CEG           86.36               44            0.08              0.15        253.39                65.46         0.589            pass              0.713             94.9                           0.638              -13.83             -1.558 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           87.50                8            1.36              0.61         63.54                25.23         0.572            pass              0.329             23.8                           0.519                1.85              0.322                                 ok           False                  False
   ADP           77.78                9            1.43              3.05        302.85                24.93         0.546            pass              0.101             15.4                           0.320                9.49              1.091                                 ok           False                  False
   KHC           91.89               37            0.20              0.03         24.79                34.81         0.514            pass              0.781             77.4                           0.795               10.25              1.105                                 ok           False                  False
   PEP           80.77               26            0.37              0.35        135.62                25.03         0.514            pass              0.284             35.1                           0.317                6.78              0.832                                 ok           False                  False
  VRTX           66.67                9            1.93              7.08        520.89                29.59         0.512            pass              0.143             30.7                           0.429                1.34              0.616                                 ok           False                  False
  PCAR           80.00                5            2.34              1.75        106.21                21.43         0.496 below_threshold              0.112             20.9                           0.236               -3.40             -0.182                                 ok           False                  False
 CMCSA          100.00                2            2.73              0.43         22.50                23.68         0.494 below_threshold              0.514             21.5                           0.521                6.72              0.865                                 ok           False                  False
  AAPL           88.89               18            1.23              2.99        346.44                16.45         0.490 below_threshold              0.448             36.1                           0.444                0.73              0.143                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261026153006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261026153006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261026153006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261026153006)

</details>
