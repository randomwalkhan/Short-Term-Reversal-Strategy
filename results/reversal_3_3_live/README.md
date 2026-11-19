# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-19 10:05:05 EST`
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
- Equity: `$106,293.80`
- Realized PnL: `$95,918.80`
- Unrealized PnL: `$375.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   APP     option         option APP270115C00400000       2026-11-18                   1     15     49725.0                 50100.0        33.15           33.4      389.81        383.56          bid_ask_mid                       33.4                bid_ask_mid                    True           375.0                   0.75         90.91               22              2.29         60.57           66.16                 121.47                4183.0           24.0               0.06                      ok
```

## Today's Closed Trades (2026-11-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   APP           90.91               22            2.28              6.25        388.23               121.61         0.781          pass              0.503             18.0                           0.194                7.27              0.340                  ok            True                  False
  IDXX           96.15               26            1.24              6.08        695.86                78.12         0.721          pass              0.644             21.9                           0.227                2.84              0.195                  ok            True                  False
  REGN           82.35               17            1.75             11.56        940.57                54.27         0.611          pass              0.240             23.0                           0.222                2.89              0.468                  ok            True                  False
 CMCSA           92.86               14            1.56              0.28         25.12                34.19         0.566          pass              0.463             12.2                           0.201               -0.42              0.259                  ok            True                  False
  COST           88.89               18            0.83              6.39       1093.88                23.52         0.555          pass              0.382             12.1                           0.174                2.06              0.443                  ok            True                  False
  ABNB           89.74               39            0.57              0.71        179.90                55.20         0.548          pass              0.669             53.6                           0.337                5.33             -0.073                  ok            True                  False
  AAPL           95.65               23            0.79              1.95        351.61                27.20         0.540          pass              0.631             30.1                           0.284                1.67              0.221                  ok            True                  False
  VRSK           80.00               20            1.79              2.54        201.22                47.31         0.537          pass              0.177             18.8                           0.266               -6.05             -0.177                  ok            True                  False
  GILD           85.00               20            1.33              1.58        168.30                31.08         0.520          pass              0.312             19.9                           0.226               -0.50             -0.007                  ok            True                  False
   CSX           85.00               20            1.11              0.40         51.16                35.07         0.519          pass              0.311             19.7                           0.218               -0.14              0.225                  ok            True                  False
  ODFL           89.47               38            0.63              0.78        174.78                43.99         0.518          pass              0.604             37.6                           0.257                2.02              0.412                  ok            True                  False
   ROP           86.96               23            1.16              3.83        469.23                42.60         0.516          pass              0.397             24.3                           0.189               -5.21             -0.246                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-11-19T10:05:05.527736-05:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:00:06.381004-05:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T00:00:05.435730-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 91, 'empty': 2}
2026-11-18T15:10:05.947802-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-11-18T15:05:06.246695-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-11-18T15:00:06.306059-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-11-18T14:55:05.603926-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-11-18T14:50:05.341851-05:00       entry_1500              entry {"allocated_cash": 49725.0, "asset_type": "option", "contract_symbol": "APP270115C00400000", "contracts": 15, "early_entry_score": 0.497, "entry_mode": "regular", "entry_option_price": 33.15, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 4183.0, "option_spread_pct": 5.73, "option_volume": 24.0, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.787}
2026-11-18T14:50:05.341851-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-18", "training_samples": 6259, "window": 5}
2026-11-18T12:00:06.155878-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261119100505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261119100505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261119100505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261119100505)

</details>
