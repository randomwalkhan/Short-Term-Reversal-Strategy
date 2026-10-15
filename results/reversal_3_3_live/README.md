# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-15 15:35:02 EDT`
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

- Cash: `$65,704.80`
- Equity: `$129,889.80`
- Realized PnL: `$118,734.80`
- Unrealized PnL: `$1,155.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-10-15                   0     33     63030.0                 64185.0         19.1          19.45       273.7        274.44          bid_ask_mid                      19.45                bid_ask_mid                    True          1155.0                   1.83         81.25               16              2.09         51.04           50.45                  59.82                 446.0           21.0               0.05                      ok
```

## Today's Closed Trades (2026-10-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CSCO     option         option CSCO261120C00115000    115          2026-10-14         2026-10-15         5.85       5.265 -6727.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           85.00               20            1.86              3.65        277.98                59.82         0.547            pass              0.424             56.3                           0.613                5.95              0.790                                 ok            True                  False
    ZS           91.89               37            0.56              0.87        220.42                59.94         0.541            pass              0.808             85.7                           0.837               10.45              1.409                                 ok            True                   True
  TMUS           85.19               27            0.79              0.88        157.41                59.52         0.602            pass              0.428             38.6                           0.336               -3.21             -0.738            downtrend_blocked_slope           False                  False
  META           86.11               36            0.21              1.11        737.06                55.15         0.571            pass              0.672             92.8                           0.551                1.38              0.191                                 ok           False                  False
  SNPS           71.43                7            2.83              9.50        475.86                52.37         0.561            pass              0.196             46.7                           0.669               -4.93             -0.267 downtrend_blocked_slope_and_streak           False                  False
  SOXL           83.33               30            2.16              1.67        109.82               111.12         0.504            pass              0.526             84.4                           0.951              -29.63             -4.279 downtrend_blocked_slope_and_streak           False                  False
  CDNS           77.78               18            1.82              4.20        327.66                37.41         0.498 below_threshold              0.270             55.7                           0.666               -7.78             -0.820 downtrend_blocked_slope_and_streak           False                  False
   PEP           79.17               24            0.43              0.39        129.10                22.64         0.485 below_threshold              0.358             72.2                           0.414                2.48              0.274                                 ok           False                  False
  INTC           87.10               31            1.83              1.26         97.58                68.27         0.483 below_threshold              0.611             77.8                           0.865              -19.73             -2.305            downtrend_blocked_slope           False                  False
   AEP           55.56                9            1.26              1.12        125.65                12.92         0.477 below_threshold              0.117             22.9                           0.326                4.00              0.547                                 ok           False                  False
   XEL           86.67               30            0.25              0.13         75.30                17.56         0.474 below_threshold              0.474             38.3                           0.328                6.56              0.655                                 ok           False                  False
  CRWD           83.33               18            2.83              4.94        247.17                48.36         0.471 below_threshold              0.266             25.5                           0.383               -8.97             -0.909 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-10-15T15:10:06.431411-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-10-15T15:05:05.112020-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-10-15T15:00:05.139552-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-10-15T14:55:07.089564-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-10-15T14:50:07.219015-04:00       entry_1500              entry {"allocated_cash": 63030.0, "asset_type": "option", "contract_symbol": "CEG261120C00270000", "contracts": 33, "early_entry_score": 0.282, "entry_mode": "regular", "entry_option_price": 19.1, "execution_mode": "option", "matched_signals": 16, "option_liquidity_status": "ok", "option_open_interest": 446.0, "option_spread_pct": 5.24, "option_volume": 21.0, "success_rate": 81.25, "ticker": "CEG", "timing_score": 0.554}
2026-10-15T14:50:07.219015-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                       {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-15", "training_samples": 6074, "window": 5}
2026-10-15T12:00:06.622764-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:55:05.998701-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:50:06.396498-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:45:05.042150-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261015153502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261015153502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261015153502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261015153502)

</details>
