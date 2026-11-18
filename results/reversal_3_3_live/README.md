# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-18 09:42:05 EST`
Last processed slot: `manual`

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

- Cash: `$58,029.80`
- Equity: `$102,654.80`
- Realized PnL: `$101,239.80`
- Unrealized PnL: `$-8,585.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   APP     option         option APP261218C00400000       2026-11-17                   1     17     53210.0                 44625.0         31.3          26.25      402.79        403.22          bid_ask_mid                      26.25                bid_ask_mid                    True         -8585.0                 -16.13         94.12               17              2.99         63.29           61.55                  119.5                1252.0          197.0               0.01                      ok
```

## Today's Closed Trades (2026-11-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
   BKR           87.50               32            0.51              0.17         47.39                58.51         0.621          pass              0.491             27.3                           0.229               -4.86             -0.029                       ok            True                  False
   TXN           92.00               25            1.05              2.18        294.93                59.80         0.614          pass              0.574             30.7                           0.292               -6.02              0.186                       ok            True                  False
   ADI           92.11               38            0.59              1.57        383.00                67.50         0.597          pass              0.713             47.9                           0.343               -6.11              0.130                       ok            True                  False
  MDLZ           95.65               23            0.52              0.24         66.65                29.89         0.572          pass              0.738             64.6                           0.698               -1.45              0.022                       ok            True                  False
  TMUS           81.48               27            0.99              1.16        167.40                47.29         0.567          pass              0.296             29.0                           0.432                4.44              0.515                       ok            True                  False
  INSM           84.09               44            0.68              0.58        121.61                62.27         0.553          pass              0.420             18.6                           0.372               10.03              1.109                       ok            True                  False
  ABNB           89.74               39            0.57              0.72        180.63                55.65         0.550          pass              0.644             45.1                           0.406                2.01              0.197                       ok            True                  False
   CEG           90.62               32            1.51              2.84        266.85                61.66         0.534          pass              0.483              0.0                           0.170                7.61              1.114                       ok            True                  False
  COST           84.00               25            0.53              4.08       1108.33                22.66         0.532          pass              0.421             53.6                           0.548                5.52              0.633                       ok            True                  False
  SOXL           62.96               27            2.95              1.01         48.64               265.73         0.927          pass              0.286             26.8                           0.161              -28.58             -0.495  downtrend_blocked_slope           False                  False
  INTC           67.86               28            2.14              0.83         54.82               143.31         0.809          pass              0.285             28.0                           0.254               -7.35             -0.133 downtrend_blocked_streak           False                  False
  ALNY           82.61               46            0.48              0.53        156.27               110.55         0.743          pass              0.518             58.1                           0.468               -3.31              0.034                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-11-18T00:00:06.344355-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 91, 'empty': 2}
2026-11-17T15:10:05.988632-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-11-17T15:05:03.951251-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-11-17T15:00:05.898014-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-11-17T14:55:04.972939-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-11-17T14:50:06.628486-05:00       entry_1500              entry {"allocated_cash": 53210.0, "asset_type": "option", "contract_symbol": "APP261218C00400000", "contracts": 17, "early_entry_score": 0.66, "entry_mode": "regular", "entry_option_price": 31.3, "execution_mode": "option", "matched_signals": 17, "option_liquidity_status": "ok", "option_open_interest": 1252.0, "option_spread_pct": 1.28, "option_volume": 197.0, "success_rate": 94.12, "ticker": "APP", "timing_score": 0.778}
2026-11-17T14:50:06.628486-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-17", "training_samples": 6239, "window": 5}
2026-11-17T12:00:06.286293-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:55:01.833366-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:50:06.047053-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261118094205)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261118094205)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261118094205)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261118094205)

</details>
