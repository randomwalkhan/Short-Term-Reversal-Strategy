# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 15:50:01 EDT`
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

- Cash: `$1,008.10`
- Equity: `$46,818.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$-900.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 23760.0         1.65           1.65       32.33         32.24          bid_ask_mid                       1.65                bid_ask_mid                    True             0.0                   0.00          87.5               16              1.99         38.72           41.36                  40.13                 398.0          105.0               0.06                      ok
  MSTR     option         option MSTR261009C00122000       2026-09-02                   0     20     22950.0                 22050.0        11.48          11.02      122.50        122.81          bid_ask_mid                      11.02                bid_ask_mid                    True          -900.0                  -3.92          80.0               30              1.91         71.34           67.32                  86.77                 141.0           20.0               0.07                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           81.25               32            1.61              1.41        124.28                86.77         0.597          pass              0.381             47.1                           0.530               17.86              1.567                                 ok            True                  False
  COST           93.33               15            1.21              7.97        936.55                19.36         0.531          pass              0.568             42.1                           0.540               -2.97             -0.197                                 ok            True                  False
    ZS          100.00               18            2.95              3.68        176.79                60.79         0.525          pass              0.582             25.4                           0.275               -6.22              0.055                                 ok            True                  False
  PAYX          100.00               16            1.27              1.11        125.16                25.34         0.512          pass              0.623             44.0                           0.351                1.27              0.225                                 ok            True                  False
  MNST           86.67               15            1.24              0.39         44.82               424.41         1.000          pass              0.434             41.1                           0.689               -6.33             -0.719            downtrend_blocked_slope           False                  False
   WDC           80.56               36            0.38              1.21        449.92                82.26         0.649          pass              0.513             86.8                           0.833               -2.89             -0.214           downtrend_blocked_streak           False                  False
   STX           86.67               30            1.12              6.41        813.89                70.47         0.595          pass              0.582             70.4                           0.763               -3.01             -0.249           downtrend_blocked_streak           False                  False
  MRVL           79.41               34            1.87              2.75        209.21                79.24         0.560          pass              0.345             43.0                           0.413              -12.98             -1.682 downtrend_blocked_slope_and_streak           False                  False
  FAST          100.00               13            1.34              0.46         48.55                20.15         0.531          pass              0.595             40.7                           0.441               -6.50             -0.590 downtrend_blocked_slope_and_streak           False                  False
  INTU           91.89               37            0.40              0.96        344.52                46.23         0.518          pass              0.775             75.5                           0.533               -5.22             -0.559            downtrend_blocked_slope           False                  False
  AMAT           86.11               36            0.65              2.00        441.00                44.19         0.515          pass              0.584             65.6                           0.595              -11.43             -1.250 downtrend_blocked_slope_and_streak           False                  False
  LRCX           82.86               35            0.86              1.74        289.45                48.78         0.510          pass              0.465             57.1                           0.511               -6.34             -0.692 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-02T15:10:01.537083-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-02T15:05:01.526637-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-02T15:00:06.384646-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-02T14:58:03.772540-04:00       entry_1500              entry {"allocated_cash": 22950.0, "asset_type": "option", "contract_symbol": "MSTR261009C00122000", "contracts": 20, "early_entry_score": 0.304, "entry_mode": "regular", "entry_option_price": 11.475, "execution_mode": "option", "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 141.0, "option_spread_pct": 6.54, "option_volume": 20.0, "success_rate": 80.0, "ticker": "MSTR", "timing_score": 0.589}
2026-09-02T14:58:03.772540-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-02", "training_samples": 5758, "window": 5}
2026-09-02T12:00:02.480923-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:55:01.504562-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:50:01.337983-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:45:01.308184-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:40:01.399320-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902155001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902155001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902155001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902155001)

</details>
