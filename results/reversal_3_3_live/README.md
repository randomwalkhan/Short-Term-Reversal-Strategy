# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-01 09:30:30 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$14,720.50`
- Equity: `$28,960.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$-400.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260821C00130000       2026-06-29                   2     32     14640.0                 14240.0         4.58           4.45      126.19        126.59     last_price_stale                        NaN                unavailable                   False          -400.0                  -2.73         93.33               15              1.32         33.41            1.56                  29.34                 807.0           40.0               0.08                      ok
```

## Today's Closed Trades (2026-07-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SOXL           83.33               12            9.68             18.08        259.06               249.48         0.705          pass              0.217             14.8                           0.341                6.54             -0.213                      ok            True                  False
  UPRO           84.00               25            0.73              0.73        141.53                55.16         0.643          pass              0.414             47.7                           0.541               -2.10             -0.204                      ok            True                  False
  MRVL          100.00               13            4.93             10.28        293.48               157.45         0.631          pass              0.554             23.5                           0.341                1.63             -0.381                      ok            True                  False
  KLAC           90.00               10            4.14              8.75        297.96               103.22         0.601          pass              0.454             42.4                           0.332               21.86              1.849                      ok            True                  False
  ASML           91.67               12            3.49             48.66       1968.58                71.16         0.585          pass              0.428             15.2                           0.217                6.43              0.346                      ok            True                  False
  LRCX          100.00               12            4.28             12.99        427.76                94.12         0.556          pass              0.626             52.2                           0.357               12.38              1.145                      ok            True                  False
  INTC           90.00               20            3.64              3.56        138.10                95.61         0.556          pass              0.449             20.0                           0.311               14.95              0.938                      ok            True                  False
  AVGO           78.26               23            1.29              3.41        376.29                74.76         0.691          pass              0.295             46.5                           0.478               -0.86             -0.576                      ok           False                  False
  MPWR           83.33               24            2.01             19.48       1374.01                91.02         0.659          pass              0.389             46.8                           0.456               -9.62             -1.384 downtrend_blocked_slope           False                  False
   WDC           91.67               12            4.01             17.92        631.04               116.88         0.653          pass              0.533             47.8                           0.448               -9.98             -1.640 downtrend_blocked_slope           False                  False
  MCHP           90.91               22            1.89              1.20         90.68                74.43         0.639          pass              0.503             22.8                           0.345               -6.43             -1.000 downtrend_blocked_slope           False                  False
   TXN           88.89               27            0.98              2.04        297.20                70.14         0.632          pass              0.605             63.9                           0.652               -3.45             -0.796 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-30T17:05:09.028498-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-06-29T15:10:05.899695-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T15:05:05.773719-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T15:00:06.338367-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T14:55:08.793154-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T14:50:09.505108-04:00       entry_1500                   entry {"allocated_cash": 14640.0, "asset_type": "option", "contract_symbol": "GILD260821C00130000", "contracts": 32, "early_entry_score": 0.533, "entry_mode": "regular", "entry_option_price": 4.575, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 807.0, "option_spread_pct": 7.65, "option_volume": 40.0, "success_rate": 93.33, "ticker": "GILD", "timing_score": 0.563}
2026-06-29T14:50:09.505108-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                {"early_entry_score": 0.248, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 22.22, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "EXC", "timing_score": 0.577}
2026-06-29T14:50:09.505108-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-29", "training_samples": 5314, "window": 5}
2026-06-29T12:00:02.850105-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:55:01.636700-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260701093030)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260701093030)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260701093030)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260701093030)

</details>
