# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-01 15:05:02 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$23,958.10`
- Equity: `$46,998.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$-720.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   0    144     23760.0                 23040.0         1.65            1.6       32.33         32.31          bid_ask_mid                        1.6                bid_ask_mid                    True          -720.0                  -3.03          87.5               16              1.99         38.72           38.01                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SHOP     option         option SHOP261016C00150000     30          2026-08-31         2026-09-01          8.2        7.38 -2460.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           80.00               10            1.67              0.54         45.69               551.67         1.000            pass              0.139             13.1                           0.387               -0.80             -0.163                                 ok            True                  False
   TRI           93.33               30            1.05              0.79        106.98                60.77         0.593            pass              0.649             33.7                           0.308                7.90              0.520                                 ok            True                  False
  PAYX          100.00               14            1.42              1.26        126.80                24.69         0.559            pass              0.534             17.1                           0.353                5.90              0.599                                 ok            True                  False
  CPRT           87.50               16            1.99              0.46         32.79                40.13         0.554            pass              0.311              5.1                           0.150                2.00              0.065                                 ok            True                  False
  CSCO           85.71               35            0.73              0.57        110.25                40.87         0.538            pass              0.517             48.1                           0.616               -2.85             -0.083                                 ok            True                  False
 CMCSA           90.48               21            0.96              0.18         26.54                24.41         0.536            pass              0.418              3.8                           0.193                3.11              0.240                                 ok            True                  False
  NVDA           85.71               28            1.38              2.13        219.59                45.52         0.519            pass              0.455             43.7                           0.386               -1.04              0.129                                 ok            True                  False
  COST           96.67               30            0.60              3.93        942.20                19.33         0.500 below_threshold              0.614             10.4                           0.167               -1.60             -0.149                                 ok            True                  False
  INSM           86.49               37            0.88              0.75        121.50               109.80         0.780            pass              0.591             53.5                           0.608               -5.90             -0.694            downtrend_blocked_slope           False                  False
  TEAM           77.78               18            3.72              5.06        192.00               115.35         0.697            pass              0.174             17.1                           0.236               14.69              1.374                                 ok           False                  False
  ABNB           94.74               38            0.25              0.32        183.08                62.80         0.639            pass              0.901             85.7                           0.458                1.94              0.103                                 ok           False                  False
  PYPL          100.00               38            0.41              0.15         52.60                53.75         0.604            pass              0.833             61.9                           0.356              -13.21             -1.601 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-01T15:05:02.102329-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-01T15:00:06.883715-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-01T14:55:03.896264-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-01T14:50:05.175915-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-01", "training_samples": 5739, "window": 5}
2026-09-01T14:50:05.175915-04:00       entry_1500                   entry {"allocated_cash": 23760.0, "asset_type": "option", "contract_symbol": "CPRT261016C00032500", "contracts": 144, "early_entry_score": 0.311, "entry_mode": "regular", "entry_option_price": 1.65, "execution_mode": "option", "matched_signals": 16, "option_liquidity_status": "ok", "option_open_interest": 398.0, "option_spread_pct": 6.06, "option_volume": 105.0, "success_rate": 87.5, "ticker": "CPRT", "timing_score": 0.554}
2026-09-01T14:50:05.175915-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                               {"early_entry_score": 0.536, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 36.0, "option_spread_pct": 15.38, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "PAYX", "timing_score": 0.559}
2026-09-01T14:50:05.175915-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                 {"early_entry_score": 0.709, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 25.0, "option_volume": 5.0, "reason": "no_trade_low_option_liquidity", "ticker": "TRI", "timing_score": 0.593}
2026-09-01T14:50:05.175915-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                            {"early_entry_score": 0.235, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 7.0, "option_spread_pct": 11.24, "option_volume": 8.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.697}
2026-09-01T12:00:06.980016-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:55:07.200979-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260901150502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260901150502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260901150502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260901150502)

</details>
