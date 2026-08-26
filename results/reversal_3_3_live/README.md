# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-26 11:15:01 EDT`
Last processed slot: `early_entry_1115`

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

- Cash: `$27,460.60`
- Equity: `$54,663.10`
- Realized PnL: `$44,775.60`
- Unrealized PnL: `$-112.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   2      9     27315.0                 27202.5        30.35          30.22      310.66        312.01          bid_ask_mid                      30.22                bid_ask_mid                    True          -112.5                  -0.41          87.5               32              1.06         63.04           62.52                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-26)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KHC     option         option KHC261016C00025000    287          2026-08-25         2026-08-26         1.02       0.918 -2927.4       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MNST           91.30               23            0.77              0.26         48.62               552.32         1.000          pass              0.579             30.4                           0.277                5.17              0.595                      ok            True                  False
  ABNB           96.67               30            0.86              1.14        190.01                61.60         0.660          pass              0.647             16.0                           0.243                4.87              0.498                      ok            True                  False
  SHOP           90.00               30            1.67              1.80        153.11                72.08         0.621          pass              0.529             22.2                           0.206                0.60             -0.151                      ok            True                  False
  REGN          100.00               10            1.68              9.78        829.37                29.20         0.598          pass              0.493             11.1                           0.188                2.83              0.423                      ok            True                  False
   TRI           88.46               26            1.84              1.34        103.80                66.28         0.597          pass              0.522             43.2                           0.230                0.51              0.311                      ok            True                  False
  WDAY           82.14               28            2.35              3.20        193.05                76.21         0.591          pass              0.351             38.4                           0.265                8.31              0.264                      ok            True                  False
  DXCM           86.67               30            1.02              0.64         88.89                51.46         0.573          pass              0.503             44.8                           0.295               -2.81             -0.105                      ok            True                  False
  MELI           96.67               30            1.25             17.54       1989.48                47.50         0.536          pass              0.626             13.0                           0.222                7.86              1.016                      ok            True                  False
  BKNG           95.65               23            1.59              2.38        212.76                35.36         0.523          pass              0.596             19.0                           0.293               -0.89              0.033                      ok            True                  False
  CPRT           82.76               29            1.32              0.31         33.20                43.23         0.503          pass              0.281             10.2                           0.278               13.45              1.365                      ok            True                  False
  SOXL           80.00               35            0.84              0.68        115.38               150.52         0.794          pass              0.453             69.1                           0.566              -19.32             -2.995 downtrend_blocked_slope           False                  False
  DRAM           75.68               37            0.19              0.07         56.21                90.57         0.711          pass              0.515             88.1                           0.597                2.44             -0.127                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-08-26T11:15:01.102404-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:10:05.253776-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:05:02.266288-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:00:04.246676-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "DXCM260925C00089000", "current_drop_pct": 0.52, "early_entry_score": 0.684, "early_reclaim_pct": 72.1, "entry_ask": 4.2, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 3.8, "hypothetical_budget": 13730.3, "hypothetical_contracts": 36, "matched_signals": 36, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 54.0, "option_spread_pct": 21.05, "option_volume": 54.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.554, "shadow_only": true, "success_rate": 88.89, "ticker": "DXCM", "timing_score": 0.569, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.684, "early_reclaim_pct": 72.1, "matched_signals": 36, "recovery_stability_score": 0.554, "success_rate": 88.89, "ticker": "DXCM", "timing_score": 0.569, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-26T10:55:01.094732-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:50:01.106808-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:45:02.279556-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:40:01.110768-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:35:05.204853-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:30:05.720184-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260826111501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260826111501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260826111501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260826111501)

</details>
