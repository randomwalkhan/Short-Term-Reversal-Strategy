# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-17 15:05:06 EDT`
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

- Cash: `$15,119.25`
- Equity: `$29,224.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   TXN     option         option TXN260821C00290000       2026-07-17                   0      7     14105.0                 14105.0        20.15          20.15      284.95        285.16          bid_ask_mid                      20.15                bid_ask_mid                    True             0.0                    0.0          90.0               20              2.15         62.88           63.29                  64.46                 207.0          231.0               0.09                      ok
```

## Today's Closed Trades (2026-07-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MDLZ          100.00               14            0.78              0.34         61.28                33.43         0.610          pass              0.602             38.1                           0.532                0.05              0.072                  ok            True                  False
   KHC           90.91               11            1.05              0.19         26.15                36.78         0.602          pass              0.457             32.9                           0.455                2.31              0.352                  ok            True                  False
   TXN           90.91               22            2.08              4.24        289.40                64.46         0.595          pass              0.579             49.4                           0.618               -2.70             -0.207                  ok            True                  False
   ADI           84.00               25            1.42              3.79        378.90                54.65         0.582          pass              0.447             60.6                           0.659               -0.54             -0.002                  ok            True                  False
  ASML           93.10               29            1.52             18.96       1776.75                64.12         0.564          pass              0.733             66.8                           0.533               -0.65             -0.040                  ok            True                  False
   XEL          100.00               13            1.11              0.62         79.71                21.95         0.557          pass              0.567             30.5                           0.528               -3.50             -0.199                  ok            True                  False
  NXPI           85.19               27            1.34              2.53        269.57                54.99         0.542          pass              0.516             70.2                           0.610               -2.31             -0.217                  ok            True                  False
  GILD           89.47               19            1.24              1.18        135.79                34.67         0.526          pass              0.403             12.4                           0.219                2.54              0.100                  ok            True                  False
   CSX           88.24               17            0.89              0.32         50.75                21.08         0.526          pass              0.395             25.4                           0.385                3.16              0.395                  ok            True                  False
   ADP           96.30               27            0.70              1.25        256.02                34.79         0.522          pass              0.760             65.0                           0.601                5.16              0.574                  ok            True                  False
  CTAS           81.25               16            1.62              2.35        205.24                39.81         0.514          pass              0.210             28.4                           0.375               11.87              1.266                  ok            True                  False
  BKNG           85.71               21            1.65              2.14        183.69                41.98         0.513          pass              0.420             47.8                           0.565               -1.63              0.017                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-07-17T15:05:06.030959-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-17T15:00:09.838561-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-17T14:55:11.420522-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-17T14:50:08.434742-04:00       entry_1500                   entry {"allocated_cash": 14105.0, "asset_type": "option", "contract_symbol": "TXN260821C00290000", "contracts": 7, "early_entry_score": 0.537, "entry_mode": "regular", "entry_option_price": 20.15, "execution_mode": "option", "matched_signals": 20, "option_liquidity_status": "ok", "option_open_interest": 207.0, "option_spread_pct": 8.93, "option_volume": 231.0, "success_rate": 90.0, "ticker": "TXN", "timing_score": 0.602}
2026-07-17T14:50:08.434742-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                         {"early_entry_score": 0.572, "option_liquidity_status": "low_volume", "option_open_interest": 709.0, "option_spread_pct": 11.11, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "MDLZ", "timing_score": 0.602}
2026-07-17T14:50:08.434742-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                       {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-17", "training_samples": 5456, "window": 5}
2026-07-17T12:00:05.871771-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:55:01.882856-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:50:01.906755-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:45:01.890808-04:00 early_entry_1145      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260717150506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260717150506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260717150506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260717150506)

</details>
