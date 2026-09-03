# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-03 09:40:01 EDT`
Last processed slot: `manage_0930`

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
- Equity: `$48,040.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$322.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   2    144     23760.0                 24192.0         1.65           1.68       32.33         33.95     last_price_stale                        NaN                unavailable                   False           432.0                   1.82          87.5               16              1.99         38.72             0.0                  40.13                 398.0          105.0               0.06                      ok
  MSTR     option         option MSTR261009C00122000       2026-09-02                   1     20     22950.0                 22840.0        11.48          11.42      122.50        132.18     last_price_stale                        NaN                unavailable                   False          -110.0                  -0.48          80.0               30              1.91         71.34             0.0                  86.77                 141.0           20.0               0.07                      ok
```

## Today's Closed Trades (2026-09-03)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CHTR           90.91               44            0.50              0.56        158.73                59.56         0.519            pass              0.722             59.6                           0.457                7.05              0.408                                 ok            True                  False
  CSCO           88.24               34            0.76              0.58        109.20                36.36         0.518            pass              0.577             48.6                           0.427               -0.89             -0.135                                 ok            True                  False
  PANW           86.36               44            0.62              1.43        327.87                70.92         0.509            pass              0.624             67.8                           0.427               -6.61             -0.241                                 ok            True                  False
  MNST           89.47               38            0.14              0.04         44.40               424.20         0.999            pass              0.765             75.1                           0.450               -6.59             -0.930 downtrend_blocked_slope_and_streak           False                  False
  MRVL           81.08               37            0.87              1.26        205.94                78.54         0.619            pass              0.471             66.7                           0.570              -18.45             -2.008 downtrend_blocked_slope_and_streak           False                  False
  MCHP           88.46               26            1.61              0.82         72.41                58.99         0.569            pass              0.537             49.4                           0.318               -5.00             -0.493            downtrend_blocked_slope           False                  False
  DRAM           83.33               30            2.58              1.02         55.77                63.42         0.507            pass              0.347             24.7                           0.256               -4.90             -0.271            downtrend_blocked_slope           False                  False
  AMGN           96.77               31            0.22              0.67        442.55                21.97         0.505            pass              0.816             75.1                           0.508                2.48              0.037                                 ok           False                  False
  INSM           87.50               24            1.63              1.45        126.01               111.12         0.494 below_threshold              0.382             13.2                           0.260               -0.42             -0.123                                 ok           False                  False
   KHC           81.82               11            2.40              0.44         26.07                29.16         0.490 below_threshold              0.104              0.0                           0.190                0.23              0.185                                 ok           False                  False
  MDLZ           90.00               20            1.33              0.58         62.20                20.19         0.489 below_threshold              0.411              9.7                           0.160               -3.93             -0.466 downtrend_blocked_slope_and_streak           False                  False
   STX           86.36               22            3.41             19.29        800.27                70.48         0.488 below_threshold              0.415             38.7                           0.440               -8.15             -0.497 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-03T00:00:02.675455-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-09-02T15:10:01.537083-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-02T15:05:01.526637-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-02T15:00:06.384646-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-02T14:58:03.772540-04:00       entry_1500              entry {"allocated_cash": 22950.0, "asset_type": "option", "contract_symbol": "MSTR261009C00122000", "contracts": 20, "early_entry_score": 0.304, "entry_mode": "regular", "entry_option_price": 11.475, "execution_mode": "option", "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 141.0, "option_spread_pct": 6.54, "option_volume": 20.0, "success_rate": 80.0, "ticker": "MSTR", "timing_score": 0.589}
2026-09-02T14:58:03.772540-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-02", "training_samples": 5758, "window": 5}
2026-09-02T12:00:02.480923-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:55:01.504562-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:50:01.337983-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:45:01.308184-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260903094001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260903094001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260903094001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260903094001)

</details>
