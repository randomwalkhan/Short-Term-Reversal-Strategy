# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-26 11:10:05 EDT`
Last processed slot: `manage_1100`

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
  LRCX     option         option LRCX261016C00310000       2026-08-24                   2      9     27315.0                 27202.5        30.35          30.22      310.66         312.2          bid_ask_mid                      30.22                bid_ask_mid                    True          -112.5                  -0.41          87.5               32              1.06         63.04           62.01                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-26)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KHC     option         option KHC261016C00025000    287          2026-08-25         2026-08-26         1.02       0.918 -2927.4       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MNST           92.31               26            0.66              0.22         48.63               552.32         1.000          pass              0.657             40.6                           0.324                5.29              0.601                      ok            True                  False
  ABNB           96.55               29            0.94              1.26        189.96                61.60         0.661          pass              0.609              5.3                           0.135                4.78              0.494                      ok            True                  False
  SHOP           90.00               30            1.60              1.72        153.14                72.08         0.625          pass              0.540             25.8                           0.215                0.67             -0.148                      ok            True                  False
   TRI           88.89               27            1.62              1.19        103.87                66.28         0.604          pass              0.560             49.9                           0.258                0.73              0.321                      ok            True                  False
  WDAY           82.14               28            2.55              3.47        192.93                76.21         0.579          pass              0.335             33.2                           0.213                8.08              0.255                      ok            True                  False
  DXCM           87.88               33            0.95              0.60         88.90                51.46         0.560          pass              0.565             48.5                           0.327               -2.74             -0.102                      ok            True                  False
  MELI           96.77               31            1.16             16.26       1990.03                47.50         0.535          pass              0.652             19.3                           0.254                7.96              1.020                      ok            True                  False
  BKNG           95.65               23            1.61              2.41        212.75                35.36         0.522          pass              0.592             17.8                           0.316               -0.91              0.032                      ok            True                  False
  CPRT           82.14               28            1.35              0.32         33.19                43.23         0.506          pass              0.252              8.1                           0.208               13.42              1.363                      ok            True                  False
  SOXL           80.56               36            0.31              0.25        115.56               150.52         0.811          pass              0.535             88.4                           0.726              -18.89             -2.971 downtrend_blocked_slope           False                  False
  INSM           86.11               36            1.26              1.09        123.42               110.58         0.689          pass              0.615             70.0                           0.409               -7.52             -0.482 downtrend_blocked_slope           False                  False
  MRVL           81.08               37            0.06              0.11        240.33                91.37         0.684          pass              0.565             95.8                           0.513               10.66              0.992                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-08-26T11:10:05.253776-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:05:02.266288-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:00:04.246676-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "DXCM260925C00089000", "current_drop_pct": 0.52, "early_entry_score": 0.684, "early_reclaim_pct": 72.1, "entry_ask": 4.2, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 3.8, "hypothetical_budget": 13730.3, "hypothetical_contracts": 36, "matched_signals": 36, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 54.0, "option_spread_pct": 21.05, "option_volume": 54.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.554, "shadow_only": true, "success_rate": 88.89, "ticker": "DXCM", "timing_score": 0.569, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.684, "early_reclaim_pct": 72.1, "matched_signals": 36, "recovery_stability_score": 0.554, "success_rate": 88.89, "ticker": "DXCM", "timing_score": 0.569, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-26T10:55:01.094732-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:50:01.106808-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:45:02.279556-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:40:01.110768-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:35:05.204853-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:30:05.720184-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:25:04.269067-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260826111005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260826111005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260826111005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260826111005)

</details>
