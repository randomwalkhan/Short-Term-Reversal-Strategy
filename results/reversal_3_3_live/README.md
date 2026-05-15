# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 11:45:04 EDT`
Last processed slot: `early_entry_1145`

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
- Equity: `$31,420.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$775.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 15300.0        29.05           30.6       350.6        347.76          bid_ask_mid                       30.6                bid_ask_mid                    True           775.0                   5.34          97.3               37              0.63         45.67           52.08                  37.94                2023.0           40.0               0.13                      ok
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
  NXPI           82.35               34            0.68              1.39        293.57                90.16         0.724          pass              0.532             78.8                           0.784               -1.04              0.042                                 ok            True                  False
   TXN           92.59               27            0.80              1.74        307.43                67.99         0.689          pass              0.751             77.8                           0.736                9.33              1.071                                 ok            True                  False
  GOOG           81.82               22            1.23              3.41        395.71                40.76         0.572          pass              0.304             39.3                           0.269                2.37              0.301                                 ok            True                  False
 GOOGL           82.61               23            1.25              3.51        399.56                40.65         0.563          pass              0.337             41.4                           0.298                2.69              0.312                                 ok            True                  False
   KDP           87.50               24            0.98              0.20         29.01                33.62         0.546          pass              0.389             13.6                           0.104               -0.95              0.067                                 ok            True                  False
  CDNS           96.30               27            1.50              3.72        351.25                37.94         0.532          pass              0.644             25.8                           0.247                1.93              0.163                                 ok            True                  False
 CMCSA           89.47               19            0.85              0.15         25.11                60.26         0.701          pass              0.420             12.2                           0.161               -8.22             -0.968 downtrend_blocked_slope_and_streak           False                  False
  CHTR           71.43                7            4.32              4.48        146.08               114.29         0.682          pass              0.092              8.0                           0.092              -17.55             -1.731            downtrend_blocked_slope           False                  False
  QCOM           93.02               43            0.02              0.04        200.06                98.98         0.652          pass              0.909             98.8                           0.416               13.00              1.852                                 ok           False                  False
  GEHC           46.67               15            2.09              0.92         62.28                57.53         0.595          pass              0.146             17.6                           0.179                0.54              0.182                                 ok           False                  False
  INTC          100.00                2            6.29              5.10        113.74               111.79         0.584          pass              0.538             26.4                           0.460                9.05              1.648                                 ok           False                  False
   XEL          100.00                6            2.04              1.14         79.54                24.20         0.582          pass              0.464              1.8                           0.164               -5.06             -0.352            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                            detail
2026-05-15T11:45:04.258436-04:00 early_entry_1145 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:40:01.250267-04:00 early_entry_1140 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:35:04.114840-04:00 early_entry_1135 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:30:01.141517-04:00 early_entry_1130 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:25:04.096857-04:00 early_entry_1125 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:20:04.254442-04:00 early_entry_1120 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:20:04.254442-04:00      manage_1130          exit {"asset_type": "option", "contract_symbol": "SNPS260618C00490000", "fill_price": 40.23, "pnl": -1341.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-05-15T11:15:04.096489-04:00 early_entry_1115 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:10:04.211296-04:00 early_entry_1110 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:05:04.217696-04:00 early_entry_1105 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515114504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515114504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515114504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515114504)

</details>
