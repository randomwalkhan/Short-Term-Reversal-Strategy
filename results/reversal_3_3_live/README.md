# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-16 15:55:06 EDT`
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

- Cash: `$62,756.80`
- Equity: `$121,906.80`
- Realized PnL: `$112,431.80`
- Unrealized PnL: `$-525.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-10-16                   0     35     59675.0                 59150.0        17.05           16.9      270.43        271.94          bid_ask_mid                       16.9                bid_ask_mid                    True          -525.0                  -0.88         85.71               21              1.66         51.07           47.68                  60.14                 462.0           59.0               0.05                      ok
```

## Today's Closed Trades (2026-10-16)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   CEG     option         option CEG261120C00270000     33          2026-10-15         2026-10-16         19.1       17.19 -6303.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           88.89               27            1.10              2.12        274.09                60.14         0.562            pass              0.546             46.6                           0.559                5.62              0.156                                 ok            True                  False
  DXCM           80.00               10            1.95              1.20         87.20                29.21         0.507            pass              0.082             10.5                           0.286                0.75              0.103                                 ok            True                  False
  SNPS           66.67                6            2.98              9.77        463.92                53.97         0.556            pass              0.145             29.9                           0.609               -7.30             -0.660 downtrend_blocked_slope_and_streak           False                  False
  CSCO           66.67                6            2.28              1.76        109.10                35.07         0.520            pass              0.074              7.4                           0.213               -4.33             -0.432 downtrend_blocked_slope_and_streak           False                  False
  ABNB           92.31               39            0.30              0.37        174.12                41.32         0.515            pass              0.815             80.8                           0.690                6.97              0.694                                 ok           False                  False
  CDNS           80.00               20            1.48              3.35        322.94                38.31         0.507            pass              0.233             38.5                           0.491               -9.04             -1.098 downtrend_blocked_slope_and_streak           False                  False
  MSFT          100.00                9            1.91              7.23        536.34                21.00         0.504            pass              0.544             31.2                           0.479                2.24              0.299                                 ok           False                  False
  QCOM           62.50                8            3.54              4.42        176.51                54.84         0.497 below_threshold              0.058              2.9                           0.205               -6.91             -0.515 downtrend_blocked_slope_and_streak           False                  False
  VRTX           70.00               10            1.87              6.66        505.90                25.61         0.492 below_threshold              0.096             15.5                           0.282               -1.09             -0.101                                 ok           False                  False
  INTU           85.71               21            1.66              3.85        328.52                41.38         0.487 below_threshold              0.397             41.0                           0.679               16.05              1.473                                 ok           False                  False
  DASH           77.27               22            1.96              2.65        191.91                48.67         0.485 below_threshold              0.265             45.5                           0.606                0.06             -0.082                                 ok           False                  False
  ALNY           80.00               35            1.14              1.87        233.23                44.37         0.483 below_threshold              0.221              2.0                           0.100                5.30              0.473                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-16T15:10:05.870833-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-16T15:05:04.429616-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-16T15:00:06.363478-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-16T14:55:05.627788-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-16T14:50:06.542626-04:00       entry_1500              entry {"allocated_cash": 59675.0, "asset_type": "option", "contract_symbol": "CEG261120C00270000", "contracts": 35, "early_entry_score": 0.326, "entry_mode": "regular", "entry_option_price": 17.05, "execution_mode": "option", "matched_signals": 21, "option_liquidity_status": "ok", "option_open_interest": 462.0, "option_spread_pct": 5.28, "option_volume": 59.0, "success_rate": 85.71, "ticker": "CEG", "timing_score": 0.564}
2026-10-16T14:50:06.542626-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-16", "training_samples": 6095, "window": 5}
2026-10-16T12:00:06.321774-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:55:06.475716-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:50:05.492018-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:45:05.286618-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261016155506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261016155506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261016155506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261016155506)

</details>
