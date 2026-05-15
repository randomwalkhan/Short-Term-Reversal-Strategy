# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 11:55:05 EDT`
Last processed slot: `manage_1200`

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
- Equity: `$31,520.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$875.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 15400.0        29.05           30.8       350.6        347.61          bid_ask_mid                       30.8                bid_ask_mid                    True           875.0                   6.02          97.3               37              0.63         45.67           52.33                  37.94                2023.0           40.0               0.13                      ok
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
   TXN           92.00               25            1.04              2.24        307.21                67.99         0.687          pass              0.703             71.4                           0.639                9.08              1.061                                 ok            True                  False
  GOOG           85.71               21            1.34              3.74        395.57                40.76         0.576          pass              0.384             33.4                           0.220                2.25              0.295                                 ok            True                  False
 GOOGL           85.71               21            1.39              3.91        399.40                40.65         0.571          pass              0.387             34.9                           0.245                2.54              0.306                                 ok            True                  False
   KDP           88.00               25            0.93              0.19         29.02                33.62         0.543          pass              0.422             18.2                           0.143               -0.89              0.069                                 ok            True                  False
  SNPS          100.00               11            3.22             11.48        505.10                41.57         0.538          pass              0.501             13.5                           0.256                0.94              0.220                                 ok            True                  False
  CDNS           96.43               28            1.50              3.70        351.25                37.94         0.527          pass              0.651             26.1                           0.195                1.94              0.163                                 ok            True                  False
   WMT           94.12               17            1.00              0.93        132.06                21.34         0.524          pass              0.476              0.0                           0.150               -0.17              0.068                                 ok            True                  False
  NXPI           77.78               27            1.30              2.68        293.02                90.16         0.725          pass              0.363             59.2                           0.625               -1.66              0.014                                 ok           False                  False
  CHTR           77.78                9            4.15              4.29        146.16               114.29         0.687          pass              0.104             11.9                           0.112              -17.40             -1.723            downtrend_blocked_slope           False                  False
 CMCSA           88.89               27            0.62              0.11         25.12                60.26         0.669          pass              0.526             36.4                           0.351               -8.00             -0.957 downtrend_blocked_slope_and_streak           False                  False
  QCOM           92.50               40            0.16              0.22        199.99                98.98         0.661          pass              0.876             92.3                           0.386               12.86              1.846                                 ok           False                  False
  FTNT           97.78               45            0.26              0.22        121.76                71.29         0.587          pass              0.935             92.2                           0.566               40.85              3.913                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                            detail
2026-05-15T11:55:05.834638-04:00 early_entry_1155 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:50:01.284692-04:00 early_entry_1150 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:45:04.258436-04:00 early_entry_1145 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:40:01.250267-04:00 early_entry_1140 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:35:04.114840-04:00 early_entry_1135 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:30:01.141517-04:00 early_entry_1130 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:25:04.096857-04:00 early_entry_1125 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:20:04.254442-04:00 early_entry_1120 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:20:04.254442-04:00      manage_1130          exit {"asset_type": "option", "contract_symbol": "SNPS260618C00490000", "fill_price": 40.23, "pnl": -1341.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-05-15T11:15:04.096489-04:00 early_entry_1115 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515115505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515115505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515115505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515115505)

</details>
