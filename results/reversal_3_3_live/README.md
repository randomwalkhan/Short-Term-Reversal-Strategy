# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-01 15:45:03 EDT`
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

- Cash: `$23,958.10`
- Equity: `$46,998.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$-720.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   0    144     23760.0                 23040.0         1.65            1.6       32.33         32.36          bid_ask_mid                        1.6                bid_ask_mid                    True          -720.0                  -3.03          87.5               16              1.99         38.72            37.4                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SHOP     option         option SHOP261016C00150000     30          2026-08-31         2026-09-01          8.2        7.38 -2460.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           93.33               30            1.02              0.76        106.99                60.77         0.596          pass              0.657             36.1                           0.326                7.94              0.521                                 ok            True                  False
  PAYX          100.00               15            1.34              1.20        126.83                24.69         0.557          pass              0.553             21.4                           0.332                5.98              0.602                                 ok            True                  False
  CPRT           87.50               16            2.00              0.46         32.79                40.13         0.552          pass              0.320              8.2                           0.311                1.98              0.064                                 ok            True                  False
 CMCSA           90.48               21            1.02              0.19         26.54                24.41         0.531          pass              0.435              9.6                           0.248                3.05              0.237                                 ok            True                  False
  CSCO           86.84               38            0.63              0.49        110.28                40.87         0.527          pass              0.587             55.1                           0.702               -2.75             -0.078                                 ok            True                  False
  NVDA           85.71               28            1.40              2.17        219.57                45.52         0.517          pass              0.452             42.7                           0.355               -1.06              0.128                                 ok            True                  False
  COST           96.43               28            0.74              4.88        941.80                19.33         0.502          pass              0.602             10.6                           0.285               -1.74             -0.156                                 ok            True                  False
  MNST           71.43                7            1.95              0.63         45.65               551.67         1.000          pass              0.122              7.3                           0.195               -1.09             -0.176                                 ok           False                  False
  INSM           89.13               46            0.27              0.23        121.72               109.80         0.770          pass              0.777             85.6                           0.823               -5.32             -0.666            downtrend_blocked_slope           False                  False
  TEAM           78.95               19            3.58              4.87        192.08               115.35         0.701          pass              0.191             20.2                           0.328               14.85              1.380                                 ok           False                  False
  ABNB           93.75               32            0.47              0.60        182.96                62.80         0.660          pass              0.799             73.2                           0.408                1.71              0.093                                 ok           False                  False
  PYPL          100.00               33            0.63              0.23         52.57                53.75         0.620          pass              0.740             41.6                           0.245              -13.40             -1.610 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-01T15:10:01.952718-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-01T15:05:02.102329-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-01T15:00:06.883715-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-01T14:55:03.896264-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-01T14:50:05.175915-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                 {"early_entry_score": 0.709, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 25.0, "option_volume": 5.0, "reason": "no_trade_low_option_liquidity", "ticker": "TRI", "timing_score": 0.593}
2026-09-01T14:50:05.175915-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                            {"early_entry_score": 0.235, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 7.0, "option_spread_pct": 11.24, "option_volume": 8.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.697}
2026-09-01T14:50:05.175915-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-01", "training_samples": 5739, "window": 5}
2026-09-01T14:50:05.175915-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                               {"early_entry_score": 0.536, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 36.0, "option_spread_pct": 15.38, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "PAYX", "timing_score": 0.559}
2026-09-01T14:50:05.175915-04:00       entry_1500                   entry {"allocated_cash": 23760.0, "asset_type": "option", "contract_symbol": "CPRT261016C00032500", "contracts": 144, "early_entry_score": 0.311, "entry_mode": "regular", "entry_option_price": 1.65, "execution_mode": "option", "matched_signals": 16, "option_liquidity_status": "ok", "option_open_interest": 398.0, "option_spread_pct": 6.06, "option_volume": 105.0, "success_rate": 87.5, "ticker": "CPRT", "timing_score": 0.554}
2026-09-01T12:00:06.980016-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260901154503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260901154503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260901154503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260901154503)

</details>
