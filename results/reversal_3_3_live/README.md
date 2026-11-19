# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-19 10:00:06 EST`
Last processed slot: `manage_1000`

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

- Cash: `$56,193.80`
- Equity: `$108,693.80`
- Realized PnL: `$95,918.80`
- Unrealized PnL: `$2,775.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   APP     option         option APP270115C00400000       2026-11-18                   1     15     49725.0                 52500.0        33.15           35.0      389.81        383.86          bid_ask_mid                       35.0                bid_ask_mid                    True          2775.0                   5.58         90.91               22              2.29         60.57           69.66                 121.47                4183.0           24.0               0.06                      ok
```

## Today's Closed Trades (2026-11-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   APP           92.59               27            2.06              5.65        388.49               121.61         0.774          pass              0.526              0.0                           0.177                7.51              0.350                  ok            True                  False
  IDXX           95.83               24            1.39              6.78        695.57                78.12         0.725          pass              0.570              1.4                           0.165                2.70              0.188                  ok            True                  False
 CMCSA           92.86               14            1.55              0.27         25.12                34.19         0.569          pass              0.434              2.5                           0.073               -0.40              0.260                  ok            True                  False
  SBUX           80.00               10            1.69              1.29        108.56                31.90         0.554          pass              0.117             20.7                           0.244                1.64              0.155                  ok            True                  False
  FAST           90.91               11            1.15              0.43         53.77                20.11         0.553          pass              0.371              6.1                           0.170                0.83              0.097                  ok            True                  False
  AAPL          100.00               22            0.83              2.05        351.57                27.20         0.549          pass              0.615             26.6                           0.226                1.63              0.219                  ok            True                  False
  ABNB           89.74               39            0.61              0.77        179.88                55.20         0.545          pass              0.658             50.0                           0.282                5.28             -0.075                  ok            True                  False
  COST           86.36               22            0.59              4.52       1094.68                23.52         0.542          pass              0.417             37.8                           0.443                2.31              0.454                  ok            True                  False
   MAR           80.00               10            1.61              4.80        423.11                24.12         0.540          pass              0.114             19.9                           0.213                0.25              0.105                  ok            True                  False
  VRSK           80.00               20            1.84              2.61        201.19                47.31         0.534          pass              0.170             16.6                           0.232               -6.10             -0.179                  ok            True                  False
   CSX           83.33               18            1.18              0.42         51.15                35.07         0.527          pass              0.202              2.4                           0.159               -0.21              0.222                  ok            True                  False
  ODFL           88.24               34            0.89              1.09        174.64                43.99         0.525          pass              0.471             12.9                           0.198                1.76              0.400                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-11-19T10:00:06.381004-05:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T00:00:05.435730-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 91, 'empty': 2}
2026-11-18T15:10:05.947802-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-11-18T15:05:06.246695-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-11-18T15:00:06.306059-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-11-18T14:55:05.603926-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-11-18T14:50:05.341851-05:00       entry_1500              entry {"allocated_cash": 49725.0, "asset_type": "option", "contract_symbol": "APP270115C00400000", "contracts": 15, "early_entry_score": 0.497, "entry_mode": "regular", "entry_option_price": 33.15, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 4183.0, "option_spread_pct": 5.73, "option_volume": 24.0, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.787}
2026-11-18T14:50:05.341851-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-18", "training_samples": 6259, "window": 5}
2026-11-18T12:00:06.155878-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:55:05.147885-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261119100006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261119100006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261119100006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261119100006)

</details>
