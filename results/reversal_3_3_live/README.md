# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 12:20:01 EDT`
Last processed slot: `manage_1230`

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
- Equity: `$30,820.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$175.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 14700.0        29.05           29.4       350.6        348.82          bid_ask_mid                       29.4                bid_ask_mid                    True           175.0                    1.2          97.3               37              0.63         45.67           47.93                  37.94                2023.0           40.0               0.13                      ok
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
  NXPI           80.65               31            0.99              2.04        293.29                90.16         0.723          pass              0.436             68.9                           0.625               -1.35              0.028                                 ok            True                  False
   TXN           92.31               26            0.86              1.86        307.37                67.99         0.691          pass              0.733             76.3                           0.636                9.27              1.069                                 ok            True                  False
 GOOGL           82.61               23            1.25              3.50        399.57                40.65         0.563          pass              0.337             41.7                           0.357                2.69              0.313                                 ok            True                  False
  GOOG           83.33               24            1.21              3.36        395.73                40.76         0.562          pass              0.359             40.1                           0.351                2.39              0.302                                 ok            True                  False
  SNPS          100.00               12            2.74              9.76        505.84                41.57         0.558          pass              0.549             26.5                           0.541                1.44              0.243                                 ok            True                  False
  CDNS           96.77               31            1.20              2.98        351.56                37.94         0.525          pass              0.714             40.6                           0.437                2.24              0.177                                 ok            True                  False
  AMAT           80.00               30            1.06              3.27        439.16                48.70         0.510          pass              0.415             76.8                           0.539               12.03              1.194                                 ok            True                  False
  CHTR           80.00                5            4.72              4.89        145.90               114.29         0.680          pass              0.072              1.3                           0.229              -17.89             -1.750            downtrend_blocked_slope           False                  False
 CMCSA           88.89               27            0.51              0.09         25.13                60.26         0.675          pass              0.562             47.9                           0.539               -7.90             -0.952 downtrend_blocked_slope_and_streak           False                  False
   XEL          100.00                6            2.02              1.13         79.54                24.20         0.582          pass              0.472              4.7                           0.237               -5.05             -0.352            downtrend_blocked_slope           False                  False
  FTNT           97.92               48            0.07              0.06        121.84                71.29         0.580          pass              0.952             98.0                           0.653               41.13              3.922                                 ok           False                  False
  GEHC           46.67               15            2.38              1.04         62.22                57.53         0.579          pass              0.110              6.3                           0.102                0.25              0.169                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515122001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515122001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515122001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515122001)

</details>
