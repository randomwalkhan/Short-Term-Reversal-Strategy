# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 15:30:02 EDT`
Last processed slot: `manage_1530`

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
- Equity: `$30,995.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$350.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 14875.0        29.05          29.75       350.6         348.4          bid_ask_mid                      29.75                bid_ask_mid                    True           350.0                   2.41          97.3               37              0.63         45.67           49.59                  37.94                2023.0           40.0               0.13                      ok
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
  NXPI           82.35               34            0.58              1.20        293.66                90.16         0.729          pass              0.541             81.8                           0.528               -0.94              0.047                                 ok            True                  False
   TXN           90.00               20            1.39              3.00        306.88                67.99         0.694          pass              0.588             61.6                           0.440                8.68              1.044                                 ok            True                  False
  GOOG           83.33               24            1.19              3.30        395.76                40.76         0.564          pass              0.362             41.2                           0.366                2.41              0.303                                 ok            True                  False
 GOOGL           82.61               23            1.23              3.46        399.59                40.65         0.564          pass              0.339             42.3                           0.370                2.71              0.313                                 ok            True                  False
  CDNS           96.67               30            1.31              3.22        351.46                37.94         0.525          pass              0.693             35.7                           0.358                2.14              0.172                                 ok            True                  False
  SNPS           96.15               26            1.69              6.03        507.43                41.57         0.524          pass              0.723             54.6                           0.639                2.53              0.292                                 ok            True                  False
   WMT           94.74               19            0.97              0.90        132.08                21.34         0.511          pass              0.575             23.6                           0.330               -0.13              0.070                                 ok            True                  False
  MPWR           83.33               18            2.60             29.40       1601.37                52.07         0.506          pass              0.295             34.0                           0.367               -0.73              0.153                                 ok            True                  False
   STX           94.44               36            0.73              4.10        803.00                56.74         0.504          pass              0.864             85.0                           0.621                9.90              1.028                                 ok            True                   True
  MRVL          100.00               23            1.69              2.16        181.66                62.77         0.504          pass              0.761             74.7                           0.537                8.82              0.904                                 ok            True                  False
 CMCSA           90.00               10            1.51              0.27         25.06                60.26         0.709          pass              0.366              9.5                           0.268               -8.83             -0.998 downtrend_blocked_slope_and_streak           False                  False
  INTC          100.00                2            6.15              4.99        113.79               111.79         0.592          pass              0.544             28.1                           0.363                9.22              1.655                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-15T15:10:01.306366-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-15T15:05:04.259285-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-15T15:00:04.164689-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-15T14:55:04.243758-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-15T14:50:02.185201-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T14:50:02.185201-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-15", "training_samples": 5061, "window": 5}
2026-05-15T12:00:02.263118-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:55:05.834638-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:50:01.284692-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:45:04.258436-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515153002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515153002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515153002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515153002)

</details>
