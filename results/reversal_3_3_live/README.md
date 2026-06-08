# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-08 15:50:06 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$16,069.75`
- Equity: `$30,774.75`
- Realized PnL: `$21,794.75`
- Unrealized PnL: `$-1,020.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260717C00100000       2026-06-08                   0     17     15725.0                 14705.0         9.25           8.65       97.75         97.75          bid_ask_mid                       8.65                bid_ask_mid                    True         -1020.0                  -6.49         93.94               33              1.73         79.38           74.66                  86.36                1396.0           69.0               0.05                      ok
```

## Today's Closed Trades (2026-06-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM260717C00100000     16          2026-06-05         2026-06-08         9.85       8.865 -1576.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  TEAM           93.94               33            1.73              1.20         98.95                86.36         0.623          pass              0.733             48.7                           0.465               14.43              1.803                      ok            True                  False
  ROST           89.47               19            1.27              2.05        229.49                43.36         0.612          pass              0.396              7.3                           0.228               -3.14             -0.174                      ok            True                  False
  CRWD           81.25               16            2.29             10.74        666.42                64.90         0.576          pass              0.189             19.3                           0.314                1.15              0.933                      ok            True                  False
  PANW           82.35               17            2.20              4.19        270.25                60.15         0.575          pass              0.231             21.5                           0.259                5.20              1.163                      ok            True                  False
  MSFT           88.00               25            1.00              2.91        415.42                34.82         0.560          pass              0.516             48.8                           0.641               -1.45              0.123                      ok            True                  False
  AMGN           90.00               10            1.23              3.00        348.29                22.27         0.538          pass              0.537             72.1                           0.553                1.77              0.301                      ok            True                  False
   ADP           95.65               23            1.16              1.89        231.14                32.55         0.529          pass              0.652             37.4                           0.359                1.75              0.587                      ok            True                  False
  DASH           86.96               23            2.10              2.30        155.81                51.66         0.517          pass              0.443             39.7                           0.308               -3.61             -0.113                      ok            True                  False
  FAST           90.91               22            1.05              0.34         46.64                21.36         0.509          pass              0.522             33.4                           0.368                5.37              0.690                      ok            True                  False
  AAPL           90.91               11            1.75              3.77        305.73                17.55         0.507          pass              0.360              3.9                           0.205               -2.22             -0.046                      ok            True                  False
    ZS           82.76               29            1.38              1.27        130.24               157.69         0.898          pass              0.412             40.6                           0.282              -29.28             -2.420 downtrend_blocked_slope           False                  False
  PAYX          100.00                8            1.54              1.08        100.07                33.39         0.621          pass              0.526             21.2                           0.261                2.05              0.531                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-08T15:10:01.789141-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-08T15:05:04.798011-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-08T15:00:02.588621-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-08T14:55:02.835387-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-08T14:50:04.804691-04:00       entry_1500              entry {"allocated_cash": 15725.0, "asset_type": "option", "contract_symbol": "TEAM260717C00100000", "contracts": 17, "early_entry_score": 0.733, "entry_mode": "regular", "entry_option_price": 9.25, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 1396.0, "option_spread_pct": 5.41, "option_volume": 69.0, "success_rate": 93.94, "ticker": "TEAM", "timing_score": 0.623}
2026-06-08T14:50:04.804691-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-08", "training_samples": 5231, "window": 5}
2026-06-08T12:35:06.508215-04:00      manage_1230               exit                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "TEAM260717C00100000", "fill_price": 8.865, "pnl": -1576.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TEAM"}
2026-06-08T12:00:05.977560-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:55:06.347594-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:50:04.863668-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260608155006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260608155006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260608155006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260608155006)

</details>
