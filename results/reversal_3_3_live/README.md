# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-09 15:45:06 EDT`
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

- Cash: `$14,359.25`
- Equity: `$28,819.25`
- Realized PnL: `$18,399.25`
- Unrealized PnL: `$420.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260821C00135000       2026-07-09                   0     24     14040.0                 14460.0         5.85           6.02      133.88        134.93          bid_ask_mid                       6.02                bid_ask_mid                    True           420.0                   2.99         93.33               15              1.42          35.3           33.09                  35.14                8090.0           34.0               0.07                      ok
```

## Today's Closed Trades (2026-07-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
   CSX     option         option  CSX260821C00047500     54          2026-07-07         2026-07-09        2.350      3.0750  3915.0   30.851064 take_profit_day2_hit_at_scan
  PAYX     option         option PAYX260821C00110000     50          2026-07-08         2026-07-09        2.525      2.2725 -1262.5  -10.000000        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN           92.31               13            1.26              3.26        366.59                27.70         0.536          pass              0.501             33.2                           0.512                3.39              0.437                                 ok            True                  False
  PAYX          100.00               28            0.53              0.39        106.41                32.56         0.531          pass              0.814             80.3                           0.599               10.09              1.176                                 ok            True                  False
   ADP           96.15               26            0.60              1.01        240.94                32.32         0.527          pass              0.789             76.7                           0.783                9.13              1.237                                 ok            True                  False
  GILD           88.46               26            0.68              0.65        135.54                35.14         0.515          pass              0.625             80.5                           0.777                7.77              0.933                                 ok            True                  False
  CTAS           83.33               18            1.52              1.91        179.35                32.70         0.509          pass              0.282             29.5                           0.372                3.81              0.708                                 ok            True                  False
  MDLZ          100.00                4            1.77              0.74         59.16                30.45         0.581          pass              0.485              9.1                           0.187               -4.58             -0.257 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           77.78               18            0.02              0.00         23.19                30.42         0.573          pass              0.407             98.7                           0.783                3.80              0.307                                 ok           False                  False
   KDP          100.00               13            1.05              0.23         30.87                33.74         0.568          pass              0.616             46.3                           0.328               -1.71             -0.473 downtrend_blocked_slope_and_streak           False                  False
   XEL          100.00               20            0.77              0.43         79.44                21.16         0.525          pass              0.605             28.7                           0.392               -3.02             -0.305            downtrend_blocked_slope           False                  False
  CPRT           80.00               20            1.38              0.28         28.47                44.46         0.518          pass              0.268             49.7                           0.699               -7.25             -0.511            downtrend_blocked_slope           False                  False
   TRI           82.86               35            0.16              0.10         88.85                40.11         0.515          pass              0.576             93.9                           0.817                9.59              1.161                                 ok           False                  False
  MSFT           78.95               38            0.07              0.18        383.26                38.03         0.508          pass              0.531             97.8                           0.871                4.82              0.758                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-07-09T15:10:06.797522-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-09T15:05:11.506156-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-09T15:00:11.129710-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-09T14:55:10.687527-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-09T14:50:10.393351-04:00       entry_1500              entry {"allocated_cash": 14040.0, "asset_type": "option", "contract_symbol": "GILD260821C00135000", "contracts": 24, "early_entry_score": 0.621, "entry_mode": "regular", "entry_option_price": 5.85, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 8090.0, "option_spread_pct": 6.84, "option_volume": 34.0, "success_rate": 93.33, "ticker": "GILD", "timing_score": 0.541}
2026-07-09T14:50:10.393351-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-09", "training_samples": 5465, "window": 5}
2026-07-09T12:00:04.046756-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:55:06.157143-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:50:05.085430-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:45:03.060463-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260709154506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260709154506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260709154506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260709154506)

</details>
