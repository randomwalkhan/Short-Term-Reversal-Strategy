# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 12:50:04 EDT`
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
- Equity: `$30,645.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 14525.0        29.05          29.05       350.6        349.42          bid_ask_mid                      29.05                bid_ask_mid                    True             0.0                    0.0          97.3               37              0.63         45.67           45.93                  37.94                2023.0           40.0               0.13                      ok
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
   TXN           92.31               26            0.82              1.76        307.41                67.99         0.693          pass              0.736             77.4                           0.655                9.32              1.071                                 ok            True                  False
 GOOGL           84.00               25            1.08              3.02        399.77                40.65         0.562          pass              0.412             49.6                           0.563                2.87              0.321                                 ok            True                  False
  GOOG           85.19               27            1.06              2.95        395.90                40.76         0.554          pass              0.449             47.4                           0.434                2.54              0.308                                 ok            True                  False
  SNPS           94.12               17            2.23              7.95        506.61                41.57         0.548          pass              0.598             40.1                           0.541                1.97              0.267                                 ok            True                  False
  CDNS           97.06               34            0.97              2.39        351.82                37.94         0.520          pass              0.769             52.3                           0.477                2.49              0.188                                 ok            True                  False
   WMT           94.74               19            0.96              0.89        132.08                21.34         0.513          pass              0.553             16.3                           0.318               -0.12              0.070                                 ok            True                  False
  NXPI           82.86               35            0.47              0.97        293.76                90.16         0.730          pass              0.572             85.3                           0.825               -0.83              0.052                                 ok           False                  False
 CMCSA           89.47               19            0.82              0.14         25.11                60.26         0.703          pass              0.430             15.8                           0.191               -8.19             -0.966 downtrend_blocked_slope_and_streak           False                  False
  CHTR           66.67                3            5.56              5.76        145.53               114.29         0.619          pass              0.064              0.6                           0.051              -18.62             -1.790            downtrend_blocked_slope           False                  False
   XEL          100.00                3            2.29              1.28         79.48                24.20         0.581          pass              0.487              9.6                           0.221               -5.31             -0.364            downtrend_blocked_slope           False                  False
  GEHC           46.67               15            2.38              1.04         62.22                57.53         0.578          pass              0.112              6.9                           0.287                0.25              0.169                                 ok           False                  False
  INTC          100.00                2            6.56              5.32        113.65               111.79         0.568          pass              0.527             23.3                           0.252                8.74              1.635                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515125004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515125004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515125004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515125004)

</details>
