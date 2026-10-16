# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-16 15:45:06 EDT`
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

- Cash: `$62,756.80`
- Equity: `$120,506.80`
- Realized PnL: `$112,431.80`
- Unrealized PnL: `$-1,925.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-10-16                   0     35     59675.0                 57750.0        17.05           16.5      270.43         270.8          bid_ask_mid                       16.5                bid_ask_mid                    True         -1925.0                  -3.23         85.71               21              1.66         51.07           49.17                  60.14                 462.0           59.0               0.05                      ok
```

## Today's Closed Trades (2026-10-16)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   CEG     option         option CEG261120C00270000     33          2026-10-15         2026-10-16         19.1       17.19 -6303.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           86.36               22            1.59              3.05        273.69                60.14         0.562            pass              0.376             23.2                           0.362                5.11              0.134                                 ok            True                  False
  ABNB           91.67               36            0.57              0.70        173.98                41.32         0.516            pass              0.727             63.6                           0.626                6.68              0.681                                 ok            True                   True
  DXCM           80.00               10            1.93              1.18         87.20                29.21         0.509            pass              0.085             11.5                           0.316                0.77              0.104                                 ok            True                  False
  SNPS           66.67                6            3.19             10.45        463.63                53.97         0.545            pass              0.130             25.1                           0.487               -7.50             -0.670 downtrend_blocked_slope_and_streak           False                  False
  QCOM           70.00               10            3.09              3.86        176.75                54.84         0.520            pass              0.090             12.7                           0.267               -6.48             -0.494 downtrend_blocked_slope_and_streak           False                  False
  CSCO           60.00                5            2.37              1.82        109.07                35.07         0.515            pass              0.058              2.3                           0.256               -4.41             -0.436 downtrend_blocked_slope_and_streak           False                  False
  MSFT          100.00                3            2.52              9.50        535.37                21.00         0.506            pass              0.479              9.6                           0.262                1.61              0.271                                 ok           False                  False
  DASH           75.00               12            2.78              3.76        191.44                48.67         0.495 below_threshold              0.131             22.8                           0.470               -0.77             -0.121                                 ok           False                  False
  CDNS           77.78               18            1.90              4.32        322.53                38.31         0.493 below_threshold              0.164             20.6                           0.390               -9.43             -1.118 downtrend_blocked_slope_and_streak           False                  False
  PYPL           91.30               23            1.11              0.44         56.97                24.34         0.492 below_threshold              0.485             15.9                           0.267                7.05              0.619                                 ok           False                  False
  GILD           91.67               24            1.02              1.12        156.89                24.67         0.492 below_threshold              0.475              7.0                           0.187                7.62              0.845                                 ok           False                  False
  MPWR           72.22               18            2.70             23.64       1239.07                56.34         0.491 below_threshold              0.161             19.6                           0.232              -15.58             -2.025            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-16T15:10:05.870833-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-16T15:05:04.429616-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-16T15:00:06.363478-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-16T14:55:05.627788-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-16T14:50:06.542626-04:00       entry_1500              entry {"allocated_cash": 59675.0, "asset_type": "option", "contract_symbol": "CEG261120C00270000", "contracts": 35, "early_entry_score": 0.326, "entry_mode": "regular", "entry_option_price": 17.05, "execution_mode": "option", "matched_signals": 21, "option_liquidity_status": "ok", "option_open_interest": 462.0, "option_spread_pct": 5.28, "option_volume": 59.0, "success_rate": 85.71, "ticker": "CEG", "timing_score": 0.564}
2026-10-16T14:50:06.542626-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-16", "training_samples": 6095, "window": 5}
2026-10-16T12:00:06.321774-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:55:06.475716-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:50:05.492018-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:45:05.286618-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261016154506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261016154506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261016154506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261016154506)

</details>
