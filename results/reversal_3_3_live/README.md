# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 15:00:04 EDT`
Last processed slot: `entry_1500`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$16,120.00`
- Equity: `$31,245.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$600.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 15125.0        29.05          30.25       350.6        348.19          bid_ask_mid                      30.25                bid_ask_mid                    True           600.0                   4.13          97.3               37              0.63         45.67           50.35                  37.94                2023.0           40.0               0.13                      ok
```

## Today's Closed Trades (2026-05-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-14         2026-05-15        32.35      29.115 -1617.5       -10.0 stop_loss_hit_at_scan
  SNPS     option         option SNPS260618C00490000      3          2026-05-13         2026-05-15        44.70      40.230 -1341.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           92.31               26            0.85              1.84        307.38                67.99         0.691          pass              0.733             76.5                           0.637                9.28              1.069                                 ok            True                  False
 GOOGL           83.33               24            1.13              3.17        399.71                40.65         0.564          pass              0.380             47.2                           0.425                2.81              0.318                                 ok            True                  False
  GOOG           85.19               27            1.08              3.01        395.88                40.76         0.553          pass              0.446             46.4                           0.415                2.52              0.307                                 ok            True                  False
  SNPS           95.83               24            1.86              6.64        507.18                41.57         0.527          pass              0.696             50.0                           0.479                2.36              0.284                                 ok            True                  False
  CDNS           96.67               30            1.30              3.21        351.47                37.94         0.526          pass              0.694             36.0                           0.281                2.15              0.173                                 ok            True                  False
  MPWR           88.00               25            1.80             20.29       1605.27                52.07         0.515          pass              0.528             54.4                           0.711                0.09              0.191                                 ok            True                  False
  MRVL          100.00               25            1.47              1.88        181.78                62.77         0.504          pass              0.784             78.0                           0.687                9.06              0.914                                 ok            True                  False
  NXPI           85.00               40            0.08              0.16        294.10                90.16         0.725          pass              0.699             97.6                           0.740               -0.44              0.070                                 ok           False                  False
 CMCSA           90.00               10            1.53              0.27         25.05                60.26         0.709          pass              0.356              6.1                           0.143               -8.85             -0.999 downtrend_blocked_slope_and_streak           False                  False
  INTC          100.00                7            5.36              4.35        114.07               111.79         0.606          pass              0.573             37.3                           0.587               10.14              1.693                                 ok           False                  False
  GEHC           46.67               15            2.20              0.97         62.26                57.53         0.588          pass              0.135             14.3                           0.403                0.43              0.177                                 ok           False                  False
   XEL          100.00                3            2.30              1.29         79.48                24.20         0.575          pass              0.523             21.7                           0.486               -5.32             -0.365            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-15T15:00:04.164689-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-15T14:55:04.243758-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-15T14:50:02.185201-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T14:50:02.185201-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-15", "training_samples": 5061, "window": 5}
2026-05-15T12:00:02.263118-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:55:05.834638-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:50:01.284692-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:45:04.258436-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:40:01.250267-04:00 early_entry_1140  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:35:04.114840-04:00 early_entry_1135  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515150004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515150004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515150004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515150004)

</details>
