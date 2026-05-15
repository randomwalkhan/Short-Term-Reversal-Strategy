# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 11:20:04 EDT`
Last processed slot: `manage_1130`

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
- Equity: `$31,495.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$850.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 15375.0        29.05          30.75       350.6        350.12          bid_ask_mid                      30.75                bid_ask_mid                    True           850.0                   5.85          97.3               37              0.63         45.67           49.55                  37.94                2023.0           40.0               0.13                      ok
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
  NXPI           81.25               32            0.87              1.79        293.40                90.16         0.724          pass              0.471             72.8                           0.695               -1.23              0.034                                 ok            True                  False
   TXN           92.31               26            0.81              1.74        307.42                67.99         0.694          pass              0.737             77.7                           0.677                9.33              1.071                                 ok            True                  False
  SNPS          100.00               11            2.97             10.61        505.47                41.57         0.557          pass              0.495             11.0                           0.143                1.20              0.232                                 ok            True                  False
 GOOGL           87.10               31            0.80              2.24        400.11                40.65         0.544          pass              0.572             62.7                           0.605                3.16              0.333                                 ok            True                  False
  GOOG           87.50               32            0.78              2.16        396.24                40.76         0.542          pass              0.585             61.5                           0.580                2.83              0.321                                 ok            True                  False
   KDP           90.00               30            0.62              0.13         29.05                33.62         0.532          pass              0.590             45.5                           0.270               -0.58              0.083                                 ok            True                  False
  CDNS           97.30               37            0.81              2.01        351.98                37.94         0.510          pass              0.811             59.9                           0.557                2.65              0.195                                 ok            True                  False
  CHTR           66.67               12            3.12              3.23        146.61               114.29         0.714          pass              0.186             33.6                           0.240              -16.51             -1.674            downtrend_blocked_slope           False                  False
 CMCSA           88.89               27            0.56              0.10         25.13                60.26         0.677          pass              0.418              0.0                           0.008               -7.94             -0.954 downtrend_blocked_slope_and_streak           False                  False
  GEHC           57.14               21            1.66              0.73         62.36                57.53         0.596          pass              0.237             34.6                           0.314                0.98              0.202                                 ok           False                  False
  MELI           81.82               11            2.71             30.44       1594.32                58.02         0.578          pass              0.128              5.0                           0.215              -15.47             -2.061            downtrend_blocked_slope           False                  False
  INTC          100.00                2            6.48              5.26        113.68               111.79         0.573          pass              0.530             24.2                           0.377                8.83              1.639                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                            detail
2026-05-15T11:20:04.254442-04:00 early_entry_1120 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:20:04.254442-04:00      manage_1130          exit {"asset_type": "option", "contract_symbol": "SNPS260618C00490000", "fill_price": 40.23, "pnl": -1341.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-05-15T11:15:04.096489-04:00 early_entry_1115 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:10:04.211296-04:00 early_entry_1110 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:05:04.217696-04:00 early_entry_1105 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:00:05.390084-04:00 early_entry_1100 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T10:55:04.100799-04:00 early_entry_1055 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T10:50:04.174954-04:00 early_entry_1050 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T10:45:04.262629-04:00 early_entry_1045 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T10:40:01.261107-04:00 early_entry_1040 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515112004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515112004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515112004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515112004)

</details>
