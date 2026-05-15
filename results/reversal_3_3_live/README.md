# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 12:55:06 EDT`
Last processed slot: `manage_1300`

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
- Equity: `$30,920.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$275.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 14800.0        29.05           29.6       350.6        349.24          bid_ask_mid                       29.6                bid_ask_mid                    True           275.0                   1.89          97.3               37              0.63         45.67           46.24                  37.94                2023.0           40.0               0.13                      ok
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
   TXN           92.31               26            0.81              1.75        307.42                67.99         0.693          pass              0.737             77.6                           0.671                9.32              1.071                                 ok            True                  False
  GOOG           83.33               24            1.16              3.22        395.79                40.76         0.565          pass              0.367             42.6                           0.365                2.44              0.304                                 ok            True                  False
 GOOGL           83.33               24            1.16              3.25        399.68                40.65         0.563          pass              0.376             45.9                           0.397                2.78              0.317                                 ok            True                  False
  SNPS           94.12               17            2.30              8.23        506.49                41.57         0.544          pass              0.592             38.1                           0.449                1.89              0.263                                 ok            True                  False
  CDNS           97.06               34            1.05              2.60        351.73                37.94         0.515          pass              0.756             48.2                           0.414                2.40              0.184                                 ok            True                  False
  NXPI           82.86               35            0.45              0.93        293.77                90.16         0.731          pass              0.573             85.8                           0.819               -0.81              0.053                                 ok           False                  False
 CMCSA           88.89               18            0.89              0.16         25.10                60.26         0.704          pass              0.385              8.2                           0.151               -8.26             -0.970 downtrend_blocked_slope_and_streak           False                  False
  CHTR           66.67                3            5.84              6.05        145.41               114.29         0.599          pass              0.062              0.6                           0.141              -18.86             -1.804            downtrend_blocked_slope           False                  False
   XEL          100.00                3            2.31              1.29         79.48                24.20         0.580          pass              0.485              8.9                           0.236               -5.33             -0.365            downtrend_blocked_slope           False                  False
  GEHC           46.67               15            2.35              1.03         62.23                57.53         0.580          pass              0.116              8.1                           0.364                0.28              0.170                                 ok           False                  False
  INTC          100.00                2            6.87              5.57        113.54               111.79         0.550          pass              0.514             19.7                           0.250                8.38              1.620                                 ok           False                  False
  ISRG           89.29               28            1.11              3.32        426.64                42.54         0.533          pass              0.504             27.6                           0.447               -7.53             -0.826            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                            detail
2026-05-15T12:00:02.263118-04:00 early_entry_1200 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:55:05.834638-04:00 early_entry_1155 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:50:01.284692-04:00 early_entry_1150 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:45:04.258436-04:00 early_entry_1145 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:40:01.250267-04:00 early_entry_1140 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:35:04.114840-04:00 early_entry_1135 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:30:01.141517-04:00 early_entry_1130 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:25:04.096857-04:00 early_entry_1125 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:20:04.254442-04:00      manage_1130          exit {"asset_type": "option", "contract_symbol": "SNPS260618C00490000", "fill_price": 40.23, "pnl": -1341.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-05-15T11:20:04.254442-04:00 early_entry_1120 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515125506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515125506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515125506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515125506)

</details>
